import pygame
import sys
from .ui.config import *
from .ui.telas.tela_menu import TelaMenu
from .ui.telas.tela_edicao import TelaEdicao
from .ui.telas.tela_jogo import TelaJogo
from .ui.telas.tela_fim import TelaFim

class GerenciadorJogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption(TITULO_JANELA)
        self.clock = pygame.time.Clock()
        self.rodando = True
        
        # Inicializar Telas
        self.telas = {
            ESTADO_MENU: TelaMenu(self),
            ESTADO_EDICAO: TelaEdicao(self),
            ESTADO_JOGO: TelaJogo(self),
            ESTADO_FIM: TelaFim(self)
        }
        
        self.estado_atual = ESTADO_MENU
        self.tela_atual = self.telas[ESTADO_MENU]

    def mudar_estado(self, novo_estado, **kwargs):
        self.estado_atual = novo_estado
        self.tela_atual = self.telas[novo_estado]
        if hasattr(self.tela_atual, 'configurar'):
            if kwargs:
                # Se houver kwargs, passa como argumentos nomeados ou um dict de config dependendo da assinatura
                # Simplificação: Se a tela espera 'config' ou argumentos específicos
                if 'config' in kwargs and 'config' in self.tela_atual.configurar.__code__.co_varnames:
                     self.tela_atual.configurar(kwargs['config'])
                elif 'modo' in kwargs: # Caso especifico da tela de edicao
                     self.tela_atual.configurar(kwargs['modo'])
                elif 'passos' in kwargs: # Caso especifico da tela de fim
                     self.tela_atual.configurar(kwargs['passos'])

    def sair(self):
        self.rodando = False

    def run(self):
        while self.rodando:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    self.rodando = False
            
            self.tela_atual.processar_eventos(eventos)
            self.tela_atual.atualizar()
            self.tela_atual.desenhar(self.tela)
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jogo = GerenciadorJogo()
    jogo.run()
