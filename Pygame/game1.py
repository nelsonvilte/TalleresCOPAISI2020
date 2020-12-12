import sys, pygame
pygame.init()

size = (800,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mi primer ventana")
 
#Reloj, para controlar los frames por segundo (FPS)
clock = pygame.time.Clock()

#indicamos la posicion inicial de la figura, de acuerdo a coord x e y
#teniendo en cuenta que este punto hace referencia al extremos superior izq del cuadrado
coord_x = 400
coord_y = 300 

#velocidad a la que se moverá
speed_x = 2
speed_y = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   
    #Dar el efecto de rebote en la pantalla
    if (coord_x >= 720 or coord_x <= 0): 
        speed_x *= -1 #invertimos la velocidad
    
    if(coord_y >= 410 or coord_y <= 0):
        speed_y *= -1 
    
    screen.fill((0,0,0)) #Rellena la superficie con un color sólido. Si no se proporciona ningún argumento rect, se rellenará toda la superficie.
      
    #Genera el movimiento
    #Desplazamiento horizontal
    coord_x += speed_x

    #Desplazamiento vertical
    coord_y += speed_y
    

    #Dibujamos figuras geometricas
    pygame.draw.rect(screen,(255,0,0),(coord_x,coord_y,80,90))
    #pygame.draw.circle(screen, (0,255,0), [coord_x,coord_y], 35)
    
    #Muestra la figura en pantalla
    pygame.display.flip()
    #pygame.display.update()
    
    clock.tick(60)
