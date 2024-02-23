# Imports.

import sys
import pygame

pygame.init()

# Configurações da Tela.

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Player", True, BRANCO)

# Posicionamento do Texto.

# text_rect = texto.get_rect(center=(largura/2, altura/2)) # Centro
# text_rect = texto.get_rect(center=(largura/2, 25)) # Parte de Cima
# text_rect = texto.get_rect(center=(400, 575)) # Parte de Baixo

# text_rect = texto.get_rect(center=(740, 300)) # Lado Direito
# text_rect = texto.get_rect(center=(55, 300)) # Lado Esquerdo

# text_rect = texto.get_rect(center=(735, 25)) # Canto Superior Direito
# text_rect = texto.get_rect(center=(55, 25)) # Canto Superior Esquerdo 

# text_rect = texto.get_rect(center=(740, 570)) # Canto Inferior Direito
# text_rect = texto.get_rect(center=(55, 570)) # Canto Inferior Esquerdo

# Loop Principal.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(PRETO)
    tela.blit(texto, text_rect)
    pygame.display.flip()