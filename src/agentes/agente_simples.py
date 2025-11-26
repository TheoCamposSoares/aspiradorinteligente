from .base_agent import AgenteBase

class SimpleReflexAgent(AgenteBase):

    def decidir_acao(self, percepcao):
        location, dirty_here = percepcao
        if dirty_here:
            return "Suck"
        elif location == "A":
            return "Right"
        elif location == "B":
            return "Left"