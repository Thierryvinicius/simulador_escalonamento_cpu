import random

def FCFS():
    processos = {}
    processos_ordenados = []

    for i in range(1, 5):
        processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 'tempo_execucao': random.randint(1, 5), 'prioridade': random.randint(1,5)}

    processos_ordenados = sorted(processos.items(), key=lambda x: x[1]['tempo_chegada'])

    diagrama = []


    for processo, info in processos_ordenados:
        for _ in range(info['tempo_execucao']):
            diagrama.append(processo)

    return processos, diagrama

# Teste do FCFS corrigido
processos_fcfs, diagrama_fcfs = FCFS()
print("Processos FCFS:", processos_fcfs)
print("Diagrama FCFS:", diagrama_fcfs)
