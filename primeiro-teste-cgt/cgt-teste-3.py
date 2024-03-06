# Imports.

import sys
import pygame
import random

pygame.init()

# Configurações da Tela.

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("ANTEDEGUEMON", True, BRANCO)

# Posicionamento do Texto.

texto_rect = texto.get_rect(center=(largura/2, altura/2)) # Centro

clock = pygame.time.Clock() 

# velocidade_x = 1
# velocidade_y = 1

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

# texto_rect = texto.get_rect(center=(largura/2, 25)) # Parte de Cima
# texto_rect = texto.get_rect(center=(400, 575)) # Parte de Baixo

# texto_rect = texto.get_rect(center=(740, 300)) # Lado Direito
# texto_rect = texto.get_rect(center=(55, 300)) # Lado Esquerdo

# texto_rect = texto.get_rect(center=(735, 25)) # Canto Superior Direito
# texto_rect = texto.get_rect(center=(55, 25)) # Canto Superior Esquerdo 

# texto_rect = texto.get_rect(center=(740, 570)) # Canto Inferior Direito
# texto_rect = texto.get_rect(center=(55, 570)) # Canto Inferior Esquerdo

# Posicionamento Avançado.

# texto_rect = texto.get_rect() # Função.

# Canto Superior Esquerdo
# texto_rect.left = 0
# texto_rect.top = 0

# Canto Inferior Esquerdo
# texto_rect.left = 0
# texto_rect.bottom = 600

# Canto Superior Direito
# texto_rect.right = 800
# texto_rect.top = 0

# Canto Inferior Direito
# texto_rect.right = 800
# texto_rect.bottom = 600

# Loop Principal.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x

    texto_rect.y += velocidade_y

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("ANTEDEGUEMON", True, AZUL)

    if texto_rect.bottom >= altura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("ANTEDEGUEMON", True, VERMELHO)

    if texto_rect.left <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("ANTEDEGUEMON", True, VERDE)

    if texto_rect.top <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("ANTEDEGUEMON", True, AMARELO)

    clock.tick(250)
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()