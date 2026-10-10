n=int(input("Nehta son kiritasiz: "))
lst=list(map(int,input("Sonlarni kiritng: ").split()))

dct={}

for i in lst:
    dct[i]=dct.get(i,0)+1

natija=max(dct.values())

lstt=[i for i, j in dct.items() if j==natija]

javob=min(lstt)

print(javob)