import random

essai = -1
nb_essai = 0
borne_minimale = 0
borne_maximale = 0

# cette fonction est pour lorsque lessai est le bon nombre, ELLE VA SOIT QUITTER LE JEU OU REJOUER
def QuiterOuRejouer():
    global nb_essai
    print("Bravo! Bonne reponse \n Vous avez reussi en: " + str(nb_essai) + " essai(s)")
    quit = str(input("Voulez-vous faire une autre partie (o/n)?"))
    if quit == "n":

        print("Merci et au revoir...")
        exit()
    else:
        nb_essai = 0
        global x
        questioner()

# cette fonction est pour la gestion de chaque essai
def essayer():
    essai = int(input())

    global nb_essai
    nb_essai += 1
    if essai < x:
        print("x>essai")
    elif essai > x:
        print("x<essai")
    else:
        QuiterOuRejouer()

# cette fonction choisis les bornes du jeu
def bornes():
    bornes = str(input("Voulez-vous choisir les bornes (o/n)?"))
    if bornes == "o":
        global borne_minimale
        global borne_maximale
        borne_minimale = int(input("Choisis une borne minimale"))
        borne_maximale = int(input("Choisis une borne maximale"))
    else:
        borne_minimale = 0
        borne_maximale = 100

# cette fonction demarre le jeu et te laisse reessayer jusqua tu gagnes
def questioner():
    bornes()
    global x
    x = random.randint(borne_minimale, borne_maximale)
    print("J'ai choisi un nombre aléatoire entre " + str(borne_minimale) + " et " + str(
        borne_maximale) + ", essaye de le deviner")
    while x != essai:
        essayer()

questioner()
