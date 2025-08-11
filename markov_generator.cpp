#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <iomanip>
#include <stdexcept>
#include <random>
#include <chrono>
using namespace std;

static string read_file2(const string &path){
    ifstream f(path);
    if(!f) throw runtime_error("Cannot open model file: " + path);
    stringstream ss; ss << f.rdbuf();
    return ss.str();
}

// Very small JSON helpers tailored to the model format produced by analyzer.
// We parse lengths -> map<int,double>, single_chars -> map<char,double>, initial_bigrams -> map<string,double>, chains -> map<string,map<string,double>>

static void trim(string &s){ size_t a = s.find_first_not_of(" \t\n\r"); size_t b = s.find_last_not_of(" \t\n\r"); if(a==string::npos) { s=""; return;} s = s.substr(a, b-a+1); }

static string extract_object(const string &s, const string &key){
    // find "key" and return the brace-enclosed substring that follows (the object including braces)
    string pat = "\"" + key + "\"";
    size_t pos = s.find(pat);
    if(pos==string::npos) return "";
    pos = s.find_first_of('{', pos+pat.size());
    if(pos==string::npos) return "";
    int depth=0; size_t start = pos;
    for(size_t i=pos;i<s.size();++i){ if(s[i]=='{') depth++; else if(s[i]=='}'){ depth--; if(depth==0) return s.substr(start, i-start+1); } }
    return "";
}

static map<int,double> parse_lengths(const string &obj){
    map<int,double> out;
    // remove braces
    string t = obj; if(t.size()>=2) t = t.substr(1,t.size()-2);
    // split by commas at top level
    size_t i=0;
    while(i<t.size()){
        // find key
        size_t q1 = t.find('\"', i);
        if(q1==string::npos) break;
        size_t q2 = t.find('\"', q1+1);
        if(q2==string::npos) break;
        string key = t.substr(q1+1, q2-q1-1);
        size_t colon = t.find(':', q2);
        if(colon==string::npos) break;
        size_t j = colon+1;
        // read number
        while(j<t.size() && (t[j]==' '||t[j]=='\t')) j++;
        size_t k = j;
        while(k<t.size() && ( (t[k]>='0'&&t[k]<='9') || t[k]=='.' || t[k]=='e' || t[k]=='E' || t[k]=='-' || t[k]=='+')) k++;
        string num = t.substr(j,k-j);
        try{ double v = stod(num); out[stoi(key)] = v; } catch(...){}
        i = k;
    }
    return out;
}

static map<char,double> parse_single_chars(const string &obj){
    map<char,double> out;
    string t = obj; if(t.size()>=2) t = t.substr(1,t.size()-2);
    size_t i=0;
    while(i<t.size()){
        size_t q1 = t.find('\"', i);
        if(q1==string::npos) break;
        size_t q2 = t.find('\"', q1+1);
        if(q2==string::npos) break;
        string key = t.substr(q1+1, q2-q1-1);
        size_t colon = t.find(':', q2);
        if(colon==string::npos) break;
        size_t j = colon+1; while(j<t.size() && isspace((unsigned char)t[j])) j++;
        size_t k=j; while(k<t.size() && ( (t[k]>='0'&&t[k]<='9') || t[k]=='.' || t[k]=='e' || t[k]=='E' || t[k]=='-' || t[k]=='+')) k++;
        string num = t.substr(j,k-j);
        if(!key.empty()){
            try{ double v = stod(num); out[key[0]] = v; } catch(...){}
        }
        i=k;
    }
    return out;
}

static map<string,double> parse_string_map(const string &obj){
    map<string,double> out;
    string t = obj; if(t.size()>=2) t = t.substr(1,t.size()-2);
    size_t i=0;
    while(i<t.size()){
        size_t q1 = t.find('\"', i);
        if(q1==string::npos) break;
        size_t q2 = t.find('\"', q1+1);
        if(q2==string::npos) break;
        string key = t.substr(q1+1, q2-q1-1);
        size_t colon = t.find(':', q2);
        if(colon==string::npos) break;
        size_t j = colon+1; while(j<t.size() && isspace((unsigned char)t[j])) j++;
        size_t k=j; while(k<t.size() && ( (t[k]>='0'&&t[k]<='9') || t[k]=='.' || t[k]=='e' || t[k]=='E' || t[k]=='-' || t[k]=='+')) k++;
        string num = t.substr(j,k-j);
        try{ double v = stod(num); out[key] = v; } catch(...){}
        i=k;
    }
    return out;
}

static map<string,map<string,double>> parse_chains(const string &obj){
    map<string,map<string,double>> out;
    // obj looks like { "ab": { "c": 0.3, "$": 0.7 }, "xy": { ... } }
    // We iterate top-level keys
    size_t i=0;
    string t = obj; if(t.size()>=2) t = t.substr(1,t.size()-2);
    while(i<t.size()){
        size_t q1 = t.find('\"', i);
        if(q1==string::npos) break;
        size_t q2 = t.find('\"', q1+1); if(q2==string::npos) break;
        string key = t.substr(q1+1, q2-q1-1);
        size_t brace = t.find('{', q2);
        if(brace==string::npos) break;
        int depth=0; size_t start = brace; size_t end=start;
        for(size_t k=brace;k<t.size();++k){ if(t[k]=='{') depth++; else if(t[k]=='}'){ depth--; if(depth==0){ end=k; break; } } }
        if(end<=start) break;
        string inner = t.substr(start, end-start+1);
        auto mapinner = parse_string_map(inner);
        out[key] = mapinner;
        i = end+1;
    }
    return out;
}

// sampler helpers

template<typename T>
T sample_from(const vector<pair<T,double>> &vec, mt19937 &rng){
    double r = uniform_real_distribution<double>(0.0, 1.0)(rng);
    double acc = 0.0;
    for(auto &p: vec){ acc += p.second; if(r <= acc) return p.first; }
    return vec.back().first; // numerical fallback
}

int main_gen(int argc,char**argv){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(argc < 3){ cerr<<"Usage: markov_generator model.json NUM_WORDS [seed]\n"; return 1; }
    string modelpath = argv[1];
    int N = stoi(argv[2]);
    unsigned int seed = (argc>=4? (unsigned int)stoul(argv[3]) : (unsigned int)chrono::high_resolution_clock::now().time_since_epoch().count());
    mt19937 rng(seed);

    string content;
    try{ content = read_file2(modelpath); } catch(exception &e){ cerr<<e.what()<<"\n"; return 2; }

    string lengths_obj = extract_object(content, "lengths");
    string single_obj = extract_object(content, "single_chars");
    string init_obj = extract_object(content, "initial_bigrams");
    string chains_obj = extract_object(content, "chains");
    if(lengths_obj.empty() || init_obj.empty() || chains_obj.empty()){ cerr<<"Model seems invalid or missing fields.\n"; return 3; }

    auto lengths = parse_lengths(lengths_obj);
    auto single_chars = parse_single_chars(single_obj);
    auto initial_bigrams = parse_string_map(init_obj);
    auto chains = parse_chains(chains_obj);

    // build sampler vectors
    vector<pair<int,double>> lengths_vec; for(auto &p: lengths) lengths_vec.emplace_back(p.first, p.second);
    sort(lengths_vec.begin(), lengths_vec.end(), [](auto &a, auto &b){ return a.first < b.first; });

    vector<pair<string,double>> init_vec; for(auto &p: initial_bigrams) init_vec.emplace_back(p.first, p.second);
    if(init_vec.empty()){ cerr<<"No initial bigrams in model.\n"; return 4; }

    // global fallback char distribution from chains
    unordered_map<string,double> global_char_prob; // char -> prob (we accumulate)
    double total_glob = 0.0;
    for(auto &outer: chains){
        for(auto &inner: outer.second){ if(inner.first!="$") { global_char_prob[inner.first] += inner.second; total_glob += inner.second; } }
    }
    vector<pair<string,double>> global_char_vec;
    for(auto &p: global_char_prob) global_char_vec.emplace_back(p.first, p.second / (total_glob>0? total_glob:1.0));
    sort(global_char_vec.begin(), global_char_vec.end());

    // single char vec
    vector<pair<string,double>> single_vec;
    for(auto &p: single_chars) single_vec.emplace_back(string(1,p.first), p.second);
    if(single_vec.empty()){
        // fallback: build single letter distribution from initial bigrams first letter
        unordered_map<string,double> fallback;
        for(auto &p: init_vec){ string s = p.first; if(s.size()>=1) fallback[string(1,s[0])] += p.second; }
        for(auto &p: fallback) single_vec.emplace_back(p.first, p.second);
    }
    // normalize single_vec
    double ssum = 0.0; for(auto &p: single_vec) ssum += p.second; for(auto &x: single_vec) x.second /= (ssum>0? ssum:1.0);

    // normalize init_vec
    double isum = 0.0; for(auto &p: init_vec) isum += p.second; for(auto &x: init_vec) x.second /= (isum>0? isum:1.0);

    // normalize global_char_vec already normalized

    // prepare chain vectors map
    unordered_map<string, vector<pair<string,double>>> chain_vecs;
    for(auto &p: chains){
        vector<pair<string,double>> v;
        double sum=0.0; for(auto &q: p.second) sum += q.second;
        for(auto &q: p.second) v.emplace_back(q.first, q.second / (sum>0? sum:1.0));
        sort(v.begin(), v.end());
        chain_vecs[p.first] = move(v);
    }

    // prepare lengths cumulative vector
    vector<pair<int,double>> lengths_sampling = lengths_vec; // already sorted by key
    double lsum = 0.0; for(auto &p: lengths_sampling) lsum += p.second; for(auto &p: lengths_sampling) p.second /= (lsum>0? lsum:1.0);

    // Generate words
    vector<string> outwords; outwords.reserve(N);
    for(int w=0; w<N; ++w){
        // sample length
        int L = sample_from<int>(lengths_sampling, rng);
        if(L<=0) L = 3;
        if(L==1){ string s = sample_from<string>(single_vec, rng); outwords.push_back(s); continue; }
        // sample initial bigram
        string cur = sample_from<string>(init_vec, rng);
        // ensure cur has length 2; if not, pad using global chars
        while((int)cur.size()<2){ string pick = sample_from<string>(global_char_vec, rng); cur += pick; if((int)cur.size()>2) cur = cur.substr(0,2); }
        // generate until length reached
        while((int)cur.size() < L){
            string bigram = cur.substr(cur.size()-2,2);
            auto it = chain_vecs.find(bigram);
            string next;
            if(it==chain_vecs.end() || it->second.empty()){
                // fallback: pick from global char vec
                next = sample_from<string>(global_char_vec, rng);
            } else {
                next = sample_from<string>(it->second, rng);
                if(next == "$"){
                    // chain suggested end-of-word too early; pick fallback char instead to reach desired length
                    next = sample_from<string>(global_char_vec, rng);
                }
            }
            cur.push_back(next[0]);
        }
        outwords.push_back(cur);
    }

    // output as a single string (space separated)
    for(size_t i=0;i<outwords.size();++i){ if(i) cout<<' '; cout<<outwords[i]; }
    cout<<"\n";
    return 0;
}

// Because the canvas file contains two programs in one C++ file for convenience, we provide a tiny dispatcher when compiled as a single file.
int main(int argc,char**argv){
    string argv0 = argc>0? string(argv[0]) : string();
    if(argv0.find("analyzer")!=string::npos || (argc>=2 && string(argv[1])=="analyze")){
        // naive dispatch to analyzer: re-exec logic by calling the analyzer main above would require refactoring; instead tell user to compile separate files.
        cerr<<"This combined source is for reference. Please compile markov_analyzer.cpp and markov_generator.cpp separately as described in comments.\n";
        return 1;
    }
    // otherwise run generator dispatcher
    return main_gen(argc,argv);
}