# Déclaration des variables
victoire = False
case_prise = "False"
selection_colonne = ""
selection_ligne = ""
total_selection= []
message_victoire = ""
joueur = ""

# mise en place de la grille
ligne1 = ["-","-","-"]
ligne2 = ["-","-","-"]
ligne3 = ["-","-","-"]
def grille():
    print("|".join(ligne1))
    print("|".join(ligne2))
    print("|".join(ligne3))
grille()


# condition de victoire
def condition_victoire(ligne1, ligne2, ligne3, joueur):
    global victoire
    global message_victoire
    # les lignes
    if ligne1[0] ==  ligne1[1] ==  ligne1[2] == joueur:
        victoire = True
        message_victoire = f"Victoire {joueur} !"
    elif ligne2[0] ==  ligne2[1] ==  ligne2[2] == joueur:
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    elif ligne3[0] == ligne3[1] == ligne3[2] == joueur:
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    # les colonnes
    elif ligne1[0] == ligne2[0] == ligne3[0] == joueur:
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    elif ligne1[1] == ligne2[1] == ligne3[1] == joueur:   
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    elif ligne1[2] == ligne2[2] == ligne3[2] == joueur:   
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    # les diagonales
    elif ligne1[0] == ligne2[1] == ligne3[2] == joueur:   
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    elif ligne1[2] == ligne1[1] == ligne1[0] == joueur:   
        victoire = True
        message_victoire = f"Victoire joueur {joueur} !"
    print(message_victoire)
       
# Vérification si case occupée
def occuper(selection_ligne, selection_colonne):
    global case_prise
    case_occupe = []    
    case_occupe.append(selection_ligne) 
    case_occupe.append(selection_colonne)
    if case_occupe in total_selection:
        print("cette case à déjà été joué")
        print(total_selection)
        case_prise = "True"
    else:
        total_selection.append(case_occupe)
        print(total_selection)

# Choix du joueur/symbole
def choix_joueur():
    global joueur1, joueur2
    symbole = input("Veuillez choisir le symbole joueur 1 (X ou O) : ")
    symbole = symbole.upper()
    print(symbole)
    if symbole == "O":
        print("Le joueur 1 aura le symbole O !")
        print("Le joueur 2 aura le symbole X !")
        joueur1 = symbole
        joueur2 = "X"
    elif symbole == "X":
        print("Le joueur 1 aura le symbole X !")
        print("Le joueur 2 aura le symbole O !")
        joueur1 = symbole
        joueur2 = "O"
    else:
        print("Le symbole entré n'est pas valide ! ")
        choix_joueur()
        
# JOUEUR 1
# demande des cohordonnés
def tour_joueur(joueur):
    global case_prise
    case_prise = "False"
    print(f"Joueur {joueur}")
    selection_ligne = int(input("Choisissez dans quelle ligne (chiffre entre 1 et 3): "))
    selection_colonne = int(input("Choisissez dans quelle colone (chiffre entre 1 et 3): "))
    # on vérifie que la saisi est OK:
    if selection_ligne > 3 or selection_ligne < 1 \
    or selection_colonne > 3 \
    or selection_colonne < 1:
        print("le chiffre entré est invalide !")
        tour_joueur(joueur)
    else:
        # on vérifie si la case est occupée 
        occuper(selection_ligne,selection_colonne)
        
        if selection_ligne == 1:
            ligne1[selection_colonne-1] = joueur
                    
        elif selection_ligne == 2:
            ligne2[selection_colonne-1] = joueur
                    
        elif selection_ligne == 3:
            ligne3[selection_colonne-1] = joueur        
        # mise à jour de la grille
        grille()
        condition_victoire(ligne1, ligne2, ligne3, joueur)

# selection de la ligne joué
def turn_game():
    choix_joueur()
    while victoire != True:
        tour_joueur(joueur1)
        if victoire == True:
            break
        while case_prise == "True":
            tour_joueur(joueur1)
        if len(total_selection) == 9:
            print("Dommage personne à réussi à gagner !")
            restart = input("refaire une partie ? oui ou non :")
            if restart == "oui":
                turn_game()
            else:
                ("Ciao ! ")
                break
        tour_joueur(joueur2)
        if victoire == True:
            break
        while case_prise == "True":
            tour_joueur(joueur2)
        
turn_game()