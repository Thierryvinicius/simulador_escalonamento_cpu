import random

def FCFS(qtd):
    processos = {}
    processos_ordenados = []
    orq = None
    for i in range(1, qtd):
        processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 'tempo_execucao': random.randint(1, 5), 'prioridade': random.randint(1,5)}

    processos_ordenados = dict(sorted(processos.items(), key=lambda x: x[1]['tempo_chegada']))

    diagrama = []

    for ps in processos_ordenados:
        for i in range(processos_ordenados[ps]['tempo_execucao']):
            diagrama.append(ps)

    return processos,diagrama,processos_ordenados