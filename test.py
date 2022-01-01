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
l=generateur_liste()
plateau=cree_plateau(l)