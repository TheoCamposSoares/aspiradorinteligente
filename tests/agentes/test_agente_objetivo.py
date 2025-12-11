from src.agentes.objetivo.agente_objetivo import AgenteBaseadoObjetivo


class AmbienteFake:
    # Simulação de ambiente apenas com o que o agente usa
    def __init__(self):
        self.grid = {}
        self.largura = 7
        self.altura = 7


def test_agente_limpa_quando_sujo():
    ambiente = AmbienteFake()
    agente = AgenteBaseadoObjetivo()
    agente.vincular_ambiente(ambiente, (2, 2))

    percepcao = {
        "estado_atual": "sujo",
        "sujeiras_visiveis": [],
        "posicoes_vizinhas": {}
    }

    acao = agente.decidir_acao(percepcao)
    assert acao == "LIMPAR"

# teste para ver se o agente planeja o caminho quendo percebe a sujeira


def test_planeja_quando_ve_sujeira(monkeypatch):
    ambiente = AmbienteFake()
    agente = AgenteBaseadoObjetivo()
    agente.vincular_ambiente(ambiente, (1, 1))

    # A* fake
    def fake_buscar(ambiente, inicio, objetivo):
        return [(2, 1), (3, 1)]  # caminho fake

    monkeypatch.setattr(agente.planejador, "buscar", fake_buscar)

    percepcao = {
        "estado_atual": "limpo",
        "sujeiras_visiveis": [(3, 1)],
        "posicoes_vizinhas": {}
    }

    acao = agente.decidir_acao(percepcao)

    # caminho deve ter sido preenchido
    assert agente.caminho_atual == [(3, 1)]
    # primeira ação deve ser seguir destino
    assert acao == "DIREITA"

# teste para ver se o agente segue o caminho quando ele existe


def test_segue_caminho():
    ambiente = AmbienteFake()
    agente = AgenteBaseadoObjetivo()
    agente.vincular_ambiente(ambiente, (1, 1))

    agente.caminho_atual = [(2, 1)]  # destino imediato

    percepcao = {
        "estado_atual": "limpo",
        "sujeiras_visiveis": [],
        "posicoes_vizinhas": {}
    }

    acao = agente.decidir_acao(percepcao)
    assert acao == "DIREITA"

# verifica se o agente explora o ambiente quando não há sujeiras imediatas


def test_explora_quando_sem_sujeiras():
    ambiente = AmbienteFake()
    agente = AgenteBaseadoObjetivo()
    agente.vincular_ambiente(ambiente, (1, 1))

    percepcao = {
        "estado_atual": "limpo",
        "sujeiras_visiveis": [],
        "posicoes_vizinhas": {
            "CIMA": True,
            "BAIXO": False,
            "ESQUERDA": False,
            "DIREITA": False
        }
    }

    acao = agente.decidir_acao(percepcao)
    assert acao == "CIMA"

# verifica se o agente não se move quando o objetivo é o mesmo lugar onde se encontra atualmente


def test_sem_movimento_quando_destino_igual():
    ambiente = AmbienteFake()
    agente = AgenteBaseadoObjetivo()
    agente.vincular_ambiente(ambiente, (2, 2))

    agente.caminho_atual = [(2, 2)]  # caminho inválido

    percepcao = {
        "estado_atual": "limpo",
        "sujeiras_visiveis": [],
        "posicoes_vizinhas": {}
    }

    acao = agente.decidir_acao(percepcao)
    assert acao is None
