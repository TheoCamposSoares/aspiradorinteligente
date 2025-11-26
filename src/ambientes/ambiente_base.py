from abc import ABC, abstractmethod

class AmbienteBase(ABC):

    def __init__(self):
        self.agente = None

    # Conecta o agente ao ambiente
    def registrar_agente(self, agente, posicao_inicial):
        self.agente = agente
        agente.vincular_ambiente(self, posicao_inicial)

    # MÉTODOS ABSTRATOS ESSENCIAIS PARA AMBOS

    @abstractmethod
    def obter_percepcao(self, posicao):
        """
        Retorna a percepção no formato esperado pelo agente específico
        que está interagindo com este ambiente.
        """
        pass

    @abstractmethod
    def executar_acao(self, agente, acao):
        """
        Executa a ação do agente e retorna True/False indicando sucesso.
        """
        pass

    @abstractmethod
    def estado_objetivo(self):
        """
        Retorna True quando o ambiente atingiu o objetivo global.
        (Ex: todas as salas limpas ou todo o grid limpo)
        """
        pass