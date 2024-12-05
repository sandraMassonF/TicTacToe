
victoire = False
case_prise = "False"
# mise en place de la grille
ligne1 = ["-","-","-"]
ligne2 = ["-","-","-"]
ligne3 = ["-","-","-"]
def grille():
    print("|".join(ligne1))
    print("|".join(ligne2))
    print("|".join(ligne3))
grille()
selection_colonne = ""
selection_ligne = ""
total_selection= []
message_victoire = ""
# condition de victoire
def condition_victoire(ligne1, ligne2, ligne3):
    global victoire
    global message_victoire
# les lignes
    if ligne1[0] == "O" and ligne1[1] == "O" and ligne1[2] == "O":
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne1[0] == "X" and ligne1[1] == "X" and ligne1[2] == "X":
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
    elif ligne2[0] == "O" and ligne2[1] == "O" and ligne2[2] == "O":
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne2[0] == "X" and ligne2[1] == "X" and ligne2[2] == "X":
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
    elif ligne3[0] == "O" and ligne3[1] == "O" and ligne3[2] == "O":
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne3[0] == "X" and ligne3[1] == "X" and ligne3[2] == "X":
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
# les colonnes
    elif ligne1[0] == "O" and ligne2[0] == "O" and ligne3[0] == "O":
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne1[0] == "X" and ligne2[0] == "X" and ligne3[0] == "X":
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
    elif ligne1[1] == "O" and ligne2[1] == "O" and ligne3[1] == "O":   
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne1[1] == "X" and ligne2[1] == "X" and ligne3[1] == "X":   
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
    elif ligne1[2] == "O" and ligne2[2] == "O" and ligne3[2] == "O":   
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne1[2] == "X" and ligne2[2] == "X" and ligne3[2] == "X":   
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
# les diagonales
    elif ligne1[0] == "O" and ligne2[1] == "O" and ligne3[2] == "O":   
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne1[0] == "X" and ligne2[1] == "X" and ligne3[2] == "X":   
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
    elif ligne1[2] == "O" and ligne1[1] == "O" and ligne1[0] == "O":   
        victoire = True
        message_victoire = "Victoire Joueur 1 !"
    elif ligne1[2] == "X" and ligne1[1] == "X" and ligne1[0] == "X":   
        victoire = True
        message_victoire = "Victoire Joueur 2 !"
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
    
# JOUEUR 1
# demande des cohordonnés
def joueur1():
    global case_prise
    case_prise = "False"
    print("Joueur 1")
    selection_ligne = int(input("Choisissez dans quelle ligne (chiffre entre 1 et 3): "))
    selection_colonne = int(input("Choisissez dans quelle colone (chiffre entre 1 et 3): "))
# on vérifie que la saisi est OK:
    if selection_ligne > 3 or selection_ligne < 1 or selection_colonne > 3 or selection_colonne < 1:
        print("le chiffre entré est invalide !")
        joueur1()
    else:
# on vérifie si la case est occupée 
        occuper(selection_ligne,selection_colonne)
        
        if selection_ligne == 1:
            ligne1[selection_colonne-1] = "O"
                    
        elif selection_ligne == 2:
            ligne2[selection_colonne-1] = "O"
                    
        elif selection_ligne == 3:
            ligne3[selection_colonne-1] = "O"        
# mise à jour de la grille
        grille()
        condition_victoire(ligne1, ligne2, ligne3)
# Joueur 2  
def joueur2():
    global case_prise
    case_prise = "False"        
    print("Joueur 2")
    selection_ligne = int(input("Choisissez dans quelle ligne (chiffre entre 1 et 3): "))
    selection_colonne = int(input("Choisissez dans quelle colone (chiffre entre 1 et 3): "))
# on vérifie que la saisi est OK:
    if selection_ligne > 3 or selection_ligne < 1 or selection_colonne > 3 or selection_colonne < 1:
        print("le chiffre entré est invalide !")
        joueur2()
    else:
# on vérifie si la case est occupée
        occuper(selection_ligne, selection_colonne)
        if selection_ligne == 1:
            ligne1[selection_colonne-1] = "X"
                    
        elif selection_ligne == 2:
            ligne2[selection_colonne-1] = "X"
                    
        elif selection_ligne == 3:
            ligne3[selection_colonne-1] = "X"
    # mise à jour de la grille            
        grille()
        condition_victoire(ligne1, ligne2, ligne3)
    
# selection de la ligne joué
def start_game():
    while victoire != True:
        joueur1()
        if victoire == True:
            break
        while case_prise == "True":
            joueur1()
        if len(total_selection) == 9:
            print("Dommage personne à réussi à gagner !")
            restart = input("refaire une partie ? oui ou non :")
            if restart == "oui":
                start_game()
            else:
                ("Ciao ! ")
        joueur2()
        if victoire == True:
            break
        while case_prise == "True":
            joueur2()
        
start_game()
