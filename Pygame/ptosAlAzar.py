# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
 
# Traducción por: Ricardo Torres
# https://rctorr.wordpress.com
 
# Importa la librería llamada 'pygame'
import pygame
# Importa la librería llamada 'random'
import random
 
# Inicializa la maquina de juego
pygame.init()
 
# El color del fondo
black = [ 0, 0, 0]
# El color de la nieve
white = [255,255,255]
 
# Asigna el ancho y alto de la ventana
size=[400,400]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Animación de nieve!")
 
# Crea un arreglo vacío
star_list=[]
 
# Repite 50 veces adicionando una estrella de nieve en una posición aleatoria x,y
for i in range(50):
    x=random.randrange(0,400)
    y=random.randrange(0,400)
    star_list.append([x,y])
 
clock = pygame.time.Clock()
 
# Repite hasta que el usuario de click en el botón cerrar.
done=False
while done==False:
 
    for event in pygame.event.get(): # El usuario hizo algo
        if event.type == pygame.QUIT: # Si el usuario hizo click en botón cerrar
            done=True # La bandera que se usa para del ciclo es 'done'
 
    # Se asigna el color de fondo
    screen.fill(black)
 
    # Se procesa cada estrella de nieve de la lista
    for i in range(len(star_list)):
        # Se dibuja la estrella de nieve
        pygame.draw.circle(screen,white,star_list[i],2)
 
        # Se mueve la estrella de nieve un pixel hacia abajo
        star_list[i][1]+=1
 
        # Si la estrella de nieve se mueve más allá del limite inferior de la
        # ventana
        if star_list[i][1] > 400:
            # La mueve de nuevo a la parte superior de la ventana
            y=random.randrange(-50,-10)
            star_list[i][1]=y
            # Da a esta una nueva posición x
            x=random.randrange(0,400)
            star_list[i][0]=x
 
    # Actualiza la ventana con lo que se ha dibujado.
    pygame.display.flip()
    clock.tick(20)
 
# Si olvida esta línea el programa se puede congelar al salir.
pygame.quit ()