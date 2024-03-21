# Imports.

import pygame
import sys

# Configurações iniciais, variaveis e definições.

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Crazy Ping Pong")

# Definição das propriedades da raquete.

raq_lar = 10
raq_alt = 60
tam_bola = 10

# Posição da raquete do PC.

pc_x = 10
pc_y = altura // 2 - raq_alt // 2

# Pocição da raquete do Player.

player1_x = largura - 20  # Aqui é 20 pois o tamanho da raquete ja é 10, então adicionamos + 10, por isso diminuimos 20, e não 10.
player1_y = altura // 2 - raq_alt // 2

# Posição da bola.

bola_x = largura // 2 - tam_bola // 2
bola_y = altura // 2 - tam_bola // 2

# Velocidade da raquete.

raq_pl1_dy = 5
raq_pc_dy = 5

clock = pygame.time.Clock()

# Mecânica do Loop Infinito.

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.fill(PRETO)

    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raq_lar,raq_alt))             # Desenhando a raquete esquerda.
    pygame.draw.rect(screen, BRANCO, (player1_x, player1_y, raq_lar, raq_alt))  # Desenhando a raquete direita.
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tam_bola, tam_bola))   # Desenhando a bola.

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player1_y > 0:
        player1_y -= raq_pl1_dy
    if keys[pygame.K_DOWN] and player1_y < altura - raq_alt:
        player1_y += raq_pl1_dy

    pygame.display.flip()

    clock.tick(120)

    

pygame.quit()
sys.exit()

