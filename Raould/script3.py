a = input("Entrer une expression : ")
b = input("Entrer une autre expression : ")
if a>b:
    print("Selon l'ordre lexicographique le mot {} vient avant le mot {}".format(b,a))
else:
    print("Selon l'ordre lexicographique le mot {} vient avant le mot {}".format(a,b))
if a == b:
    print("les deux expressions sont égales")
