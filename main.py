# import pygame
import pygame

#import random
import random

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Define o título e o ícone da janela
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')  # Carrega a imagem do ícone
pygame.display.set_icon(icon)  # Define o ícone da janela

# Jogador
playerImg = pygame.image.load('player.png')  # Carrega a imagem do jogador
playerX = 370  # Posição inicial do jogador no eixo X
playerY = 480  # Posição inicial do jogador no eixo Y
playerX_change = 0  # Variável para controlar a mudança na posição X do jogador

#Inimigo
enemyImg = pygame.image.load('enemy.png')  
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0   

# Função para desenhar o jogador na tela
def player(x, y):
    screen.blit(playerImg, (x, y))  # Desenha o jogador na posição (x, y)

# Função para desenhar o inimigo na tela
def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # Desenha o inimigo na posição (x, y)

# Loop do jogo
running = True  # Variável de controle para manter o loop do jogo rodando

# Enquanto a variável 'running' for True, o loop continuará
while running:  

    # Preenche a tela com a cor preta (RGB - Red, Green, Blue)
    screen.fill((0, 0, 0))
    
    # Captura todos os eventos que estão acontecendo no jogo (como cliques, teclas pressionadas, etc.)
    for event in pygame.event.get():  
        
        # Verifica se o evento capturado é o de fechar a janela (pygame.QUIT)
        if event.type == pygame.QUIT:  
            
            # Se o evento for de fechar a janela, define 'running' como False, encerrando o loop
            running = False
        
        # Verifica se uma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            print("Uma tecla foi pressionada")
            
            # Se a tecla pressionada for a seta para a esquerda, move o jogador para a esquerda
            if event.key == pygame.K_LEFT:
                playerX_change = -1.0
            
            # Se a tecla pressionada for a seta para a direita, move o jogador para a direita
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.0
        
        # Verifica se uma tecla foi solta
        if event.type == pygame.KEYUP:
            
            # Se a tecla solta for a seta para a esquerda ou direita, para o movimento do jogador
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Atualiza a posição do jogador no eixo X
    playerX += playerX_change

    #limite de borda left e right
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    # Chama a função para desenhar o jogador na nova posição
    player(playerX, playerY)

    # Chama a função para desenhar o inimigo na nova posição
    enemy(enemyX, enemyY)
    
    # Atualiza a tela
    pygame.display.update()