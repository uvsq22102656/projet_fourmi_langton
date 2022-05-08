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
from tracemalloc import stop

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
p = True
compt = 0 #variable pour relancer le jeu apres avoir mis sur pause

#position initiale au milieu du canvas orienté Nord
X = LARGEUR_CASE*N//2
Y = HAUTEUR_CASE*N//2
pos = (N//2,N//2)
dir = "N"

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
    """- cree la liste id à la bonne taille
    - fait apparaitre la fourmi au milieu du tableau"""
    global id, fourmi
    id = [[0]*(N) for k in range(N)] #initialisation de la grille blanche = 0
    fourmi = canvas.create_polygon((X+LARGEUR_CASE//2,Y), (X+LARGEUR_CASE,Y+HAUTEUR_CASE), (X,Y+HAUTEUR_CASE),
                                    fill="blue")

def mouvement(pos, dir, id):
    """- fait tourner la fourmi de 90° (N<-Gauche / B->Droite)
    - deplace d'une case la fourmi en prenant compte de son orientation
    (fonction inspirée de http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)"""
    global fourmi
    i, j = pos

    if id[i][j] == 0:
        if dir == "N":
            j += 1
            if j == N:
                j=0 
            dir = "E"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE,y+HAUTEUR_CASE//2), (x,y), (x,y+HAUTEUR_CASE),
                                            fill='blue')
        elif dir == "S":
            j -= 1
            if j<0:
                j=N-1
            dir = "O"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x,y+HAUTEUR_CASE//2), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x+LARGEUR_CASE,y),
                                            fill='blue')
        elif dir == "E":
            i += 1
            if i==N :
                i=0 
            dir = "S"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y+HAUTEUR_CASE), (x,y), (x+LARGEUR_CASE,y),
                                            fill='blue')
        elif dir == "O":
            i -= 1
            if i<0:
                i=N-1
            dir = "N"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x,y+HAUTEUR_CASE),
                                            fill='blue')
    else:
        if dir == "S":
            j += 1
            if j==N:
                j=0 
            dir = "E"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE,y+HAUTEUR_CASE//2), (x,y), (x,y+HAUTEUR_CASE),
                                            fill='blue')
        elif dir == "N":
            j -= 1
            if j<0:
                j=N-1
            dir = "O"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x,y+HAUTEUR_CASE//2), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x+LARGEUR_CASE,y),
                                            fill='blue')
        elif dir == "O":
            i += 1
            if i==N:
                i=0 
            dir = "S"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y+HAUTEUR_CASE), (x,y), (x+LARGEUR_CASE,y),
                                            fill='blue')
        elif dir == "E":
            i -= 1
            if i<0:
                i=N-1
            dir = "N"
            x = j*LARGEUR_CASE
            y = i*HAUTEUR_CASE
            canvas.delete(fourmi)
            fourmi = canvas.create_polygon((x+LARGEUR_CASE//2,y), (x+LARGEUR_CASE,y+HAUTEUR_CASE), (x,y+HAUTEUR_CASE),
                                            fill='blue')

    return (i,j), dir
    

def modif_case(pos, dir, id):
    """- modifie l'etat de l'ancienne case apres que la fourmi l'ai quitte
    - renvoie la nouvelle position et la direction (+ id de la case sur laquelle est arrive la fourmi)
    pour les modifier à l'etape suivante
    (fonction inspirée de http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)"""
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
    lance l'animation
    (fonction inspirée de http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html)"""
    global pos, dir, p
    if p:
        pos, dir = modif_case(pos, dir, id) #on stocke les nouvelles valeurs
        canvas.after(vitesse, play)
    else:
        p = True

def pause():
    """permet d'arreter le programme"""
    global p
    p = False

def sauvegarde():
    """Ecrit la taille de la grille et les valeurs de la variable
     terrain das le fichier sauvegarde.txt
     -> fonction provenant du code generation_terrain fait en cours
     """
    fic = open("sauvegarde.txt", "w")
    i, j = pos
    fic.write(str(N) + " " + str(i) + " " + str(j) + " "+ str(dir) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(id[i][j]) + "\n")
    fic.close()

def load():
    """
    Lire le fichier sauvegarde.txt et affiche dans le canvas la configuration lu
     -> fonction provenant du code generation_terrain fait en cours
    """
    global N, id, pos, dir
    fic = open("sauvegarde.txt", "r") 
    l1 = fic.readline()
    a = l1.split()
    N = int(a[0])
    pos = (int(a[1]), int(a[2]))
    dir = a[3]
    canvas.delete()
    c_fourmi()
    i = j = 0
    for ligne in fic:
        id[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    print(id)
    p = True
    fic.close()

def dim_vitesse():
    """diminue la vitesse lorque l'utilisateur clique sur le bouton ralentir
    vitesse minimale : 1000 ms entre chaque etape"""
    global vitesse
    if vitesse < 1000:
        vitesse += 100

def aug_vitesse():
    """augmente la vitesse lorque l'utilisateur clique sur le bouton accelerer
    vitesse maximale : 10ms entre chaque etape"""
    global vitesse
    if vitesse > 200:
        vitesse -= 100
    else:
        vitesse = 10

############################
# programme principal

racine = tk.Tk()
racine.title("Fourmi de Langton")

# définition des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)

bouton_play = tk.Button(racine, text='play', command=play)
bouton_pause = tk.Button(racine, text='pause', command=pause)
bouton_aug = tk.Button(racine, text='accelerer', command=aug_vitesse)
bouton_dim = tk.Button(racine, text='ralentir', command=dim_vitesse)
bouton_save = tk.Button(racine, text='sauvegarder', command=sauvegarde)
bouton_load = tk.Button(racine, text='ancienne configuration', command=load)



#position des widgets
canvas.grid(row=0, column=1, columnspan=5, rowspan=2)
bouton_play.grid(row=2, column=1)
bouton_pause.grid(row=2, column=2)
bouton_aug.grid(row=2, column=5)
bouton_dim.grid(row=2, column=6)
bouton_save.grid(row=0, column=0)
bouton_load.grid(row=1, column=0)

c_fourmi()

#boucle principale 
racine.mainloop()