import cv2
import string
import os

d={}
c={}

for i in range (255):
    d[chr(i)]=i
    c[i]=chr(i)


#print(c)

slika=input("Unesite naziv slike u kojој zelite da podaci budu sakriveni: ")
x=cv2.imread(slika) 

i=x.shape[0]    
j=x.shape[1]    
print(i,j)

key=input("Uneti sigurnosni kljuc: ")
text=input("Uneti tekst koji zelite da bude sakriven: ")

kl=0
tln=len(text)
z=0 
n=0 
m=0 

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]  
    n=n+1
    m=m+1
    m=(m+1)%3
    #n=(n+1)%3      #horizontalno
    #z=(z+1)%3      #dijagonalno
    kl=(kl+1)%len(key)




nova_slika=input("Unesite kako zelite da se zove nova slika u kojoj ce biti skriveni podaci: ")
cv2.imwrite(nova_slika,x)  
os.startfile(nova_slika)   
print("\nSakrivanje podatka uspesno izvrseno")


kl=0
tln=len(text)
z=0 
n=0 
m=0 

ch=int(input("\nUneti 1 za izvlacenje podataka iz slike: "))

if ch == 1:
    key1=input("\nUneti kljuc: ")
    decrypt=""

    if key == key1:
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[kl]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            kl=(kl+1)%len(key)
        print("\nEnkriptovana poruka je bila: ",decrypt)
    else:
        print("\nKljuc nije ispravan")
else:
    print("Kraj")
