#########################################
# DLMP groupe 6
# NOUVEAU Maxence
# DERWEL Nathan 
# VOLIVERT Coline
# https://github.com/uvsq-info/l1-python
#########################################

"""->pour deplacer la fourmi, faire une liste avec tous les deplacements
possibles style : [[1,0],[0,1],[-1,0],[0,-1]] qui correspond respectivement
à avancer d'une case vers la droite, vers le bas, vers la gauche, vers le
haut
et ensuite faire des if pour chaque condition (couleur) et definir l'indice"""

#########################
# import des librairies
import tkinter as tk
import random as rd

#########################

# taille de la grille carrée
N = 10
# dimensions du canvas et de la grille
LARGEUR = 500
HAUTEUR = 500
LARGEUR_CASE = LARGEUR // N
HAUTEUR_CASE = HAUTEUR // N

##############################
# variables globales en plus des widgets

# objets graphiques représentant la grille dans un tableau 2D
grille = None

liste_couleur =["white", "black"]
coul = 0

############################
# fonction
def init_grille():
    """initialise la grille carrée de dimension N aleatoirement
    """
    global grille
    grille = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(0, N):
        x = i * LARGEUR_CASE
        for j in range(0, N):
            y = j * HAUTEUR_CASE
            n = rd.randint(0,1)
            carre = canvas.create_rectangle((x, y), (x+LARGEUR_CASE, y+HAUTEUR_CASE),
                                            fill=liste_couleur[n], outline="grey50")
            grille[i][j] = carre
            fic = open("config.txt", "w")
            fic.write(str(carre)+" ")
            fic.close()
    c_fourmi()


def c_fourmi():
    """fait apparaitre la fourmi dans la premiere case à gauche du tableau"""
    #changer cette fonction pour qu'on puisse la faire apparaitre a differents endroits
    global fourmi
    x = 0
    y = 0
    fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x,y+HAUTEUR_CASE),
                                    fill="blue")

def mouvement():
    """- fait tourner la fourmi de 90° (N<-Gauche / B->Droite)
    - change de couleur case
    - deplace d'une case la fourmi"""
    global coul
    x0,y0, x1,y1 = canvas.coords(fourmi)
    i = int(x0//LARGEUR_CASE)
    j = int(y0//HAUTEUR_CASE)

    if canvas['bg'] == 'white': # REECUPERER COULEUR (CONFIGURATION DE LA GRILLE) DANS UN FICHIEEEEER
        coul = 1-coul
        canvas.itemconfigure(grille[i][j], fill=liste_couleur[coul])
        canvas.itemconfigure(grille[i][j], (x+L_f,y-L_f),(x0+L_f,y0-L_f))
        canvas.move(fourmi, LARGEUR_CASE, 0)

    if canvas['bg'] == 'black':
        coul = 1-coul
        canvas.itemconfigure(grille[i][j], fill=liste_couleur[coul])
        canvas.itemconfigure(grille[i][j], (x+L_f,y-L_f),(x0+L_f,y0-L_f))      
        canvas.move(fourmi, -LARGEUR_CASE, 0)
    
    canvas.after(20, mouvement)
    tore()

def tore():
    """la fourmi passe de l'autre coté du canvas quand elle atteint un bord"""
    x0, y0, x1, y1 = canvas.coords(fourmi)
    if x1<0:
        canvas.coords(fourmi, x0+LARGEUR,y0, x1+LARGEUR, y1)
    if x0>LARGEUR :
        canvas.coords(fourmi, x0-LARGEUR,y0, x1-LARGEUR, y1)
    if y1<0:
        canvas.coords(fourmi, x0, y0+HAUTEUR, x1, y1+HAUTEUR)
    if y0>HAUTEUR:
        canvas.coords(fourmi, x0,y0-HAUTEUR, x1, y1-HAUTEUR)

def pause():
    """permet d'arreter le programme"""
    pass

def lecture_fichier():
    fic = open("config.txt", "r")
    for ligne in fic:
        id = ligne.split()

############################
# programme principal

racine = tk.Tk()
racine.title("Fourmi de Langton")

# définition des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
bouton_play = tk.Button(racine, text='play', command=mouvement)
bouton_pause = tk.Button(racine, text='pause', command=pause)

init_grille()

#position des widgets
canvas.grid()
bouton_play.grid()

#boucle principale 
racine.mainloop()