'''Módulo para as instruções
   Versão: 2024-04-14'''

### Instruções Aritméticas ###

def ADD(acc, op1, dados = {}):
    if '#' in op1: # Imediato
        acc+= float(op1.split()[1][1:])
    else: # Direto
        acc+= float(dados[op1])
    return acc

def SUB(acc, op1, dados = {}):
    if '#' in op1: # Imediato
        acc-= float(op1.split()[1][1:])
    else: # Direto
        acc-= float(dados[op1.split()[1]])
    return acc

def MULT(acc, op1, dados = {}):
    if '#' in op1: # Imediato
        acc*= float(op1.split()[1][1:])
    else: # Direto
        acc*= float(dados[op1])
    return acc

def DIV(acc, op1, dados = {}):
    if '#' in op1: # Imediato
        acc/= float(op1[1:])
    else: # Direto
        acc/= float(dados[op1.split()[1]])
    return acc

### Instruções de Memória ###

def LOAD(acc, op1, dados = {}):
    if '#' in op1: # Imediato
        acc= float(op1[1:])
    else: # Direto
        acc= float(dados[op1.split()[1]])
    return acc

def STORE(acc, op1, dados):
    dados[op1] = acc
    return dados
        
### Instruções de Salto ###

def BRANY(l, labels):
    return labels[l]

def BRPOS(pc, acc, l, labels):
    if acc > 0:
        return labels[l]
    return pc+1

def BRZERO(acc, pc, l, labels):
    if acc == 0:
        return labels[l]
    return pc+1

def BRNEG(acc, pc, l, labels):
    if acc < 0:
        return labels[l]
    return pc+1