from abc import ABC, abstractmethod

class AgenteBase(ABC):

    def __init__(self, max_passos=100, func_desempenho=None):
        self.max_passos = max_passos
        self.func_desempenho = func_desempenho
        self.passos = 0
        self.ambiente = None
        self.posicao = None

    # Vincula o agente ao ambiente e define posição inicial
    def vincular_ambiente(self, ambiente, posicao_inicial):
        self.ambiente = ambiente
        self.posicao = posicao_inicial

    # Retorna a percepção atual do ambiente
    def perceber(self):
        return self.ambiente.obter_percepcao(self.posicao)

    # Age no ambiente
    def agir(self, acao):
        self.passos += 1
        return self.ambiente.executar_acao(self, acao)

    # Reseta a contagem de passos
    def resetar(self):
        self.passos = 0

    @abstractmethod
    # Decide a ação do agente baseado na percepcao
    def decidir_acao(self, percepcao):
        pass