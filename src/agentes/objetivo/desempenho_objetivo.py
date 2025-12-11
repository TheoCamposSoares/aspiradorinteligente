class PerformanceMeasureObjetivo:
    def __init__(self,
                 reward_clean=10,
                 reward_goal=100,
                 penalty_move=1,
                 penalty_wrong_suck=2,
                 penalty_invalid_action=2):
        self.reward_clean = reward_clean
        self.reward_goal = reward_goal
        self.penalty_move = penalty_move
        self.penalty_wrong_suck = penalty_wrong_suck
        self.penalty_invalid_action = penalty_invalid_action
        self.goal_given = False

    def __call__(self, agente, acao, sucesso, estado_ambiente=None):
        recompensa = 0

        # Penalidade por movimento
        if acao in ["CIMA", "BAIXO", "ESQUERDA", "DIREITA"]:
            recompensa -= self.penalty_move

        # Recompensa por limpeza
        if acao == "Suck":
            if sucesso:
                recompensa += self.reward_clean
            else:
                recompensa -= self.penalty_wrong_suck

        # Penalidade por ação inválida (bater na parede)
        if not sucesso and acao in ["CIMA", "BAIXO", "ESQUERDA", "DIREITA"]:
            recompensa -= self.penalty_invalid_action

        # Recompensa por objetivo concluído
        if len(agente.ambiente.sujeiras) == 0 and not self.goal_given:
            recompensa += self.reward_goal
            self.goal_given = True

        return recompensa

    def reset(self):
        self.goal_given = False
