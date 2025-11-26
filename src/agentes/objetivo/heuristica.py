class HeuristicaManhattan:
    """
    Implementação da heurística Manhattan para A*.
    """

    @staticmethod
    def calcular(pos_atual, pos_objetivo):
        x1, y1 = pos_atual
        x2, y2 = pos_objetivo
        return abs(x1 - x2) + abs(y1 - y2)
