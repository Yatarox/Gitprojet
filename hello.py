
recommencer = False

while not recommencer:
    nombre = int(input("Donne un nombre : "))
    print(nombre)

    for i in range(11):
        print(nombre * i)

    choix = input("Veux-tu recommencer? (Oui/Non) ").lower()

    if choix == "oui":
        recommencer = False
    elif choix == "non":
        recommencer = True
        print("C'est fini")
    else:
        print("Choix non valide. On recommence.")
