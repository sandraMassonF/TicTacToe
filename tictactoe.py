grille = ["-","-","-",
          "-","-","-",
          "-","-","-"]

joueur_actuel = ""
fin_jeu = False
gagnant = ""


def jouer():
    choix_joueur()
    affichage_grille()
    while fin_jeu == False:
       tour(joueur_actuel)
       verifier_fin_jeu():

       

def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir un symbole X ou O : ")
    while True:
     joueur_actuel = joueur_actuel.upper()
     if joueur_actuel == "X":
        print("Vous avez choisi X. Votre adversaire aura le O")
        break
     elif joueur_actuel == "O":
        print("Vous avez choisi O. Votre adversaire aura le X")
        break
     else:
       joueur_actuel = input("Veuillez choisir un symbole X ou O : ")

def affichage_grille():
    print("\n")
    print("-------------")
    print("|", grille[0], "|", grille[1], "|", grille[2], "|     | 1 | 2 | 3 |")
    print("-------------")
    print("|", grille[3], "|", grille[4], "|", grille[5], "|     | 4 | 5 | 6 |")
    print("-------------")
    print("|", grille[6], "|", grille[7], "|", grille[8], "|     | 7 | 8 | 9 |")
    print("-------------")
    print("\n")

def tour(joueur):
   print("C'est le tour du joueur ", joueur)
   pos = input("Choisissez un espace libre sur la grille entre 1 et 9 : ")

   valide = False
   while valide == False :
      while pos not in ["1","2","3","4","5","6","7","8","9"]:
         pos = input("Choisissez un espace libre sur la grille entre 1 et 9 : ")
      pos = int(pos) - 1

      if grille[pos] == "-":
         valide = True
      else:
         print("Cet emplacement n'est pas disponible")
        
grille[pos] = joueur
affichage_grille()

def verifier_fin_jeu():
   verifier_victoire()
   verifier_match_nul()

def verifier_victoire():
    global fin_jeu
    global gagnant
    if grille[0]==grille[1]==grille[2] and grille[2] != "-":
       fin_jeu = True
       gagnant = grille[2]
    elif grille[3]==grille[4]==grille[5] and grille[5] != "-":
       fin_jeu = True
       gagnant = grille[5]
    elif grille[6]==grille[7]==grille[8] and grille[8] != "-":
       fin_jeu = True
       gagnant = grille[8]
    elif grille[0]==grille[3]==grille[6] and grille[6] != "-":
        fin_jeu = True
        gagnant = grille[6]
    elif grille[1]==grille[4]==grille[7] and grille[7] != "-":
        fin_jeu = True
        gagnant = grille[7]
    elif grille[3]==grille[5]==grille[8] and grille[8] != "-":
        fin_jeu = True
        gagnant = grille[8]
    elif grille[0]==grille[4]==grille[8] and grille[8] != "-":
        fin_jeu = True
        gagnant = grille[8]
    elif grille[2]==grille[4]==grille[6] and grille[6] != "-":
        fin_jeu = True
        gagnant = grille[6]

def verifier_match_nul():
   global fin_jeu
   if "-" not in grille :
      fin_jeu = True

jouer()

