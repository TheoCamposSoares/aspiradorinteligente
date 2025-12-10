class PerformanceMeasureCorrigida:
    # Penaliza movimentos e recompensa limpeza

    def __init__(self, move_penalty=1, suck_reward=1):
        self.move_penalty = move_penalty
        self.suck_reward = suck_reward
        self.limpeza_total_ja_recompensada = False

    def __call__(self, agente, acao, sucesso, estado_ambiente=None):
        recompensa = 0.0

        # Penaliza passos
        if acao in ("Left", "Right"):
            recompensa -= self.move_penalty 

        # Recompensa limpeza
        if acao == "Suck" and sucesso:
            recompensa += self.suck_reward 
            