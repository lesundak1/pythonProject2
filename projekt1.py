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
delic='-'*62

username = input('username: ')
password = input('password: ')

print(delic)
if data.get(username) == password:
    print('Hello ' + username + ', welcome to the app.')

else:
    print('Password or username is not correct! The app quits.')
    exit()
print(delic)
print('We have 3 texts to be analyzed.')

nt=input('Choose between the tree texts, enter a number btw. 1 and 3 : ')
if nt.isnumeric():
    if int(nt) < 1 or int(nt) > 3:
        print("Chosen number is out of range. The app quits.")
        exit()
    else:
        index = int(nt) - 1
        text = TEXTS[index]
else:
    print('Chosen number is not a number. The app quits.')
    exit()

# print(f"Chosen text: {text}")
print(delic)

slova=text.split(" ")

print(f"Therea are {len(slova)} words in the selected text.")

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

print(f"There are {i} uppercase words.")
print(f"There are {j} titlecase words.")
print(f"There are {k} lowercase words.")
print(f"iThere are {l} numeric strings.")
print(f"The sum of all the numbers is {n}.")
velkadelka=max(delkaslov.values())
print(delic)
print("LEN|"+ " "*math.floor(velkadelka/2-5)+"OCCURENCES" + " "*math.ceil(velkadelka/2-5) + "|NR.")
print(delic)


for p, r in sorted(delkaslov.items()):
    if p <10:
        print("", p , "|"+"*"*r+ " "*(velkadelka-r) +"|",r )
    else:
        print(p, "|" + "*" * r + " " * (velkadelka - r) + "|", r)
print(delic)
