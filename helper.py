def draw_board(emplacements):
    """imprime la grille du jeu.

    Args:
        emplacements (dict): dictionnaire comportant les cases du jeu
    """
    board=(f"|{emplacements[7]}|{emplacements[8]}|{emplacements[9]}|\n"
           f"|{emplacements[4]}|{emplacements[5]}|{emplacements[6]}|\n"
           f"|{emplacements[1]}|{emplacements[2]}|{emplacements[3]}|")
    print(board)
    
# Fonction d'impression de la grille


def tour_jeu(tour):
    """Fonction qui permet d'avoir les tours du jeu.

    Returns:
        Renvoi X ou O dans une case de la grille.
    """
    if tour % 2 == 0:
        return "O"
    else:
        return "X"

# fonction qui verifie les tour du jeu

def jeu_gagne(emplacements):
  """Verification si le jeu est gagné ou pas.

  Args:
      Prend les valeurs du dico emplacements et verifie si 3 d'entre elles sont idéntiques.

  Returns:
      Renvoi un vrai ou faux dans le cas ou il y a partie gagné ou pas respectivement.
  """
  if   (emplacements[1]==emplacements[2]==emplacements[3]) \
    or (emplacements[4]==emplacements[5]==emplacements[6]) \
    or (emplacements[7]==emplacements[8]==emplacements[9]):
    return True
  elif (emplacements[1]==emplacements[4]==emplacements[7]) \
    or (emplacements[2]==emplacements[5]==emplacements[8]) \
    or (emplacements[3]==emplacements[6]==emplacements[9]):
    return True
  elif (emplacements[1]==emplacements[5]==emplacements[9]) \
    or (emplacements[3]==emplacements[5]==emplacements[7]):
    return True
  else:
    return False
      


