import sys, pygame
pygame.init()

size = (800,400)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Color
green = (0,255,0)

#para no visualizar el cursor encima de nuestro objeto
#Por defecto se encuentra en 1(visible el puntero)
pygame.mouse.set_visible(0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((255,255,255))
    
    #Primero
    #Para mover el objeto lo que necesitamos son las coordenadas del mouse
    mouse_pos = pygame.mouse.get_pos()
    
    #print(mouse_pos) #Mostramos como nos arroja la posicion del mouse, es una tupla

    mx_pos = mouse_pos[0]
    my_pos = mouse_pos[1]

    #Dibujamos el objeto, con la posición del mouse.
    pygame.draw.circle(screen, green, (mx_pos,my_pos),40)
    
    pygame.display.flip()#actualiza toda la pantalla / display muestra lo que los
    clock.tick(50)
        