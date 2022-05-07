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

#vitesse d'execution en ms
vitesse = 1000

##############################
# variables globales en plus des widgets
fourmi = None

#position initiale au milieu du canvas orienté Nord
X = LARGEUR_CASE*N//2
Y = HAUTEUR_CASE*N//2
pos = (N//2,N//2)
dir = "N"

#initialisation de la grille blanche = 0
id = [[0]*(N) for k in range(N)]

############################
# fonction

def creation_case(i,j):
    """ne cree que les cases noires, cases blanches = canvas vierge"""
    x = j*LARGEUR_CASE
    y = i*HAUTEUR_CASE
    case = canvas.create_rectangle((x,y), (x+LARGEUR_CASE,y+HAUTEUR_CASE),
                                    fill='black')
    return case

def c_fourmi():
    """fait apparaitre la fourmi au milieu du tableau"""
    #changer cette fonction pour qu'on puisse la faire apparaitre a differents endroits
    global fourmi
    fourmi = canvas.create_polygon((X+LARGEUR_CASE//2,Y), (X+LARGEUR_CASE,Y+HAUTEUR_CASE), (X,Y+HAUTEUR_CASE),
                                    fill="blue")

def mouvement(pos, dir, id):
    """- fait tourner la fourmi de 90° (N<-Gauche / B->Droite)
    et deplace d'une case la fourmi en prenant compte de son orientation"""
    global fourmi
    i, j = pos

    if id[i][j] == 0:
        if dir == "N":
            j += 1
            dir = "E"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE,y+HAUTEUR_CASE//2), (x,y), (x,y+HAUTEUR_CASE),
                                            fill='blue')
        elif dir == "S":
            j -= 1
            dir = "O"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x,y+HAUTEUR_CASE//2), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x+LARGEUR_CASE,y),
                                            fill='blue')
        elif dir == "E":
            i += 1
            dir = "S"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y+HAUTEUR_CASE), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (X,Y+HAUTEUR_CASE),
                                            fill='blue')
        elif dir == "O":
            i -= 1
            dir = "N"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x,y+HAUTEUR_CASE),
                                            fill='blue')
    else:
        if dir == "S":
            j += 1
            dir = "E"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE,y+HAUTEUR_CASE//2), (x,y), (x,y+HAUTEUR_CASE),
                                            fill='blue')
        elif dir == "N":
            j -= 1
            dir = "O"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x,y+HAUTEUR_CASE//2), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x+LARGEUR_CASE,y),
                                            fill='blue')
        elif dir == "O":
            i += 1
            dir = "S"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y+HAUTEUR_CASE), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (X,Y+HAUTEUR_CASE),
                                            fill='blue')
        elif dir == "E":
            i -= 1
            dir = "N"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x,y+HAUTEUR_CASE),
                                            fill='blue')

    return (i,j), dir
    

def modif_case(pos, dir, id):
    """modifie l'etat de l'ancienne case apres que la fourmi l'ai quitte
    puis renvoie la nouvelle position + id de la case (sur laquelle est arrive la fourmi)
    pour la modifier à l'etape suivante"""
    (ni,nj), ndir = mouvement(pos, dir, id)
    i,j = pos
    case = id[i][j]
    if case == 0:
        case = creation_case(i,j)
        id[i][j] = case
    else:
        canvas.delete(case)
        id[i][j] = 0

    return (ni,nj), ndir

def play():
    """initialise la fourmi au milieu
    lance l'animation"""
    global pos, dir
    pos, dir = modif_case(pos, dir, id) #on stocke les nouvelles valeurs
    canvas.after(vitesse, play)
    #tore()
    

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

def dim_vitesse(event):
    """diminue la vitesse lorque l'utilisateur clique sur le bouton ralentir
    vitesse minimale : 1000 ms entre chaque etape"""
    global vitesse
    if vitesse < 1000:
        vitesse += 10

def aug_vitesse(event):
    """augmente la vitesse lorque l'utilisateur clique sur le bouton accelerer
    vitesse maximale : 10ms entre chaque etape"""
    global vitesse
    if vitesse > 20:
        vitesse -= 10

############################
# programme principal

racine = tk.Tk()
racine.title("Fourmi de Langton")

# définition des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)

bouton_play = tk.Button(racine, text='play', command=play)
bouton_pause = tk.Button(racine, text='pause', command=pause)
bouton_aug = tk.Button(racine, text='>>', command=aug_vitesse)
bouton_dim = tk.Button(racine, text='<<', command=dim_vitesse)


#position des widgets
canvas.grid(columnspan=3)
bouton_play.grid(row=1, column=0)
bouton_aug.grid(row=1, column=2)
bouton_dim.grid(row=1, column=3)

c_fourmi()

#boucle principale 
racine.mainloop()