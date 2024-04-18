from FilaDeProcessos import FilaDeProcessos


class EscalonadorRR:
    def __init__(self, quantum):
        self.quantum = quantum
        self.filas = {
            0: FilaDeProcessos(),  # Alta prioridade
            1: FilaDeProcessos()   # Baixa prioridade
        }

    def adicionar_processo(self, processo):
        self.filas[processo.prioridade].adicionar_processo(processo)

    def escalonar(self):
        for _, fila in self.filas.items():
            while fila.Processo:
                processo = fila.obter_proximo()
                if processo:
                    processo.estado = 'executando'
                    # Execute por um quantum de tempo ou até a conclusão
                    print(f'Executando processo {processo.id} por {self.quantum} unidades de tempo')
                    processo.estado = 'finalizado'
