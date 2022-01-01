import turtle

#definit la taille de l'ecran
turtle.setup(1000,1000)
screen = turtle.Screen()

#Images correspondantes aux cases
green = "cases/green.gif"
screen.addshape(green)
red = "cases/red.gif"
screen.addshape(red)
blue = "cases/blue.gif"
screen.addshape(blue)

images=[green,red,blue]

#Image de l'étoile
star = "cases/star.gif"
screen.addshape(star)

#Images des personnages
mario = "perso/mario.gif"
screen.addshape(mario)
yoshi = "perso/yoshi.gif"
screen.addshape(yoshi)
toad = "perso/toad.gif"
screen.addshape(toad)
luigi = "perso/luigi.gif"
screen.addshape(luigi)

imagesPerso=[mario,yoshi,toad,luigi]

#Listes de stockage des turtles du plateau
turtles = []
perso = []
turtle_star=turtle.Turtle()

def cherche_place(ind,m):
    """
    Cherche la position dans le screen correspond à un indice du plateau.
    :param ind: (int) l'indice pour lequel on cherche la place.
    :param m: (list) liste d'entiers correspondant au plateau.
    :return: (float,float) la position trouvée dans le screen. 
    :CU: -1 < ind < len(m)
    """
    side_size = len(m)/4
    x_size=-((side_size+1)*100)/2+50
    y_size=((side_size+1)*100)/2-50
    if(ind <= side_size):
        x = ind
        y = 0
    elif(ind < 2*side_size):
        x = side_size
        y = ind-side_size
    elif(ind < 3*side_size):
        x = side_size-(ind%side_size)
        y = side_size
    else:
        x = 0
        y = side_size-(ind%side_size)
            
    return(x_size+(x*100),y_size-(y*100))

def cree_plateau(m):
    """
    Crée le plateau sur le screen. Le plateau est décrit par une liste d'entiers.
    :param m: (list) liste d'entiers correspondant au plateau à dessiner.
    Un 1 dans la liste correspond à une case verte, un 2 correspond à une case rouge et un 3 à une case bleue.
    :return: (None)
    :CU: len(m) doit être un multiple de 4
    """
    for i in range(len(m)):
        x,y=cherche_place(i,m) 
        case = m[i]
        if(case > 0):
            t = turtle.Turtle()
            turtles.append(t)
            t.speed(0)
            t.up()
            t.goto(x,y)
            t.down()
            t.shape(images[m[i]-1])
            
            
def cree_perso(joueurs,m):
    """
    Ajoute les joueurs sur le plateau.
    :param joueurs: (list) liste de dictionnaires.
    :param m: (list) liste d'entiers correspondant au plateau.
    :return: (None)
    :CU: chaque dictionnaire doit contenir une clé "position" correspondant à une position sur le plateau m.
    Pour chaque dictionnaire de joueurs, -1 < j["position"] < len(m)
    """
    for p in range(len(joueurs)):
        i = joueurs[p]["position"]
        
        x,y=cherche_place(i,m)
        t = turtle.Turtle()
        perso.append(t)
        t.speed(0)
        t.up()
        t.goto(x,y)
        t.down()
        t.shape(imagesPerso[p])                

def efface_plateau():
    """
    Efface tous les éléments du plateau (étoile, personnages, cases).
    """
    for i in range(len(turtles)):
        t = turtles.pop()
        t.clear()
        t.ht()
    for j in range(len(perso)):
        t=perso.pop()
        t.clear()
        t.ht()
    turtle_star.reset()
    
def place_etoile(ind,m):
    """
    Place l'étoile sur le plateau.
    :param ind: (int) indice de la case où doit être positionnée l'étoile.
    :param m: (list) liste d'entiers correspondant au plateau.
    :return: (None)
    :CU: -1 < ind < len(m)
    """
    x,y=cherche_place(ind,m)
    turtle_star.speed(0)
    turtle_star.up()
    turtle_star.goto(x,y)
    turtle_star.down()
    turtle_star.shape(star)                

def bouge_perso(joueurs,m):
    """
    Modifie la position d'un personnage sur le plateau.
    :param joueurs: (list) liste de dictionnaires.
    :param m: (list) liste d'entiers correspondant au plateau.
    :return: (None)
    :CU: chaque dictionnaire doit contenir une clé "position" correspondant à une position sur le plateau m.
    Pour chaque dictionnaire de joueurs, -1 < j["position"] < len(m)
    """
    for p in range(len(joueurs)):
        i=joueurs[p]["position"]
        x,y=cherche_place(i,m)
        t = perso[p]
        t.up()
        t.goto(x,y)
        t.down()
