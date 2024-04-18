from FilaDeProcessos import FilaDeProcessos


class EscalonadorFCFS:
    def __init__(self):
        self.fila = FilaDeProcessos()

    def escalonar(self):
        while self.fila.Processo:
            processo = self.fila.obter_proximo()
            if processo:
                processo.estado = 'executando'
                # Simule a execução aqui, possivelmente usando sleep
                print(f'Executando processo {processo.id}')
                processo.estado = 'finalizado'
