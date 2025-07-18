print("Mata in en matris rad för rad." \
" Avsluta med en tom rad.")
m=[]
while True:
    s=input("? ")
    if s == "":
        break
    ls = s.split(",")
    rad = [float(x) for x in ls]
    m.append(rad)
