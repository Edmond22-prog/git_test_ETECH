def multiplication():
    a = int(input("Entrer un nombre : "))
    for i in range(11):
        b = a*i
        print("{} * {} = {}".format(a,i,b))


def détermination():
    "vérifie si une chaine de caractère contient ou pas le caractère <<e>>"
    a = (input("Entrer un mot : "))
    if "e" in a:
        print("le mot écrit contient le caractère <<e>>")
    elif "e" not in a:  
        print("le mot écrit ne contient pas le caractère <<e>>")


def nombre_d_occurence():
    "le nombre d'occurence d'un caractère dans une expression"
    a = input("Entrer un mot : ")
    list(a)
    while("e" in a):
        print("Le nombre de caractère dans l'expression est de {} ".format())


