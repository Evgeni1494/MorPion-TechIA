from helper import draw_board, tour_jeu, jeu_gagne
import os
emplacements = {1:"1",2:"2",3:"3",4:"4",
                 5:"5",6:"6",7:"7",8:"8",9:"9"}


#draw_board(emplacements)

# Boucle du jeu
tour_avant= -1
jeu_en_cours = True
fin = False
tour = 0 
while jeu_en_cours:
    # Refaire la grille a chaque fois que un choix est fait
    os.system("cls" if os.name == "nt" else "clear")
    #dessiner la grille
    draw_board(emplacements)
    # verifie que la case selectionnée est bien valide
    if tour_avant == tour:
        print("La case selectioné est déja prise. Choisisez une autre case.")
        tour_avant == tour
    print("Tour du jouer " + str((tour%2)+1) + ": faite votre choix.")
    # obtenir l'input du jouer
    choix = input()
    if choix == 'q':
        # moyen d'eteindre le jeu
        jeu_en_cours = False
        # verifier que le nombre de l'input est bien entre 1 et 9
    elif str.isdigit(choix) and int(choix) in emplacements:
        # verifie si l'emplacement n'a pas déja était pris
        if not emplacements[int(choix)] in {"X","O"}:
            #tout va bien on passe au tour suivant
                tour +=1
                emplacements[int(choix)] = tour_jeu(tour)
        # Verifier si le jeu est gagné ou pas.
    if jeu_gagne(emplacements): jeu_en_cours, fin = False, True
    if tour > 8: jeu_en_cours = False
    
    
# en dehors de la boucle on fait voir les résultats et la grille.
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(emplacements)
if fin:
    if tour_jeu(tour) == "X":print("Jouer 1 Gagne!")
    else: print("jouer 2 Gagne!")
else:
    print("Personne gagne...")

print("Merci d'avoir joué !")
    



























