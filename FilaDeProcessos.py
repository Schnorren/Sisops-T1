from collections import deque

class FilaDeProcessos:
    def __init__(self):
        self.Processo = deque()

    def adicionar_processo(self, processo):
        self.Processo.append(processo)

    def obter_proximo(self):
        return self.Processo.popleft() if self.Processo else None
