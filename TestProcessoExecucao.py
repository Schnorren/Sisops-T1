import unittest

from Processo import Processo
from sistema import Sistema

class TestProcessoExecucao(unittest.TestCase):
    def setUp(self):
        # Setup para criar um processo com um arquivo de exemplo
        self.processo = Processo(id=1, caminho="teste.txt")

    def test_execucao_processo(self):
        # Simula a execução e verifica o estado final esperado
        self.processo.estado = 'executando'
        sistema = Sistema()
        sistema._tempo_real.append(self.processo)
        sistema.executa_processo(self.processo)

        # Verifica se a execução termina corretamente
        self.assertEqual(self.processo.estado, 'finalizado', "O processo não terminou corretamente.")

# Executar os testes
if __name__ == '__main__':
    unittest.main()
