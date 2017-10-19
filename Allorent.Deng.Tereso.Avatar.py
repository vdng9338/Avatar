import random

class Personnage ():
  def __init__(self, nom, ptsVie, force, taille, poids, categorie):
    self._nom = nom
    self._ptsVie = ptsVie
    self._force = force
    self._taille = taille
    self._poids = poids
    self._categorie = categorie
    
  def getPtsVie(self):
    return ptsVie
    
  def setPtsVie(self, ptsVie):
    self._ptsVie = ptsVie

  def afficherPtsVie(self):
    print("Points de vie de " + self.getNom() + " :", ptsVie)

  def getNom(self):
    return nom

  def setNom(self, nom):
    self._nom = nom

  def getForce (self):
    return force

  def setForce(self):
		self._force = force
    ## if force < 1 or > 50:
    ## print ("La valeur choisie est impossible.")
    ##  force = int(input("entrez une nouvelle valeur comrise entre 1 et 50: ", force2))

  def getTaille (self):
    return taille

  def setTaille (self):
    self._taille = taille
    ##while taille < 1,00 or taille > 2.00:
    ##  print ("La valeur choisie est impossible.")
    ##  taille = float(input("entrez la nouvelle taille (entre 1 et 2 mètres): ", taille2))

  def getPoids (self):
    return poids
    
  def setPoids (self):
  	self._poids = poids
    ##while poids < 50 or poids > 100:
    ##  print ("La valeur choisie est impossible.")
    ##  poids = int(input("entrez le nouveau poids (entre 50 et 100 kg): ", poids2))
      
  def getCategorie (self):
    return categorie
  
  def setCategorie (self):
  	self._categorie = categorie
  
  def afficherAvatar (self):
    print ("caractéristiques de l'avatar:")
    print("Nom: ", self.getNom())
    print("Points de Vie: ", self.getPtsVie())
    print("Force: ", self.getForce())
    print("Taille: ", self.getTaille(), " mètre(s)")
    print("Poids: ", poids, " kilogrammes")
    print("Catégorie: ", categorie)
  
  
  
  def testVie (self):
    return self.getPtsVie() >= 1
    
  def testCat (self, avatar2):
    return self.getCategorie() == avatar2.getCategorie()
    
    
  def imc(self):
      self._imc = self._poids / self._taille**2
  
  def don(self, avatar2, vie) :
    if self.testCat(avatar2) and self.getPtsVie() > avatar2.getPtsVie():
      avatar2.setPtsVie(avatar2.getPtsVie() + vie)
      self.setPtsVie(self.getPtsVie() - vie)
  
  def engendrer(self, avatar2) :
      if testCat(avatar2):
          Personnage(self._nom + "-" + avatar2._nom , int((self.getPtsVie + avatar2.getPtsVie)*100 - (self.getPtsVie + avatar2.getPtsVie)*15) , int((self.getForce + avatar2.getForce)*100 - (self.getForce + avatar2.getForce)*15), 145 , 60 , humain)
      
  def combat(self, avatar2):
      k = (self._imc + self._force) / (avatar2.imc() + avatar2.getForce())
      
      if k >= 1 :
          avatar2.setPtsVie(avatar2.getPtsVie() / K)
          
      if k < 1 :
          self.setPtsVie(self.getPtsVie() * K)
    
    
    
    #QUestion: Peut-on remplacer le terme "catégorie" par "race" (dans le programme, pas dans les variables)?
    
def afficherNomsAvatars(avatars):
    if len(avatars) == 0:
        print("Il n'y a aucun avatar.\n")
        return
    for i in range(len(avatars)):
        if avatars[i].testVie():
            print("Avatar " + i + " :", avatars[i].getNom())
        else:
            print("Avatar " + i + " (mort) :", avatars[i].getNom())
    print()

def afficherTousAvatars(avatars):
    if len(avatars) == 0:
        print("Il n'y a aucun avatar.\n")
        return
    for i in range(len(avatars)):
        print("--- Avatar", i, "---")
        avatars[i].afficherAvatar()
        print()

def demandeAvatar(avatars, message):
    if len(avatars) == 0:
        print("Il n'y a aucun avatar.\n")
        return None
    ret = -1
    while ret < 0 or ret >= len(avatars):
        ligne = input(message + " (l pour lister, d pour lister avec détails, a pour annuler) : ")
        if ligne == "l":
            afficherNomsAvatars(avatars)
        elif ligne == "d":
            afficherTousAvatars(avatars)
        elif ligne == "a":
            return None
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
    if len(avatars) <= 1:
        print("Il y a strictement moins de deux avatars. Que c'est triste...\n")
        return
    iAvatar1 = demandeAvatar(avatars, "Numéro de l'avatar qui donne")
    if iAvatar1 == None:
        return
    avatar1 = avatars[iAvatar1]
    iAvatar2 = demandeAvatar(avatars, "Numéro de l'avatar qui recoit")
    if iAvatar2 == None:
        return
    if iAvatar1 == iAvatar2:
        print("Un avatar ne peut se donner des points de vie à soi-même.\n")
        return
    avatar2 = avatars[iAvatar2]
    vie = -1
    while vie <= 0:
        try:
            vie = int(input("Nombre de points de vie : "))
        except ValueError:
            print("Vous n'avez pas entré un nombre...")
        if vie <= 0:
            print("Nombre de points de vie négatif ou nul...")
    if avatars[iAvatar1].getPtsVie() <= vie:
        print("L'avatar", avatar1.getNom(), "n'a que", avatar1.getPtsVie(), "point(s) de vie. Don impossible.\n")
    else:
        avatar1.don(avatar2, vie)
        print("Don effectué.")
        avatar1.afficherPtsVie()
        avatar2.afficherPtsVie()
        print()
        
def interactionEngendrer(avatars):
    if len(avatars) <= 1:
        print("Il y a strictement moins de deux avatars. Que c'est triste...\n")
        return
    iAvatar1 = demandeAvatar(avatars, "Numéro de l'avatar 1")
    if iAvatar1 == None:
        return
    avatar1 = avatars[iAvatar1]
    if not avatar1.testVie():
        print("L'avatar", avatar1.getNom(), "est mort.")
        return
    iAvatar2 = demandeAvatar(avatars, "Numéro de l'avatar 2")
    if iAvatar1 == iAvatar2:
        print("Il faut deux avatars différents pour en engendrer un nouveau.")
        return
    if iAvatar2 == None:
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
    if len(avatars) <= 1:
        print("Il y a strictement moins de deux avatars. Que c'est triste...\n")
        return
    iAvatar1 = demandeAvatar(avatars, "Numéro de l'avatar 1")
    if iAvatar1 == None:
        return
    avatar1 = avatars[iAvatar1]
    if not avatar1.testVie():
        print("L'avatar", avatar1.getNom(), "est mort.\n")
        return
    iAvatar2 = demandeAvatar(avatars, "Numéro de l'avatar 2")
    if iAvatar1 == iAvatar2:
        print("Un avatar ne peut se battre contre lui-même !\n")
        return
    if iAvatar2 == None:
        return
    avatar2 = avatars[iAvatar2]
    if not avatar2.testVie():
        print("L'avatar", avatar2.getNom(), "est mort.\n")
        return
    avatar1.combat(avatar2)
    print("Combat effectué.")
    avatar1.afficherPtsVie()
    avatar2.afficherPtsVie()
    print()

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
            interactionCombat(avatar)
        elif choix == "2":
            interactionDon(avatar)
        elif choix == "3":
            interactionEngendrer(avatar)
        elif choix == "4":
            afficherTousAvatars(avatar)
        elif choix == "5":
            if len(avatar) == 0:
                print("Il n'y a aucun avatar.\n")
                continue
            try:
                iAvatar = int(input("Quel avatar ? (entre 0 et " + str(len(avatar)-1) + ") "))
                if iAvatar < 0 or iAvatar >= len(avatar):
                    print("L'avatar n.", iAvatar, "n'existe pas.")
                    continue
                avatar[iAvatar].afficherAvatar()
                print()
            except ValueError:
                print("Vous n'avez pas entré un nombre.")
        elif choix == "6":
            return
        else:
            print("Choix inconnu !")

main()
