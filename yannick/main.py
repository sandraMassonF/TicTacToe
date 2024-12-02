taille_grille = 3 
zone = ["-"]
selection_joueur = []


# mise en place de la grille
ligne1 = ["-","-","-"]
ligne2 = ["-","-","-"]
ligne3 = ["-","-","-"]
print("|".join(ligne1))
print("|".join(ligne2))
print("|".join(ligne3))

# demande des cohordonnés 
colone = int(input("Choisissez dans quelle colone (chiffre entre 1 et 3): "))
ligne = int(input("Choisissez dans quelle ligne (chiffre entre 1 et 3): "))

# suivi des coups joués
case_selectionné = colone, ligne
selection_joueur.append(case_selectionné)

# selection de la ligne joué
if ligne