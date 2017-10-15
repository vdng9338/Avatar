import random

class Personnage:
    def __init__(self, nom, ptsVie, force, taille, poids, categorie):
        self._nom = nom
        self._ptsVie = ptsVie
        self._force = force
        self._taille = taille
        self._poids = poids
        self._categorie = categorie


  
def afficherNomsAvatars(avatars):
    for i in range(len(avatars)):
        if avatars[i].testVie():
            print("Avatar" + i + ":", avatars[i].getNom())
        else:
            print("Avatar" + i + " (mort) :", avatars[i].getNom())
    print()

def afficherTousAvatars(avatars):
    for i in range(len(avatars)):
        print("--- Avatar", i, "---")
        avatars[i].afficherAvatar()
        print()

def demandeAvatar(avatars, message):
    ret = -1
    while ret < 0 or ret >= len(avatars):
        ligne = input(message + " (l pour lister, d pour lister avec détails) : ")
        if ligne == "l":
            afficherNomsAvatars(avatars)
        elif ligne == "d":
            afficherTousAvatars(avatars)
        else:
            try:
                ret = int(ligne)
                if ret < 0 or ret >= len(avatars):
                    raise ValueError
            except ValueError:
                print("Veuillez entrer l, d ou un nombre entre 0 et " + str(len(avatars)-1) + ".")
    return ret
    
# Peut-on ressusciter un avatar ?
def interactionDon(avatars):
    iAvatar1 = demandeAvatar(avatars, "Numéro de l'avatar qui donne")
    avatar1 = avatars[iAvatar1]
    iAvatar2 = demandeAvatar(avatars, "Numéro de l'avatar qui recoit")
    avatar2 = avatars[iAvatar2]
    vie = int(input("Nombre de points de vie : "))
    if avatars[iAvatar1].getPtsVie() <= vie:
        print("L'avatar", avatar1.getNom(), "n'a que", avatar1.getPtsVie(), "point(s) de vie. Don impossible.")
    else:
        avatar1.don(avatar2, vie)
        print("Don effectué.")
        avatar1.afficherPtsVie()
        avatar2.afficherPtsVie()
        
def interactionEngendrer(avatars):
    iAvatar1 = demandeAvatar(avatars, "Numéro de l'avatar 1")
    avatar1 = avatars[iAvatar1]
    if not avatar1.testVie():
        print("L'avatar", avatar1.getNom(), "est mort.")
        return
    iAvatar2 = demandeAvatar(avatars, "Numéro de l'avatar 2")
    if iAvatar1 == iAvatar2:
        print("Il faut deux avatars différents pour en engendrer un nouveau.")
        return
    avatar2 = avatars[iAvatar2]
    if not avatar2.testVie():
        print("L'avatar", avatar2.getNom(), "est mort.")
        return
    if avatar1.testCat(avatar2):
        avatarEngendre = avatar1.engendrer(avatar2)
        avatars.append(avatarEngendre)
        print("L'avatar suivant (n." + len(avatars)-1 + ") a été engendré :")
        avatarEngendre.afficherAvatar()
    else:
        print("Impossible d'engendrer l'avatar.")
        print("Le 1er avatar est de catégorie", avatar1.getCategorie(), "alors que le 2e est de catégorie", avatar2.getCategorie())
  
def interactionCombat(avatars):
    iAvatar1 = demandeAvatar(avatars, "Numéro de l'avatar 1")
    avatar1 = avatars[iAvatar1]
    if not avatar1.testVie():
        print("L'avatar", avatar1.getNom(), "est mort.")
        return
    iAvatar2 = demandeAvatar(avatars, "Numéro de l'avatar 2")
    if iAvatar1 == iAvatar2:
        print("Un avatar ne peut se battre contre lui-même !")
        return
    avatar2 = avatars[iAvatar2]
    if not avatar2.testVie():
        print("L'avatar", avatar2.getNom(), "est mort.")
        return
    avatar1.combat(avatar2)
    print("Combat effectué.")
    avatar1.afficherPtsVie()
    avatar2.afficherPtsVie()

def main():
    nbAvatars = int(input("Nombre d'avatars : "))
    avatar = []
    for i in range(nbAvatars):
        print("--- Avatar", i, "---")
        nom = input("Nom : ")
        categorie = input("Catégorie : ")
        force = random.randint(1, 50)
        taille = random.randint(100, 200)/100.0
        poids = random.randint(50, 100)
        avatar.append(Personnage(nom, 10, force, taille, poids, categorie))
    while True:
        print("Que voulez-vous faire ?")
        print("1) Faire un combat")
        print("2) Faire un don")
        print("3) Engendrer un nouvel avatar")
        print("4) Lister tous les avatars et leurs détails")
        print("5) Afficher le détail d'un avatar")
        print("6) Quitter")
        choix = input()
        if choix == "1":
            interactionCombat(avatars)
        elif choix == "2":
            interactionDon(avatars)
        elif choix == "3":
            interactionEngendrer(avatars)
          elif choix == "4":
              afficherTousAvatars()
        elif choix == "5":
            try:
                iAvatar = int(input("Quel avatar ? "))
                if iAvatar < 0 or iAvatar >= len(avatars):
                    print("L'avatar n.", iAvatar, "n'existe pas.")
                avatars[iAvatar].afficherAvatar()
                print()
            except ValueError:
                print("Vous n'avez pas entré un nombre.")
        elif choix == "6":
            return
        else:
            print("Choix inconnu !")

main()
