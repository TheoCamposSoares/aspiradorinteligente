# DustBusters/tests/ambientes/test_grid.py
from src.ambientes.grid import AmbienteGrid7x7

# Teste para verificar se a inicialização do ambiente está correta
def test_inicializacao():
    env = AmbienteGrid7x7(
        largura=7,
        altura=7,
        sujeiras={(1, 2)},
        obstaculos={(3, 3)}
    )
    assert env.largura == 7
    assert env.altura == 7
    assert (1, 2) in env.sujeiras
    assert (3, 3) in env.obstaculos

# Verifica se o agente é impedido de sair do grid 
def test_limites_grid():
    amb = AmbienteGrid7x7()
    assert amb.dentro_limites((0, 0))
    assert amb.dentro_limites((6, 6))
    assert not amb.dentro_limites((-1, 0))
    assert not amb.dentro_limites((7, 3))

# Testa movimentos válidos para ver se funciona
def test_movimento_sem_obstaculo():
    amb = AmbienteGrid7x7()

    nova_pos = amb.mover_posicao((0, 0), "DIREITA")
    assert nova_pos == (1, 0)

    nova_pos = amb.mover_posicao((1, 1), "CIMA")
    assert nova_pos == (1, 0)

# Verfica se o agente é impedido de colidir com obstáculos
def test_movimento_com_obstaculo():
    amb = AmbienteGrid7x7(obstaculos={(1, 0)})

    nova_pos = amb.mover_posicao((0, 0), "DIREITA")

    # A nova posição é (1,0), mas há obstáculo → sem_obstaculo deve ser False
    assert amb.sem_obstaculo(nova_pos) is False

# Verifica se a sujeira desaparece quando o agente limpa 
def test_sujeira_grid():
    amb = AmbienteGrid7x7(sujeiras={(2, 2)})

    assert (2, 2) in amb.sujeiras

    amb.executar_acao(
        agente=type("FakeAgente", (), {"posicao": (2, 2)})(),
        acao="LIMPAR"
    )

    assert (2, 2) not in amb.sujeiras

