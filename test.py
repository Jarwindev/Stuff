x = "Python"[1]
print(x)

s="MattE"

s=s.upper()
print(s)
a="3"
b="12"
print(3*b+a)
print(b.replace("1","3"))
for letter in s:
    if letter=="M":
        break
    print(letter, ", ")
numbers=[5,10]
furniture=["Chairs","Tables"]
for x in numbers:
    for y in furniture:
        print(x,y)

g=["Hi ","Bye "]
print(min(g), max(g))
name=["Ann","Karl"]
List=[x+y for x in g for y in name]
print(List)
myTuple=(1,2,3,4,5,6,7,8)
print(myTuple) 
print(myTuple[2:5],myTuple[:4],myTuple[3:])