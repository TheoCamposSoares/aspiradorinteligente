import pygame

# Configurações de Tela
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_JANELA = "Aspirador Inteligente"
FPS = 60

# Cores (Placeholders para futura estilização)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_CLARO = (200, 200, 200)
CINZA_ESCURO = (100, 100, 100)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
MARROM = (139, 69, 19) # Para sujeira

# Cores Específicas
COR_FUNDO = BRANCO
COR_TEXTO = PRETO
COR_BOTAO = CINZA_CLARO
COR_BOTAO_HOVER = CINZA_ESCURO
COR_GRID_LINHA = PRETO
COR_AGENTE = AZUL
COR_SUJEIRA = MARROM
COR_PAREDE = PRETO

# Configurações do Grid
TAMANHO_CELULA = 60  # Tamanho em pixels de cada célula do grid
MARGEM_GRID = 20     # Margem ao redor do grid

# Estados do Jogo
ESTADO_MENU = "menu"
ESTADO_EDICAO = "edicao"
ESTADO_JOGO = "jogo"
ESTADO_FIM = "fim"
