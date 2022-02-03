
from tkinter import font
import turtle

ventana = turtle.Screen ()
ventana.title('crazy snake')
ventana.bgcolor('black')
ventana.setup(width=600, height=600)


barrera = turtle.Turtle()
barrera.goto (-300, 240)
barrera.pensize (2)
barrera.pencolor ('blue')
barrera.speed(2)
barrera.goto(300, 240)
barrera.hideturtle()

def creacion_elemento(forma, color):
    elemento = turtle.Turtle()
    elemento.speed(0)
    elemento.penup()
    elemento.shape(forma)
    elemento.color(color)
    elemento.goto(0, 0)
    return elemento

cabeza  = creacion_elemento('square', 'white')
cabeza.direccion = 'quieto'
comida = creacion_elemento('circle', 'yellow') 
comida.goto(0, 80)
texto = creacion_elemento(None, 'red')
texto.hideturtle()
texto.goto(0, 260)
texto.write(' CRAZY SNAKE', align='center', font=('aAbrigyThink', 20, 'normal' ))

def arriba ():
    cabeza.direccion = 'arriba'
    
def abajo ():
    cabeza.direccion = 'abajo'
    
def derecha ():
    cabeza.direccion = 'derecha'
    
def izquierda ():
    cabeza.direccion = 'izquierda'


ventana.listen()
ventana.onkeypress(arriba, 'Up')
ventana.onkeypress(abajo, 'Down')
ventana.onkeypress(derecha, 'Right')
ventana.onkeypress(izquierda, 'Left')



def movimiento():
    if cabeza.direccion == 'arriba':
        y = cabeza.ycor()
        cabeza.sety(y+20)

    if cabeza.direccion == 'abajo':
        y = cabeza.ycor()
        cabeza.sety(y-20)
        
    if cabeza.direccion == 'derecha':
        x = cabeza.xcor()
        cabeza.setx(x+20)

    if cabeza.direccion == 'izquierda':
        x = cabeza.xcor()
        cabeza.setx(x-20)



