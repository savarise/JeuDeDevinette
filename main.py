import random #on doit import random pour pouvoir declarer ses fonctions
x = random.randint(0, 100)
essai = -1 #il faut se souvenir de ne pas mettre essai a 0 quand on le declare sinon si lordinateur choisi 0 comme x, on va instatanement gagner
nb_essai = 0

def QuiterOuRejouer(): #cette fonction est pour lorsque lessai est le bon nombre
    global nb_essai #ceci fait que quand on declare la variable nb_essai, ca modifie cette variable hors de la fonction
    print("Bravo! Bonne reponse \n Vous avez reussi en: " + str(nb_essai) + " essai(s)")
    quit = str(input("Voulez-vous faire une autre partie (o/n)?"))
    if quit == "n":

        print("Merci et au revoir...")
        exit()
    else:
        nb_essai = 0
        global x
        x = random.randint(0, 100)
        questioner() #donc si on ne quitte pas, ca recommence le procesus du jeu

def essayer(): #cette fonction est pour chaque mauvais essai
    essai = int(input())

    global nb_essai
    nb_essai += 1 # puisque ++ ne fonctionne pas en python, on doit utiliser +=
    if essai < x:
        print("x>essai")
    elif essai > x:
        print("x<essai")
    else:
        QuiterOuRejouer()

def questioner(): #cette fonction demarre le jeu
    print(str(x))
    print("J'ai choisi un nombre aléatoire entre 0 et 100, essaye de le deviner")
    while x != essai: #ceci va laisser lutilisateur reesayer de deviner chaque essai
        essayer()
questioner()
