# Birinchi qatordegi input faqat alifbo bo'ganiga, ham har doiim bir xil bo'ganiga unga input qo'ymadim



n=input("satrni kiriting: ")
n=n.upper()

dct={
    "A":"AA",
    "B":"AD",
    "C":"AF",
    "D":"AG",
    "E":"AX",
    "F":"DA",
    "G":"DD",
    "H":"DF",
    "I":"DG",
    "J":"DG",
    "K":"DX",
    "L":"FA",
    "M":"FD",
    "N":"FF",
    "O":"FG",
    "P":"FX",
    "Q":"GA",
    "R":"GD",
    "S":"GF",
    "T":"GG",
    "U":"GX",
    "V":"XA",
    "W":"XD",
    "X":"XF",
    "Y":"XG",
    "Z":"XX"
}

natija=[]

for i in n:
    for j,x in dct.items():
        if i==j:
            s=x
    natija.append(s)

natija=("").join(natija)

print(natija)