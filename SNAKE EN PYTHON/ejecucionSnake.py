import crazySnake
import random
import time


partes_del_snake = []

cabeza = crazySnake.cabeza
comida = crazySnake.comida
texto = crazySnake.texto

puntuacion=0
mejor_puntaje=0




def  game_over():
      time.sleep (1)
      cabeza.goto(0,0)
      cabeza.direccion = 'quieto'
      for i in partes_del_snake:
            i.hideturtle()
      partes_del_snake.clear()
      texto.clear()
      texto.write('Puntuacion: {} Mejor puntaje:{}'.format(puntuacion, mejor_puntaje), align='center', font=('aAbrigyThink', 20, 'normal' ))

      


while True:
     crazySnake.ventana.update()
     
     if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 220 or cabeza.ycor() < -280:
       puntuacion = 0
       game_over()


   
     
    
     if cabeza.distance(comida) < 20:
           x = random.randint(-14,14)
           y = random.randint(-14,10)
           comida.goto(x*20, y*20)
           nuevas_partes = crazySnake.creacion_elemento ('square', 'white')
           nuevas_partes.direccion = 'quieto'
           partes_del_snake.append(nuevas_partes)

           puntuacion+= 1
           if puntuacion > mejor_puntaje:
                 mejor_puntaje = puntuacion
                 texto.clear()
                 texto.write('Puntuacion: {} Mejor puntaje:{}'.format(puntuacion, mejor_puntaje), align='center', font=('aAbrigyThink', 20, 'normal' ))



    
     partes_totales = len(partes_del_snake)
             
     for i in range(partes_totales-1, 0, -1):
                     x = partes_del_snake[i-1].xcor()
                     y = partes_del_snake[i-1].ycor()
                     partes_del_snake[i].goto(x, y)
     if partes_totales > 0:
                      x = cabeza.xcor()
                      y = cabeza.ycor()
                      partes_del_snake[0].goto(x, y)
    
            
 
    
     crazySnake.movimiento()
     
     
     for i in partes_del_snake:
           if i.distance (cabeza) < 20:
               puntuacion = 0
               game_over()
  
     time.sleep(0.05)




