from instrucoes import *
from Processo import Processo
'''Classe do sistema operacional que coordena a execução dos processos
   Versão: 2024-04-15'''

class Sistema():
    def __init__(self,):
        self._tempo_real = []
        self._melhor_esforco = []
        self.__cont = 0 # Conta número de processos
        print('--### Ambiente inicializado ###--')
    
    def cria_processo(self):
        caminho = input('Insira o código (arquivo .txt) do processo:')
        self._tempo_real.append(Processo(caminho,self.__cont))
        self.__cont+=1
    
    def executa_processo(self, p1):
        pc = 0 # inicia o ponteiro de execução em 0
        instrucoes = p1.instrucoes
        dados = p1.area_dados
        acc = None
        while True:
            operacao = instrucoes[pc]
            if operacao == 'SYSCALL 0':
                print('PROCESSO ENCERRADO')
                break
            elif operacao == 'SYSCALL 1':
                print(acc)
                pc+=1
            elif 'ADD' in operacao:
                print('ADD')
                acc = ADD(acc, operacao, dados)
                pc+=1
            elif 'SUB' in operacao:
                print('SUB')
                acc = SUB(acc, operacao, dados)
                pc+=1
            elif 'MULT' in operacao:
                print('MULT')
                acc = MULT(acc, operacao, dados)
                pc+=1
            elif 'DIV' in operacao:
                print('DIV')
                acc = DIV(acc, operacao, dados)
                pc+=1
            elif 'LOAD' in operacao:
                print('LOAD')
                acc = LOAD(acc,operacao, dados)
                print(f'ACC: {acc}')
                pc+=1
            elif 'STORE' in operacao:
                print('STORE')
                dados = STORE(acc, operacao, dados)
            elif 'BRANY' in operacao:
                print('BRANY')
                pc = BRANY(operacao)
            elif 'BRPOS' in operacao:
                print('BRPOS')
                pc = BRPOS(pc, acc, operacao.split()[1], p1.labels)
            elif 'BRZERO' in operacao:
                print('BRZERO')
                pc = BRZERO(pc, acc, operacao.split()[1], p1.labels)
            elif 'BRNEG' in operacao:
                print('BRNEG')
                pc = BRNEG(pc, acc, operacao.split()[1], p1.labels)
    
    # Getters
    @property
    def tempo_real(self):
        return self._tempo_real
    
    @property
    def melhor_esforco(self):
        return self._melhor_esforco
    


            

        
            



