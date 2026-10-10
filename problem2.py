n=int(input("Uylar sonini kiriting: "))
lst=list(map(int,input("Har bir uydagi pullarni kiriting: ").split()))

juft=[]
toq=[]

for i in range(n):
    if i%2:
        toq.append(lst[i])
    else:
        juft.append(lst[i])

if sum(juft)>sum(toq):
    print(sum(juft))
else:
    print(sum(toq))