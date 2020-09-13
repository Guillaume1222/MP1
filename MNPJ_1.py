from math import *
from random import*
#1
rayon=float(input("rayon="))
hauteur=float(input("hauteur="))

def coneDroit (rayon,hauteur):
    resultat=rayon**2*pi*hauteur/3
    return resultat

print(coneDroit(rayon,hauteur))


#2
x=int(randint(1,100))
c=0
s=int(input("choisi un nombre entre 1 et 100:"))
while s!=x :
    if s>x:
        print("trop grand!")
        s=int(input("réessaie! :"))
        c=c+1
    elif s<x:
        print("trop petit!")
        s=int(input("réessaie! :"))
        c=c+1
    else:
        c=c+1
        s=print("Gagner en",c ,"coups!")
        
#3
def etoiles(x)->None:
    for i in range(1, x + 1,2):
        print((i * "*").center(x))
    return
print(etoiles((5)))

#4

x=int(input("votre prix:"))
while x!=0:
    print("prix HT=",x*1.2)
    x=int(input("entrez 0 pour terminer:"))
    
    
#5
def chasse(poule,chien,vache,ami):
    p=poule*1+chien*3+vache*5+ami*10
    print("vous avez",p,"points")
    p=p//100
    pr=p*200
    if pr < 1 :
        print("vous pouvez gardez votre permis")
    else:  
        print("vous devez remboursez",pr , "€")
    
chasse(5,8,0,1)
    
#6
h_p=int(input("poids de Haruhi:"))
h_q=int(input("quantité de nourriture que Haruhi mange par jour:"))
h_rat = h_q / h_p
n=int(input("nombre d’animaux:"))
nombre_a=0

for i in range(n):
    stat_a=input("stat poids et quantité nourriture de l'animal=")
    a_q, a_p = stat_a.split(" ")
    a_rat = int(a_q) / int(a_p)
    a_rat=print()
    if a_rat > h_rat:
        nombre_a = nombre_a+1
        print(nombre_a)