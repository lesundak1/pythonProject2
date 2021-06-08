import math
data = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
delic='-'*40

username = input('Uživatelské jméno: ')
password = input('Heslo: ')

print('-'*20)
if data.get(username) == password:
    print('Nazdar ' + username)

else:
    print('Heslo, nebo uživatelské jméno je špatně!')
    exit()
print(delic)
print('mame pre teba 3 texty na analyzu')

print('-'*20)

nt=input('Choose between texts 1, 2 or 3 : ')
if nt.isnumeric():
    if int(nt) < 1 or int(nt) > 3:
        print("Vami vybrane cislo neni v nabidce, ukoncuji")
        exit()
    else:
        index = int(nt) - 1
        text = TEXTS[index]
else:
    print('Nezadali ste cislo,konec!')
    exit()

# print(f"Chosen text: {text}")
print(delic)

slova=text.split(" ")

print(f"Pocet slov v textu {nt} je {len(slova)} .")

vycistena_slova = [slovo.strip(".,?,'\n' ") for slovo in slova]
# print(slova)
# print(vycistena_slova)
i=0
j=0
k=0
l=0
n=0
delkaslov={}

for v in vycistena_slova:
    if v[0].isupper():
        j=1+j
    elif v.isupper():
        i= 1+i
    elif v.islower():
        k=1+k
    elif v.isnumeric():
        n=int(v)+n
        l=1+l
    delkaslov[len(v)]=delkaslov.get(len(v),0)+1
# print(delkaslov)

# print(sorted(delkaslov.items()))

print(f" Pocetu upper slov {i}")
print(f"Starts with upper {j}")
print(f"is lower {k}")
print(f"is numeric {l}")
print(f"is suma {n}")
velkadelka=max(delkaslov.values())
print(delic)
print("LEN|"+ " "*math.floor(velkadelka/2-5)+"OCCURENCES" + " "*math.ceil(velkadelka/2-5) + "|NR.")
print(delic)


for p, r in sorted(delkaslov.items()):
    if p <10:
        print("", p , "|"+"*"*r+ " "*(velkadelka-r) +"|",r )
    else:
        print(p, "|" + "*" * r + " " * (velkadelka - r) + "|", r)

