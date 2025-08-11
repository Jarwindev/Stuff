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
using namespace std;

static string read_file(const string &path){
    ifstream f(path);
    if(!f) throw runtime_error("Cannot open input file: " + path);
    stringstream ss; ss << f.rdbuf();
    return ss.str();
}

// Very small utility to extract all JSON-quoted strings from a file. Works for our use case (words are simple ASCII).
static vector<string> extract_quoted_strings(const string &s){
    vector<string> out;
    for(size_t i=0;i<s.size();){
        if(s[i]=='\"'){
            ++i; size_t start=i; string cur;
            while(i<s.size()){
                if(s[i]=='\\'){
                    if(i+1<s.size()){ cur.push_back(s[i+1]); i += 2; }
                    else break;
                } else if(s[i]=='\"'){
                    break;
                } else { cur.push_back(s[i]); ++i; }
            }
            out.push_back(cur);
            if(i<s.size() && s[i]=='\"') ++i;
        } else ++i;
    }
    return out;
}

int main(int argc,char**argv){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(argc<3){
        cerr<<"Usage: "<<argv[0]<<" input_words.json model_output.json\n";
        return 1;
    }
    string inpath = argv[1];
    string outpath = argv[2];
    string content;
    try{ content = read_file(inpath); } catch(exception &e){ cerr<<e.what()<<"\n"; return 2; }
    auto words = extract_quoted_strings(content);
    if(words.empty()){ cerr<<"No quoted strings (words) found in input file. Expected a JSON with quoted words.\n"; return 3; }

    unordered_map<int,long long> len_count;
    unordered_map<string,long long> initial_bigram_count;
    unordered_map<char,long long> single_char_count;
    unordered_map<string, unordered_map<string,long long>> chains; // bigram -> (next char or "$") -> count
    unordered_map<char,long long> global_next_char_count;

    for(auto &w: words){
        if(w.empty()) continue;
        int L = (int)w.size();
        len_count[L]++;
        if(L==1){ single_char_count[w[0]]++; }
        if(L>=2){
            string first2 = w.substr(0,2);
            initial_bigram_count[first2]++;
            // for positions 0..L-3, bigram -> next char
            for(int i=0;i<=L-3;i++){
                string bigram = w.substr(i,2);
                string nextch(1,w[i+2]);
                chains[bigram][nextch]++;
                global_next_char_count[w[i+2]]++;
            }
            // bigram at last two letters -> end token
            string lastbig = w.substr(max(0,L-2),2);
            chains[lastbig]["$"]++;
        } else if(L==1){
            // single-letter word: it doesn't contribute bigrams, but we still could add an initial bigram made from char + '$'
            string bigram;
            bigram.push_back(w[0]); bigram.push_back('$');
            initial_bigram_count[bigram]++;
            chains[bigram]["$"]++;
        }
    }

    // compute totals and normalize to probabilities (we'll output as decimals)
    auto normalize_map = [&](auto &mcounts){
        // returns vector<pair<string,double>> sorted by key for stable output
        double total = 0.0;
        for(auto &p: mcounts) total += (double)p.second;
        vector<pair<string,double>> vec;
        for(auto &p: mcounts){ vec.emplace_back(p.first, (total>0? (double)p.second/total : 0.0)); }
        sort(vec.begin(), vec.end());
        return vec;
    };

    // lengths map: keys are integers -> convert to strings for JSON
    unordered_map<string,double> lengths_probs;
    double total_len = 0.0; for(auto &p: len_count) total_len += (double)p.second;
    for(auto &p: len_count){ lengths_probs[to_string(p.first)] = (total_len>0 ? (double)p.second/total_len : 0.0); }

    // single char probs
    unordered_map<string,double> single_probs;
    double total_single = 0.0; for(auto &p: single_char_count) total_single += (double)p.second;
    for(auto &p: single_char_count) single_probs[string(1,p.first)] = (total_single>0 ? (double)p.second/total_single : 0.0);

    // initial bigrams
    auto initvec = normalize_map(initial_bigram_count);

    // chains: for each bigram, normalize inner map
    unordered_map<string, vector<pair<string,double>>> chains_probs;
    for(auto &outer: chains){
        double tot=0.0; for(auto &q: outer.second) tot += (double)q.second;
        vector<pair<string,double>> inner; inner.reserve(outer.second.size());
        for(auto &q: outer.second){ inner.emplace_back(q.first, (tot>0 ? (double)q.second/tot : 0.0)); }
        sort(inner.begin(), inner.end());
        chains_probs[outer.first] = move(inner);
    }

    // produce JSON model
    ofstream out(outpath);
    if(!out){ cerr<<"Cannot open output file for write: "<<outpath<<"\n"; return 4; }
    out<<"{\n";
    // lengths
    out<<"  \"lengths\": {\n";
    bool first=true;
    vector<pair<string,double>> len_pairs;
    for(auto &p:lengths_probs) len_pairs.emplace_back(p.first,p.second);
    sort(len_pairs.begin(), len_pairs.end(), [](auto &a, auto &b){ return stoi(a.first) < stoi(b.first); });
    for(auto &p: len_pairs){ if(!first) out<<",\n"; first=false; out<<"    \""<<p.first<<"\": "<<setprecision(9)<<p.second; }
    out<<"\n  },\n";

    // single_chars
    out<<"  \"single_chars\": {\n";
    first=true;
    vector<pair<string,double>> scp;
    for(auto &p: single_probs) scp.emplace_back(p.first,p.second);
    sort(scp.begin(), scp.end());
    for(auto &p: scp){ if(!first) out<<",\n"; first=false; out<<"    \""<<p.first<<"\": "<<setprecision(9)<<p.second; }
    out<<"\n  },\n";

    // initial_bigrams
    out<<"  \"initial_bigrams\": {\n";
    first=true;
    for(auto &p: initvec){ if(!first) out<<",\n"; first=false; out<<"    \""<<p.first<<"\": "<<setprecision(9)<<p.second; }
    out<<"\n  },\n";

    // chains
    out<<"  \"chains\": {\n";
    first=true;
    vector<string> keys; keys.reserve(chains_probs.size()); for(auto &p: chains_probs) keys.push_back(p.first); sort(keys.begin(), keys.end());
    for(auto &k: keys){ if(!first) out<<",\n"; first=false; out<<"    \""<<k<<"\": {\n";
        auto &inners = chains_probs[k];
        bool first2=true;
        for(auto &q: inners){ if(!first2) out<<",\n"; first2=false; out<<"      \""<<q.first<<"\": "<<setprecision(9)<<q.second; }
        out<<"\n    }";
    }
    out<<"\n  }\n";
    out<<"}\n";
    out.close();
    cout<<"Model written to: "<<outpath<<" (contains lengths, single_chars, initial_bigrams, chains)\n";
    return 0;
}