from src.agentes.simples.agente_simples import SimpleReflexAgent


class AmbienteFake:
    # Ambiente mínimo apenas para testar o agente simples.

    def __init__(self, estado_inicial):
        self.estado = estado_inicial
        self.registro_acoes = []

    def obter_percepcao(self, posicao):
        # Retorna (location, dirty_here)
        return (posicao, self.estado[posicao])

    def executar_acao(self, agente, acao):
        self.registro_acoes.append((agente.posicao, acao))

        if acao == "Suck":
            self.estado[agente.posicao] = False
            return True, {"nova_posicao": agente.posicao}

        if agente.posicao == "A" and acao == "Right":
            return True, {"nova_posicao": "B"}

        if agente.posicao == "B" and acao == "Left":
            return True, {"nova_posicao": "A"}

        return False, {"nova_posicao": agente.posicao}


def test_limpa_se_sujo():
    ambiente = AmbienteFake({"A": True, "B": False})
    agente = SimpleReflexAgent()
    agente.vincular_ambiente(ambiente, "A")

    percepcao = agente.perceber()
    acao = agente.decidir_acao(percepcao)

    assert acao == "Suck"


def test_para_direita_se_limp0_em_A():
    ambiente = AmbienteFake({"A": False, "B": False})
    agente = SimpleReflexAgent()
    agente.vincular_ambiente(ambiente, "A")

    percepcao = agente.perceber()
    acao = agente.decidir_acao(percepcao)

    assert acao == "Right"


def test_para_esquerda_se_limpo_em_B():
    ambiente = AmbienteFake({"A": False, "B": False})
    agente = SimpleReflexAgent()
    agente.vincular_ambiente(ambiente, "B")

    percepcao = agente.perceber()
    acao = agente.decidir_acao(percepcao)

    assert acao == "Left"
