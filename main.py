# import pygame
import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player 
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


#Game Loop
running = True  # Variável de controle para manter o loop do jogo rodando

# Enquanto a variável 'running' for True, o loop continuará
while running:  

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    
    # Captura todos os eventos que estão acontecendo no jogo (como cliques, teclas pressionadas, etc.)
    for event in pygame.event.get():  
        
        # Verifica se o evento capturado é o de fechar a janela (pygame.QUIT)
        if event.type == pygame.QUIT:  
            
            # Se o evento for de fechar a janela, define 'running' como False, encerrando o loop
            running = False
        
        # if keystroke is preesed check wheter its right or lft
        if event.type == pygame.KEYDOWN:
            print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()

    #38:23