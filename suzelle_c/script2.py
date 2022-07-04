
def lignecar(n,ca):
    "cette fonction renvoie la chaine de caractere ca n fois "
    ch = n*ca
    return ch






def surfcercle(R):
    "cette fonction renvoie la surface d'un cercle dont le rayon a ete fourni"
    pi = 3.14
    S = R*R*pi
    return S






def volboite(X1=10,X2=10,X3=10):
    V = X1*X2*X3
    return V





def maximum(n1,n2,n3):
    if(n1>n2 and n1>n3):
        maxi = n1
    elif(n2>n1 and n2>n3):
        maxi = n2
    else:
        maxi = n3
    return maxi






    

def comptecar(ca,ch):
    "renvoie le nombre de fois que l'on rencontre le caractere ca"
    j=0
    for i in ch:
        if(i == ca):
            j = j+1 
    return j


def indexmax(liste):
    "renvoit l'index de l'element ayant le plus grand element de la liste"
    maxi = liste[0]
    index = 0
    for i in liste:
        if maxi < i:
            maxi = i
            index = liste.index(maxi)
##    for i in range(1, len(liste)):
##        if(maxi < liste[i]):
##             maxi = liste[i]
##             index = i
    return index


def nommois(n):
    mois =["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"] 
    for i in mois:
        if(n >= 1 and n <=12):
            nom = mois[n-1]
        else:
            nom = "numero incorrect"
    return nom


    
        
def inverse(ch):
    "inverse l'ordre des caracteres d'une chaine quelconque"
    chaine = ""
    for i in range(len(ch)-1,-1,-1):
        chaine = chaine + ch[i]
    return chaine







def comptemot(ph):
    j = 0
    for i in ph:
        if(i == " "):
            j= j+1
    j = j+1
    return j




def changecar(ch,ca1,ca2,debut=0,fin =None):
    "remplace tous les caracteres ca1,par des caracteres ca2 dans ch a partir de l'indice debut jusqu'a l'indice fin"
    if fin == None:
        fin = len(ch)
    for i in range(debut, fin):
        if (ch[i] == ca1):
            ch = ch[:i] + ca2 + ch [i+1:]
    return ch 



def elemax(liste,debut=0,fin=None):
    "renvoie l'element ayant la plus grande valeur dans la liste transmise,debut et fin etant les indices entre lesquels doit s'exercer la recherche  "
    if fin == None:
        fin = len(liste)
    
    maxi =liste[debut] 
    for i in range(debut,fin):
        if maxi < liste[i]:
            maxi = liste[i]
    return maxi
#liste = [1,3,6,9,4,84,4]
#print("l'element ayant la plus grande valeur de la liste est : {}".format(elemax(liste,0,3)))




def conver(nombre):
    q = 1
    liste1 = []
    chaine = ""
    while q != 0:
        q = nombre//2
        r = nombre%2
        liste1.append(r)
        nombre = q
    for i in range(len(liste1)-1,-1,-1):
        chaine = chaine+str(liste1[i])
    return (chaine)
#liste = input("entrer une liste de nombre separer par des virgules")
#liste =[int(i) for i in liste.split(sep =",")]
#nombre = int(input("entrer le nombre decimal a convertir: "))
# print("({})base10 = {}".format(114,conver(114)))
