import pygame

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("PyGame games") #название для игры
icon = pygame.image.load('images/icon1.webp')
pygame.display.set_icon(icon)

myfont = pygame.font.Font()

running = True

square = pygame.Surface((50, 120)) #создание квадрата
square.fill(('Red'))
while running:

    screen.blit(square, (10, 0))
    pygame.draw.circle(square, 'Yellow', (15,11), 10) #поверхность, цвет, центр круга, радиус

    #screen.fill((196, 41, 59)) #color picker по RGV

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #чтобы выйти из окна с помощью крестика
            running == False
            pygame.quit()
        
        #elif event.type == pygame.KEYDOWN: #нажатие на клавишу
            if event.key == pygame.K_f:
                screen.fill((196, 41, 142)) #меняет цвет фона

    