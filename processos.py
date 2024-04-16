'''Classe para representar os processos
   Versão: 2024-04-14'''

class Processo():
    def __init__(self, caminho, id):
        self.id = id
        with open(caminho, 'r') as fp:
            self.linhas = [line.strip() for line in fp.readlines()]

            if '.code' in self.linhas and '.endcode' in self.linhas:
                self._codigo = self.linhas[self.linhas.index('.code')+1:self.linhas.index('.endcode')]
            else:
                self._codigo = []

            if '.data' in self.linhas and '.enddata' in self.linhas:
                self._area_dados = self.linhas[self.linhas.index('.data')+1:self.linhas.index('.enddata')]
            else:
                self._area_dados = []

            # Área de dados em formato de dicionário
            self._dicionario_area_dados = {}

            for v in self._area_dados:

                var_val = v.split()
                nome_var = var_val[0]
                valor_var = float(var_val[1])

                self._dicionario_area_dados[nome_var] = valor_var

            # Labels
            self._labels = {}

            # Instruções em formato de dicionário
            self._instrucoes  = {}

            for ind, i in enumerate(self._codigo):
                if ':' in i:
                    label, op = i.split(':')
                    self._labels[label.strip()] = ind
                    self._instrucoes[ind] = op.strip()
                else:
                    self._instrucoes[ind] = i
            

    # Getters
    @property
    def instrucoes(self):
        return self._instrucoes
    
    @property
    def area_dados(self):
        return self._dicionario_area_dados
    
    @property
    def labels(self):
        return self._labels

