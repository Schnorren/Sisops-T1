class Processo:
    def __init__(self, id, caminho=None, tempo_chegada=0, duracao=0, tipo='melhor_esforco', prioridade=None):
        self.id = id
        self.tempo_chegada = tempo_chegada
        self.duracao = duracao
        self.tipo = tipo  # 'tempo_real' ou 'melhor_esforco'
        self.prioridade = prioridade
        self.estado = 'pronto'  # pode ser 'pronto', 'executando', 'bloqueado', 'finalizado'
        self._codigo = []
        self._area_dados = []
        self._dicionario_area_dados = {}
        self._labels = {}
        self._instrucoes = {}

        if caminho:
            self.carregar_arquivo(caminho)
    
    def carregar_arquivo(self, caminho):
        with open(caminho, 'r') as fp:
            linhas = [line.strip() for line in fp.readlines()]

            if '.code' in linhas and '.endcode' in linhas:
                self._codigo = linhas[linhas.index('.code') + 1:linhas.index('.endcode')]
            if '.data' in linhas and '.enddata' in linhas:
                self._area_dados = linhas[linhas.index('.data') + 1:linhas.index('.enddata')]

            for v in self._area_dados:
                var_val = v.split()
                nome_var = var_val[0]
                valor_var = float(var_val[1])
                self._dicionario_area_dados[nome_var] = valor_var

            for ind, i in enumerate(self._codigo):
                if ':' in i:
                    label, op = i.split(':')
                    self._labels[label.strip()] = ind
                    self._instrucoes[ind] = op.strip()
                else:
                    self._instrucoes[ind] = i

    @property
    def instrucoes(self):
        return self._instrucoes

    @property
    def area_dados(self):
        return self._dicionario_area_dados

    @property
    def labels(self):
        return self._labels
