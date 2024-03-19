# Imports.

import pygame
import sys

from mecmov import MovText

# Definições da classe, onde serão declaradas seus atributos e métodos, e suas variaveis que vão ser usadas para a lógica,
# alguns: largura, altura, tela, taxa de dados, um objeto MovText (que vem da classe movendo texto (arquivo mecmov.)).

class Game:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Bate-Bate")
        self.clock = pygame.time.Clock()
        self.MovText = MovText("PLAYER", 50, self.largura, self.altura)

    def run(self):
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self.MovText.move()
            self.tela.fill((0, 0, 0))
            self.tela.blit(self.MovText.texto_surf, self.MovText.rect)
            pygame.display.flip()
            self.clock.tick(320)

        pygame.quit()
        sys.exit()