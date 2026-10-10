n=input("Satirni kiriting: ")
lst=[]

belgila={
    ")":"(",
    "]":"[",
    "}":"{"
}

for i in n:
    lst.append(i)
    lst.append(",")

s=("").join(lst)
n=s.split(",")
n.pop(-1)

lamp=True

for i in range(len(n)):
    if n[i]=="(":
        sano=n.count("(")
        sano1=n.count(")")
        if sano1!=sano:
            lamp=False
            break    

    if n[i]=="[":
            sano=n.count("[")
            sano1=n.count("]")
            if sano1!=sano:
                lamp=False
                break

    if n[i]=="{":
            sano=n.count("{")
            sano1=n.count("}")
            if sano1!=sano:
                lamp=False
                break

stack=[]

for i in n:
    if i in "([{":
        stack.append(i)

    elif i in ")]}":
        if not stack or stack[-1] != belgila[i]:
            lamp = False
            break
        stack.pop()
if lamp:
    print("YES")
else:
    print("NO")