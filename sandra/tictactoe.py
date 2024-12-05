grille = ["-","-","-",
          "-","-","-",
          "-","-","-"]

joueur_actuel = ""
fin_jeu = False
gagnant = ""


def jouer():
    choix_joueur()   # Appelle la fonction 'choix_joueur()' qui permet de déterminer les joueurs
    affichage_grille()  # Affiche la grille de jeu
    while fin_jeu == False:    # Tant que la variable 'fin_jeu' est fausse (le jeu n'est pas encore terminé)
       tour(joueur_actuel)  # Appelle la fonction 'tour(joueur_actuel)' pour jouer le tour du joueur actuel
       verifier_fin_jeu()   # Appelle la fonction 'verifier_fin_jeu()', qui vérifie si le jeu est terminé (victoire, égalité, etc.)
       joueur_suivant()  # Appelle la fonction 'joueur_suivant()', qui fait passer le tour au joueur suivant
    resultat()  # Une fois que la boucle est terminée (le jeu est fini), on appelle la fonction 'resultat()'
    # Cela pourrait afficher les résultats du jeu (qui a gagné, score final, etc.)
       

def choix_joueur():
    global joueur_actuel   # Déclare la variable 'joueur_actuel' comme une variable globale, permettant ainsi d'accéder à cette variable dans d'autres parties du programme.
    joueur_actuel = input("Veuillez choisir un symbole X ou O : ")
    while True:  # Démarre une boucle infinie (sera arrêtée manuellement si le choix est valide)
     joueur_actuel = joueur_actuel.upper()  # Convertit le choix de l'utilisateur en majuscules (au cas où il entre 'x' ou 'o' en minuscule
     if joueur_actuel == "X":   # Si le joueur choisit 'X', on lui indique son choix et on arrête la boucle
        print("Vous avez choisi X. Votre adversaire aura le O")
        break    # Sortie de la boucle car le choix est valide
     elif joueur_actuel == "O":   # Si le joueur choisit 'O', on lui indique son choix et on arrête la boucle
        print("Vous avez choisi O. Votre adversaire aura le X")
        break    # Sortie de la boucle car le choix est valide
     else:
       joueur_actuel = input("Veuillez choisir un symbole X ou O : ")


# Affichage et design de la grille
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


def verifier_victoire():
    global fin_jeu
    global gagnant
    if grille[0]==grille[1]==grille[2] and grille[2] != "-":  # Si les cases 0, 1 et 2 sont identiques et différentes de "-", la ligne est gagnante le jeu s'arrête
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
    elif grille[2]==grille[5]==grille[8] and grille[8] != "-":
        fin_jeu = True
        gagnant = grille[8]
    elif grille[0]==grille[4]==grille[8] and grille[8] != "-":
        fin_jeu = True
        gagnant = grille[8]
    elif grille[2]==grille[4]==grille[6] and grille[6] != "-":
        fin_jeu = True
        gagnant = grille[6]


def tour(joueur):
   print("C'est le tour du joueur ", joueur)
   pos = input("Choisissez un espace libre sur la grille entre 1 et 9 : ")

   valide = False   # Initialise une variable 'valide' qui servira à contrôler si le choix est valide ou non.
   while valide == False : # La boucle continue tant que 'valide' est égal à False (tant que le joueur n'a pas choisi une case valide).  
      while pos not in ["1","2","3","4","5","6","7","8","9"]: # Si l'entrée n'est pas un nombre entre 1 et 9, on redemande un choix valide.
         pos = input("Choisissez un espace libre sur la grille entre 1 et 9 : ")
      pos = int(pos) - 1 # Convertit la position saisie (qui est une chaîne de caractères) en un entier, puis ajuste l'index (de 1 à 9, donc -1)

      if grille[pos] == "-":# Si la case choisie est vide ("-"), on considère que le choix est valide et on sort de la boucle.
         valide = True
      else:# Si la case est déjà occupée par un autre symbole, on affiche un message d'erreur et on redemande une nouvelle entrée.
         print("Cet emplacement n'est pas disponible")
        
   grille[pos] = joueur   # Une fois le choix valide, on remplace le symbole de la case choisie par celui du joueur.
   affichage_grille()# Affiche la grille après que le joueur ait effectué son mouvement.

 

def verifier_fin_jeu():
   verifier_victoire()
   verifier_match_nul()


def verifier_match_nul():                                        
   global fin_jeu  # Déclare la variable 'fin_jeu' comme étant globale afin de pouvoir la modifier en dehors de la fonction
   if "-" not in grille :  # Vérifie si la grille ne contient plus de cases vides ("-")
      fin_jeu = True   # Le jeu est terminé, on met à jour 'fin_jeu' pour indiquer la fin du jeu

                    

def joueur_suivant():
   global joueur_actuel  # Déclare la variable globale 'joueur_actuel' pour pouvoir la modifier à l'intérieur de la fonction
   if joueur_actuel == "X":  # Si le joueur actuel est "X", on le change pour "O" (le joueur suivant sera "O")
      joueur_actuel = "O"
   else:   # Sinon, si le joueur actuel est "O", on le change pour "X" (le joueur suivant sera "X")
      joueur_actuel = "X"


def resultat():
   if gagnant == "X" or gagnant == "O":  # Vérifie si la variable 'gagnant' est égale à "X" ou "O" (indiquant qu'un joueur a gagné)
      print("Le joueur : ", gagnant, "a gagné")
   else: # Si aucun joueur n'a gagné, on annonce qu'il y a eu un match nul
      print("Match nul.")

 
jouer()

