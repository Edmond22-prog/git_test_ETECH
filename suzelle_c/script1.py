liste1 = []
liste = []
all = []
choix = "oui"
while(choix in ["oui","o","OUI","O"] ) :
    matricule = input("entrer le matricule de l'etudiant :")
    liste.append(matricule)
    nom = input("entrer le nom de l'etudiant :")
    liste.append(nom)
    prenom = input("entrer le prenom de l'etudiant:")
    liste.append(prenom)
    age = input("entrer l'age de l'etudiant :")

    while 1:
            try:
                age = int(age)
            except:
                print("vous avez entree un texte, entrer un age valide!")
            else:
                if(age in range(16,31)):
                    print("cet etudiant a {} ans".format(age))
                    liste.append(age)
                    break
                else:
                    print("entrer a nouveau l'age mais compris entre 16 et 30 !")
            age = input("entrer l'age de l'etudiant :")
    for i in range(1,11):
            note =input("entrer la note {} de l'etudiant : ".format(i))
            while 1:
                try:
                    note =float(note)
                except:
                    print("vous avez entree un texte, entrer une note valide!")
                else:
                    if(note in range(0,21)):
                        print("cet etudiant a comme note {} : {}".format(i, note))
                        liste1.append(note)             
                        print(liste1)
                        break
                    else:
                        print("entrer une note comprise entre 0 et 20!")
                note =input("entrer la note {} de l'etudiant : ".format(i))
    liste.append(liste1)
    print(liste)
    all.append(liste)
    liste = []
    liste1 = []
    choix = input("voulez vous enregistrer un autre etudiant : ")
for liste in all:
    print(liste)





    
# print(matricule, nom, prenom, age, note)
    

# try:    
#     for i in range(10):
#         note = float(input("entrer la note {} de l'etudiant :".format(i+1)))
#         liste1.append(note)
# except:
#     print("desolez mais vous avez entree un texte,entrer une note valide")
# else:
#     print(liste1)1

            
            
        



