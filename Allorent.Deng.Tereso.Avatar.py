import random

class Personnage ():
  def __init__(self, nom, ptsVie, force, taille, poids, categorie, argent):
    self._nom = nom
    self._ptsVie = ptsVie
    self._force = force
    self._taille = taille
    self._poids = poids
    self._categorie = categorie
    self._imc = poids / taille**2
    self._argent = argent
    
  def getPtsVie(self):
    return self._ptsVie
    
  def setPtsVie(self, ptsVie):
    self._ptsVie = int(ptsVie)

  def afficherPtsVie(self):
    print(self.getNom() + " possède", self.getPtsVie(), "point(s) de vie")

  def getNom(self):
    return self._nom

  def setNom(self, nom):
    self._nom = nom
    
  def afficherNom(self):
    print("Cet avatar s'appelle " + self.getNom())

  def getForce (self):
    return self._force

  def setForce(self, force):
    self._force = force
    
  def afficherForce(self):
    print(self.getNom() + " possède " + str(self.getForce()) + " point(s) de force")

  def getTaille (self):
    return self._taille
    
  def afficherTaille(self):
    print(self.getNom() + " mesure " + str(self.getTaille()) + " mètre(s).")

  def getPoids (self):
    return self._poids

  def afficherPoids(self):
    print(self.getNom() + " pèse " + str(self.getPoids()) + " kg.")
    
  def getCategorie (self):
    return self._categorie
  
  def setCategorie (self, categorie):
    self._categorie = categorie
  
  def afficherCategorie(self):
    print(self.getNom() + " est un " + self.getCategorie())
    
  def getImc(self):
    return round(self._imc, 1)

  def getArgent(self):  
    return self._argent
  
  def setArgent(self, argent):
    self._argent = argent
    
  def afficherArgent(self):
      print(self.getNom() + " possède " + str(self.getArgent()) + " pièce(s) d'or")
  
  def afficherImc(self):
    print(self.getNom() + " possède un IMC de " + str(self.getImc()))

  def afficherAvatar (self):
    print("Nom :", self.getNom())
    print("Points de vie :", self.getPtsVie())
    print("Force :", self.getForce())
    print("Taille :", self.getTaille(), "mètre(s)")
    print("Poids :", self.getPoids(), "kilogrammes")
    print("Catégorie :", self.getCategorie())
    print("IMC :", self.getImc())
    print("Argent :", self.getArgent(), "pièces d'or")
  
  def testVie (self):
    return self.getPtsVie() >= 1
    
  def testCat (self, avatar2):
    return self.getCategorie() == avatar2.getCategorie()
  
  def don(self, avatar2, vie) :
    if self.testCat(avatar2) and self.getPtsVie() > vie:
      avatar2.setPtsVie(avatar2.getPtsVie() + vie)
      self.setPtsVie(self.getPtsVie() - vie)
      
  def engendrer(self, avatar2) :
    if self.testCat(avatar2):
        return Personnage(self.getNom() + "-" + avatar2.getNom() , 15 , int(round((self.getForce() + avatar2.getForce()) / 2 * 0.85, 0)), round((self.getTaille() + avatar2.getTaille()) / 2 * 0.85, 2), int(round((self.getPoids() + avatar2.getPoids()) / 2 * 0.85, 0)), self.getCategorie(), 0)
      
  def combat(self, avatar2):
      k = (self.getImc() + self.getForce()) / (avatar2.getImc() + avatar2.getForce())
      if k >= 1 :
          avatar2.setPtsVie(int(round(avatar2.getPtsVie() / k)))
          self.setArgent(self.getArgent() + 25)      # prix du vainqueur
          avatar2.setArgent(avatar2.getArgent() + 5) # lot de consolation
      if k < 1 :
          self.setPtsVie(int(round(self.getPtsVie() * k)))
          avatar2.setArgent(avatar2.getArgent() + 25)
          self.setArgent(self.getArgent() + 5)
    
def afficherNomsAvatars(avatars):
    if len(avatars) == 0:
        print("Il n'y a aucun avatar.\n")
        return
    for i in range(len(avatars)):
        if avatars[i].testVie():
            print("Avatar " + str(i) + " :", avatars[i].getNom())
        else:
            print("Avatar " + str(i) + " (mort) :", avatars[i].getNom())
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
        ligne = input(message + " (d pour lister avec détails, a pour annuler) : ")
        if ligne == "d":
            afficherTousAvatars(avatars)
        elif ligne == "a":
            return None
        else:
            try:
                ret = int(ligne)
                if ret < 0 or ret >= len(avatars):
                    raise ValueError
            except ValueError:
                print("Veuillez entrer d, a ou un nombre entre 0 et " + str(len(avatars)-1) + ".\n")
    return ret
    
def interactionDon(avatars):
    if len(avatars) <= 1:
        print("Il y a strictement moins de deux avatars. Que c'est triste...\n")
        return
    for i in range(len(avatars)):
        print("Avatar " + str(i) + " : " + avatars[i].getNom() + ",", avatars[i].getPtsVie(), "point(s) de vie\n")
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
    if not avatar1.testCat(avatar2):
      print("Les deux avatars ne sont pas de la même catégorie.")
      print(avatar1.getNom() + " est de catégorie " + avatar1.getCategorie())
      print(avatar2.getNom() + " est de catégorie " + avatar2.getCategorie())
      print()
      return
    vie = -1
    while vie <= 0:
        try:
            vie = int(input("Nombre de points de vie : "))
        except ValueError:
            print("Vous n'avez pas entré un nombre...")
            continue
        if vie <= 0:
            print("Nombre de points de vie négatif ou nul...")
    if avatars[iAvatar1].getPtsVie() <= vie:
        print("")
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
    print("")
    afficherNomsAvatars(avatars)
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
        print("")
        print("L'avatar " + str(len(avatars)-1) + " a été engendré :")
        print("----------------\n")
        avatarEngendre.afficherAvatar()
        print("")
    else:
        print("")
        print("Impossible d'engendrer l'avatar.")
        print("Le 1er avatar est de catégorie", avatar1.getCategorie(), "alors que le 2eme est de catégorie", avatar2.getCategorie(),"\n")
        print("----------------")

  
def interactionCombat(avatars):
    if len(avatars) <= 1:
        print("Il y a strictement moins de deux avatars. Que c'est triste...\n")
        return
    for i in range(len(avatars)):
        print("Avatar " + str(i) + " : " + avatars[i].getNom() + ",", avatars[i].getPtsVie(), "point(s) de vie.\n")
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
    print("")
    avatar1.combat(avatar2)
    print("")
    print("Combat effectué.")
    avatar1.afficherPtsVie()
    avatar1.afficherArgent()
    avatar2.afficherPtsVie()
    avatar2.afficherArgent()
    print()
    
def interactionEntrainement(avatar):
    if len(avatar) == 0:
      print("Il n'y a aucun avatar à entraîner.\n")
      return
    try:
      print("L'entraînement coûte 20 pièces d'or et permet d'augmenter sa force de 1 à 10 points.\n")
      for i in range(len(avatar)):
        print("Avatar " + str(i) + " : " + avatar[i].getNom())
      iAvatar = int(input("Numéro de l'avatar à entraîner : "))
      print("")
      if iAvatar < 0 or iAvatar >= len(avatar):
        print("L'avatar ", iAvatar, "n'existe pas.")
        return
      if avatar[iAvatar].getForce() >= 50:
        print ("Cet avatar possède déja la force maximum atteignable.\nEntraîner plus cet avatar reviendrait à le doper, or cela est interdit aux yeux de la loi et passible de lourdes sanctions.")
      else:
        if avatar[iAvatar].getArgent() < 20:
          print("L'avatar ", iAvatar, "n'a pas assez d'argent pour s'entrainer. Il lui manque", 20 - avatar[iAvatar].getArgent(), "pièces d'or.")
        else:
          avatar[iAvatar].setArgent(avatar[iAvatar].getArgent()-20)
          forcesupp = random.randint(1,10)
          avatar[iAvatar].setForce(avatar[iAvatar].getForce() + forcesupp)
          if avatar[iAvatar].getForce() >= 50:
            avatar[iAvatar].setForce(50)  
          print("L'avatar", iAvatar, "s'est bien entraîné !\nIl a gagné", forcesupp, "point(s) de force !")
          avatar[iAvatar].afficherForce()
          avatar[iAvatar].afficherImc()
      print()
    except ValueError:
      print("Vous n'avez pas entré un nombre.")
      
def main():
    print("\n----------------------------------------------------------\n")
    print("Bienvenue dans le mini-projet d'Adrien, Victor et Manon")
    print("\n----------------------------------------------------------\n")
    nbAvatars = int(input("Nombre d'avatars à créer: "))
    print("")
    avatar = []
    for i in range(nbAvatars):
        print("--- Avatar", i, "---")
        nom = input("Nom : ")
        print("Choisir la catégorie :")
        print("1) Humain")
        print("2) Elfe")
        print("3) Gnome")
        print("4) Droïde")
        print("5) Martien")
        choixcat = int(input("Nombre entre 1 et 5 : "))
        if choixcat == 1 :
            categorie = "Humain"
        elif choixcat == 2 :
            categorie = "Elfe"
        elif choixcat == 3 :
            categorie = "Gnome"
        elif choixcat == 4 :
            categorie = "Droïde"
        elif choixcat == 5 :
            categorie = "Martien"
        force = random.randint(1, 50)
        taille = random.randint(100, 200)/100.0
        poids = random.randint(50, 100)
        print("")
        avatar.append(Personnage(nom, 10, force, taille, poids, categorie, 10))
    print("\n\n")
    afficherTousAvatars(avatar)
    
    while True:
        print("Que voulez-vous faire ?")
        print("1) Faire un combat")
        print("2) Faire un don")
        print("3) Engendrer un nouvel avatar")
        print("4) Entraîner un avatar")
        print("5) Lister tous les avatars et leurs détails")
        print("6) Afficher le détail d'un avatar")
        print("7) Quitter")
        choix = input("- ")
        print("")
        if choix == "1":
            interactionCombat(avatar)
        elif choix == "2":
            interactionDon(avatar)
        elif choix == "3":
            interactionEngendrer(avatar)
        elif choix == "4":
            interactionEntrainement(avatar)
        elif choix == "5":
            afficherTousAvatars(avatar)
        elif choix == "6":
            if len(avatar) == 0:
                print("Il n'y a aucun avatar.\n")
                continue
            try:
                for i in range(len(avatar)):
                    print("Avatar " + str(i) + " : " + avatar[i].getNom())
                iAvatar = int(input("Numéro de l'avatar à afficher : \n"))
                if iAvatar < 0 or iAvatar >= len(avatar):
                    print("L'avatar ", iAvatar, "n'existe pas.")
                    continue
                avatar[iAvatar].afficherAvatar()
                print()
            except ValueError:
                print("Vous n'avez pas entré un nombre.")
        elif choix == "7":
            return
        else:
            print("Choix inconnu !")
        

main()
