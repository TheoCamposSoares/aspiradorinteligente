import pygame
from ..config import *
from ..componentes import Botao
from ...simulacao.engine import SimulationEngine

class TelaJogo:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.engine = None
        self.timer_passo = 0
        self.DELAY_PASSO = 200 # ms
        
        self.offset_x = 0
        self.offset_y = 0

    def configurar(self, config):
        self.engine = SimulationEngine(config)
        
        # Recalcular offsets para centralizar
        grid_largura = self.engine.grid_size[0] * TAMANHO_CELULA
        grid_altura = self.engine.grid_size[1] * TAMANHO_CELULA
        self.offset_x = (LARGURA_TELA - grid_largura) // 2
        self.offset_y = (ALTURA_TELA - grid_altura) // 2
        
        self.timer_passo = pygame.time.get_ticks()

    def processar_eventos(self, eventos):
        pass # Usuário apenas assiste

    def atualizar(self):
        if self.engine.finalizado:
            self.gerenciador.mudar_estado(ESTADO_FIM, passos=self.engine.passos)
            return

        agora = pygame.time.get_ticks()
        if agora - self.timer_passo > self.DELAY_PASSO:
            self.timer_passo = agora
            self.engine.executar_passo()

    def desenhar(self, superficie):
        superficie.fill(COR_FUNDO)
        
        # Desenhar Grid e Estado Atual
        for x in range(self.engine.grid_size[0]):
            for y in range(self.engine.grid_size[1]):
                rect = pygame.Rect(
                    self.offset_x + x * TAMANHO_CELULA,
                    self.offset_y + y * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA
                )
                pygame.draw.rect(superficie, COR_GRID_LINHA, rect, 1)
                
                is_dirty = False
                is_wall = False
                is_agent = False
                
                if self.engine.modo == "simples":
                    loc = "A" if x == 0 else "B"
                    is_dirty = self.engine.ambiente.estado_sujeira[loc]
                    is_agent = (self.engine.agente.posicao == loc)
                else:
                    # Modo Grid
                    is_dirty = (x, y) in self.engine.ambiente.sujeiras
                    is_wall = (x, y) in self.engine.ambiente.obstaculos
                    is_agent = (self.engine.agente.posicao == (x, y))

                if is_dirty:
                    pygame.draw.circle(superficie, COR_SUJEIRA, rect.center, TAMANHO_CELULA // 4)
                if is_wall:
                    pygame.draw.rect(superficie, COR_PAREDE, rect)
                if is_agent:
                    # Desenhar agente (círculo azul ou aspirador)
                    pygame.draw.circle(superficie, COR_AGENTE, rect.center, TAMANHO_CELULA // 3)

        # HUD
        fonte = pygame.font.SysFont(None, 36)
        texto_passos = fonte.render(f"Passos: {self.engine.passos}", True, COR_TEXTO)
        superficie.blit(texto_passos, (20, 20))
