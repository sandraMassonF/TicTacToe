from random import *

numero_1 = 0
numero_2 = 0

# Défini l'action de l'IA
def ia_actions():    
    numero_1 = randint(1, 3)
    numero_2 = randint(1, 3)
    # * ligne 1
    if numero_1 == 1 and numero_2 == 1:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    elif numero_1 == 1 and numero_2 == 2:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    elif numero_1 == 1 and numero_2 == 3:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    # * ligne 2
    elif numero_1 == 2 and numero_2 == 1:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    elif numero_1 == 2 and numero_2 == 2:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    elif numero_1 == 2 and numero_2 == 3:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    # * ligne 3
    elif numero_1 == 3 and numero_2 == 1:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    elif numero_1 == 3 and numero_2 == 2:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    elif numero_1 == 3 and numero_2 == 3:
        if ligne1[numero_2 - 1] == "_":
            ligne1[numero_2 - 1] = symbole
        else:
            return ia_actions()
    # Imprime le rendu du tableau au fur a mesure des actions des joueurs
    print()
    print("L'IA a joué ")
    print()
    print("|".join(ligne1))
    print("|".join(ligne2))
    print("|".join(ligne3))
    print()

# Changement de joueur avec IA
def changement_ia():
    global tour
    global joueur_1
    global joueur_2
    global symbole
    tour = 1
    while verifie() != True and tour <= 10:
        if tour % 2 == 1:
            symbole = joueur_1
            print("Joueur 1, c'est à ton tour de jouer!")
            actions()
        else:
            symbole = joueur_2
            ia_actions()
        tour += 1
    relancer_partie()

# Lancement de l'IA 
def lancement_ia():
    print()
    print("Vous jouez desormais contre une IA")
    print("Bonne chance!")
    print()
    changement_ia()

#################################################

# joueurs
joueur_1= "X"
joueur_2= "O"
symbole = ""

# tableau
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
ligne1 = board[0]
ligne2 = board[1]
ligne3 = board[2]

# Efface le tableau d'une partie terminée
def efface():
    global ligne1
    global ligne2
    global ligne3
    global board
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    ligne1 = board[0]
    ligne2 = board[1]
    ligne3 = board[2]
    print("|".join(ligne1))
    print("|".join(ligne2))
    print("|".join(ligne3))
    print()
    if ia_rejouer == 1:
        lancement_ia()
    else:
        changement_joueur()

# Rejouer au jeu 
def relancer_partie():
    global tour
    global ia_rejouer
    print()
    rejouer = input("Souhaitez-vous rejouer ? ")
    print()
    if rejouer.lower() == "n" or rejouer.lower() == "non" or rejouer.lower() == "no":
        print("Aurevoir !")
        print()
    # Erreur si le joueur entre une lettre non demandé
    elif rejouer.lower() != "o" and rejouer.lower() != "oui" \
    and rejouer.lower() != "n" and rejouer.lower() != "non" and rejouer.lower() != "no":
        print("Erreur! Entrez [O]ui ou [N]on ")
        print()
        return relancer_partie()
    # Si le joueur souhaite jouer
    elif rejouer.lower() == "o" or rejouer.lower() == "oui":
        ia_rejouer = input("Contre qui souhaitez-vous jouer ? [1] l'IA ? ou [2] un humain ? ")
        if ia_rejouer == "1":
            efface()

# Vérifie si un joueur a une ligne gagnante OU si la partie est égalité
def verifie():
    # Joueur 1 - vérification horizontale
    if board[0] == ["X", "X", "X"] \
    or board[1] == ["X", "X", "X"] \
    or board[2] == ["X", "X", "X"]:
        print("HOORAY!")
        print("Joueur 1 gagne !")
        return True
    # Joueur 1 - vérification verticale
    elif board[0][0] == joueur_1 and board[1][0] == joueur_1 and board[2][0] == joueur_1 \
    or board[0][1] == joueur_1 and board[1][1] == joueur_1 and board[2][1] == joueur_1 \
    or board[0][2] == joueur_1 and board[1][2] == joueur_1 and board[2][2] == joueur_1:
        print("HOORAY!")
        print("Joueur 1 gagne !")
        return True
    # Joueur 1 - vérification diagonale
    elif board[0][0] == joueur_1 and board[1][1] == joueur_1 and board[2][2] == joueur_1 \
    or board[0][2] == joueur_1 and board[1][1] == joueur_1 and board[2][0] == joueur_1:
        print("HOORAY!")
        print("Joueur 1 gagne !")
        return True
    # Joueur 2 - vérification horizontale
    if board[0] == ["O", "O", "O"] \
    or board[1] == ["O", "O", "O"] \
    or board[2] == ["O", "O", "O"]:
        print("HOORAY!")
        print("Joueur 2 gagne !")
        return True
    # Joueur 2 - vérification verticale
    elif board[0][0] == joueur_2 and board[1][0] == joueur_2 and board[2][0] == joueur_2 \
    or board[0][1] == joueur_2 and board[1][1] == joueur_2 and board[2][1] == joueur_2 \
    or board[0][2] == joueur_2 and board[1][2] == joueur_2 and board[2][2] == joueur_2:
        print("HOORAY!")
        print("Joueur 2 gagne !")
        return True
    # Joueur 2 - vérification diagonale
    elif board[0][0] == joueur_2 and board[1][1] == joueur_2 and board[2][2] == joueur_2 \
    or board[0][2] == joueur_2 and board[1][1] == joueur_2 and board[2][0] == joueur_2:
        print("HOORAY!")
        print("Joueur 2 gagne !")
        return True
    # Vérification d'une égalité
    elif tour == 10:
        print("C'est une égalite !")
        print()
        return True
    else:
        return False

# Changement de joueur entre les tours
def changement_joueur():
    global tour
    global joueur_1
    global joueur_2
    global symbole
    print("Vous jouez désormais contre un joueur")
    print("Bonne Chance !")
    print()
    tour = 1
    while verifie() != True and tour <= 10:
        if tour % 2 == 1:
            symbole = joueur_1
            print("Joueur 1, c'est à ton tour de jouer!")
        else:
            symbole = joueur_2
            print("Joueur 2, c'est à ton tour de jouer!")
        actions()
        tour += 1
    relancer_partie()
    
                                   
# Défini l'action des joueurs ET vérifie si les informations demandées
def actions():
    global action_1
    global action_2
    # Erreur qui apparait si les éléments demandés ne sont pas respecté
    while True:
        action_1 = int(input("Sur quelle ligne voulez-vous jouer ? (1,2,3) : "))
        if action_1 > 3 or action_1 == 0:
            print()
            print("1- Erreur, entrez un numéro 1, 2 ou 3")
            print()
        else:
            break
    while True:
        action_2 = int(input("Dans quelle colonne ? (1,2,3) : "))
        if action_2 > 3 or action_2 == 0:
            print()
            print("2- Erreur, entrez un numéro 1, 2 ou 3")
            print()
        else:
            break
    # Détermine une action en ligne 1 
    # ET une erreur si l'emplacement est déjà occupé par l'adversaire
    if action_1 == 1:
        if ligne1[action_2 - 1] == "_":
            ligne1[action_2 - 1] = symbole
        else:
            print()
            print("OOPS! Il semblerait que cet emplacement soit déjà occupé.")
            print("Essaie-en un autre :)")
            print()   
            return actions()           
    # Détermine une action en ligne 2 
    # ET une erreur si l'emplacement est déjà occupé par l'adversaire
    elif action_1 == 2:
        if ligne2[action_2 - 1] == "_":
            ligne2[action_2 - 1] = symbole
        else:
            print()
            print("OOPS! Il semblerait que cet emplacement soit déjà occupé.")
            print("Essaie-en un autre :)")
            print()
            return actions()
    # Détermine une action en ligne 3 
    # ET une erreur si l'emplacement est déjà occupé par l'adversaire
    elif action_1 == 3:
        if ligne3[action_2 - 1] == "_":
            ligne3[action_2 - 1] = symbole
        else:
            print()
            print("OOPS! Il semblerait que cet emplacement soit déjà occupé.")
            print("Essaie-en un autre :)")
            print()
            return actions()
    # Imprime le rendu du tableau au fur a mesure des actions des joueurs
    print()
    print("|".join(ligne1))
    print("|".join(ligne2))
    print("|".join(ligne3))
    print()

def lancement_jeu():
    print("Commencer une partie contre: ")
    print()
    partie = int(input("[1] une IA ou [2] un joueur : "))
    print()
    # Si le joueur choisi de jouer contre une IA
    if partie == 1:
        # Imprime le modèle du tableau
        print()
        print("|".join(ligne1))
        print("|".join(ligne2))
        print("|".join(ligne3))
        print()
        lancement_ia()
    # Si le joueur choisi de jouer contre un joueur réel
    elif partie == 2:
        # Imprime le modèle du tableau
        print("|".join(ligne1))
        print("|".join(ligne2))
        print("|".join(ligne3))
        print()
        changement_joueur()
    # Affiche une erreur si le numéro entré n'est pas celui demandé
    else:
        print("! ERREUR !")
        print("Saisissez 1 ou 2")
        print("[1] Pour jouer contre une IA")
        print("[2] pour jouer contre un adversaire réel")
        print()
        return lancement_jeu()
        
# Pré-lancement du jeu - Message d'Accueil
def pre_lancement():
    print()
    print("Bienvenue dans Tik Tak Toe ! ")
    print("Un monde de grilles et de symboles")
    print()
    lancement_jeu()

# Appel au lancement du jeu dans le terminal
pre_lancement()
