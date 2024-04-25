# Imports.

import random
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

# Velocidade da raquete.

raq_pl1_dy = 5  # dy significa velocidade
raq_pc_dy = 5

# Velocidade da bola.

velocidade_bx = 3
velocidade_by = 3

# Definir vencedor.

vencedor = ""

# Definir Controle.

rodando = True
controle = False

# Configuração da fonte.

font_file = "crazy-ping-pong/font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 20)

# Taxa de quadros.

clock = pygame.time.Clock()

# Criando o Menu do Jogo

def menu_principal():
    global rodando, controle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    return

        # Renderiza o texto do menu.
                    
        screen.fill(PRETO)
        texto_menu = font.render("Ping Pong", True, BRANCO)
        texto_menu_rect = texto_menu.get_rect(center=(largura // 2, altura // 2))   
        screen.blit(texto_menu, texto_menu_rect)

        tempo = pygame.time.get_ticks()

        # Pressione espaço para jogar.

        if tempo % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, BRANCO)
            texto_iniciar_rect = texto_menu.get_rect(center=(325, 400))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        pygame.display.flip()

# Posição Inicioal das variaveis.

def posicao_inicial():
    global pc_x, pc_y, player1_x, player1_y, bola_x, bola_y, score_pc, score_player1

    # Posição da raquete do PC.

    pc_x = 10
    pc_y = altura // 2 - raq_alt // 2

    # Pocição da raquete do Player.

    player1_x = largura - 20  # Aqui é 20 pois o tamanho da raquete ja é 10, então adicionamos + 10, por isso diminuimos 20, e não 10.
    player1_y = altura // 2 - raq_alt // 2

    # Posição da bola.

    bola_x = largura // 2 - tam_bola // 2
    bola_y = altura // 2 - tam_bola // 2

    # Define o Score (Pontuação).

    score_player1 = 0
    score_pc = 0
    
# Fim do jogo

def fim_jogo():
    global rodando, vencedor, controle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    posicao_inicial()
                    rodando = True
                    return
                
        # Renderiza o Texto do Menu.

        screen.fill(PRETO)
        texto_fim = font.render(f"Vencedor: {vencedor}", True, BRANCO)
        texto_fim_rect = texto_fim.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_fim, texto_fim_rect)

        pygame.display.flip()    
    
menu_principal()
posicao_inicial()

# Mecânica do Loop Infinito.

while rodando:
    if not controle:
        fim_jogo()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        screen.fill(PRETO)

        # Movendo a bola.

        bola_x += velocidade_bx
        bola_y += velocidade_by

        # Retângulos de colisão.

        bola_rect = pygame.Rect(bola_x, bola_y, tam_bola, tam_bola)
        raq_pc_rect = pygame.Rect(pc_x, pc_y, raq_lar, raq_alt)
        raq_player1_rect = pygame.Rect(player1_x, player1_y, raq_lar, raq_alt)
        
        # Colisão da bola com a raquete do pc e a raquete do player.

        if bola_rect.colliderect(raq_pc_rect) or bola_rect.colliderect(raq_player1_rect):
            velocidade_bx = - velocidade_bx

        # Colisão da bola com as bordas da tela.
        
        if bola_y <= 0 or bola_y >= altura - tam_bola:
            velocidade_by = - velocidade_by
        
        # Posicionar a bola no inicio do jogo.
            
        if bola_x <= 0:
            bola_x = largura // 2 - tam_bola // 2
            bola_y = altura // 2 - tam_bola // 2
            velocidade_bx = - velocidade_bx
            score_player1 += 1
            print(f"Score Player1: {score_player1}")
            if score_player1 == 5:
                print("Player_1 ganhou!")
                vencedor = "Player 1"
                fim_jogo()
        
        if bola_x >= largura - tam_bola:
            bola_x = largura // 2 - tam_bola // 2
            bola_y = altura // 2 - tam_bola // 2
            velocidade_bx = - velocidade_bx
            score_pc += 1
            print(f"Score PC: {score_pc}")
            if score_pc == 5:
                print("PC ganhou!")
                vencedor = "PC"
                fim_jogo()

        # Movendo a raquete do PC para seguir a bola.
            
        if pc_y + raq_alt // 2 < bola_y:
            pc_y += raq_pc_dy
        elif pc_y + raq_alt // 2 > bola_y:
            pc_y -= raq_pc_dy
        
        # Evitar que a raquete do PC saia da área.
        
        if pc_y < 0:
            pc_y = 0
        elif pc_y > altura - raq_alt:
            pc_y = altura - raq_alt

        # Mostrando o Score do Jogo.

        fonte_score = pygame.font.Font(font_file, 16)        
        score_texto = font.render(
            f"Score PC: {score_pc}        Score Player1: {score_player1}", True, BRANCO
        )
        score_rect = score_texto.get_rect(center=(largura // 2, 30))

        screen.blit(score_texto, score_rect)

        # Deixando a raquete do player automatica.
            
        # if player1_y + raq_alt // 2 < bola_y:
        #    player1_y += raq_pl1_dy
        # elif player1_y + raq_alt // 2 > bola_y:
        #    player1_y -= raq_pl1_dy
        
        # Evitar que a raquete do player saia da área.

        # if player1_y < 0:
        #    player1_y = 0
        # elif player1_y > altura - raq_alt:
        #    player1_y = altura - raq_alt

        # Deixando o movimento das raquetes aleatório.

        pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raq_lar,raq_alt))                   # Desenhando a raquete esquerda.
        pygame.draw.rect(screen, BRANCO, (player1_x, player1_y, raq_lar, raq_alt))        # Desenhando a raquete direita.
        pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tam_bola, tam_bola))         # Desenhando a bola.
        pygame.draw.aaline(screen, BRANCO, (largura // 2, 0), (largura // 2, altura))     # Desenhando a linha do meio

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and player1_y > 0:
            player1_y -= raq_pl1_dy
        if keys[pygame.K_DOWN] and player1_y < altura - raq_alt:
            player1_y += raq_pl1_dy

        pygame.display.flip()

        clock.tick(60)

#fim_jogo()
pygame.quit()
sys.exit()