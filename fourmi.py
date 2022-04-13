#########################################
# DLMP groupe 6
# NOUVEAU Maxence
# DERWEL Nathan 
# VOLIVERT Coline
# https://github.com/uvsq-info/l1-python
#########################################

#########################
# import des librairies
import tkinter as tk
import random as rd

#########################

# taille de la grille carrée
N = 4
# dimensions du canvas et de la grille
LARGEUR = 500
HAUTEUR = 500
LARGEUR_CASE = LARGEUR // N
HAUTEUR_CASE = HAUTEUR // N

# dimensions de la fourmi
L_f = LARGEUR_CASE // 3
H_f = HAUTEUR_CASE

#########################################
# variables globales en plus des widgets

# objets graphiques représentant la grille dans un tableau 2D
grille = None
# configuration courante dans un tableau 2D de dimension N+2
# pour tenir compte des bords
config_cur = None

############################
# fonction
def init_grille():
    """Retourne une grille carrée vide
       dimension N, les éléments de la configuration vont de 1 à N
    """
    global grille, config_cur    
    liste_couleur =["white", "black"]
    grille = [[0 for i in range(N+1)] for j in range(N+1)]
    config_cur = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(1, N+1):
        x = (i - 1) * LARGEUR_CASE
        for j in range(1, N+1):
            y = (j - 1) * HAUTEUR_CASE
            n = rd.randint(0,1)
            couleur = liste_couleur[n]
            carre = canvas.create_rectangle(x, y, x+LARGEUR_CASE,
                                            y+HAUTEUR_CASE, fill=couleur,
                                            outline="grey50")
            grille[i][j] = carre
    fourmi()


def fourmi():
    global fourmi
    x = 0
    y = 0
    fourmi = canvas.create_rectangle((x+L_f,y), (x+2*L_f,y+HAUTEUR_CASE),
                                    fill="blue")




############################
# programme principal

racine = tk.Tk()
racine.title("Fourmi de Langton")

# définition des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
bouton_play = tk.Button(racine, text='play')

init_grille()

#position des widgets
canvas.grid()
bouton_play.grid()

#boucle principale 
racine.mainloop()