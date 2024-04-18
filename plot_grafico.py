###########################################################################
#QUASE PERFEITO O DE BAIXO!!
############################################################################

# import matplotlib.pyplot as plt
# from SRTF import srtf

# def geraValor(processos, operador):
#     if operador == 'FCFS':
#         processos_ordenados = sorted(processos.items(), key=lambda x: x[1]['tempo_chegada'])
#     elif operador == 'SJF':
#         processos_ordenados = sorted(processos.items(), key=lambda x: x[1]['tempo_execucao'])
#     elif operador == 'SRTF':
#         processos, diagrama = srtf(len(processos))
#         plot_gantt(processos, diagrama, "SRTF")
#         return
#     else:
#         # Defina a lógica para outras políticas de escalonamento
#         pass

#     if operador in ['FCFS', 'SJF']:
#         processos_ordenados = [proc[0] for proc in processos_ordenados]  # Apenas pegando as chaves dos processos ordenados
#         tempo_conclusao = calcula_tempo_conclusao(processos, processos_ordenados)
#         plot_gantt(processos_ordenados, tempo_conclusao, operador)

# def calcula_tempo_conclusao(processos, processos_ordenados):
#     tempo_conclusao = []
#     current_time = 0

#     for proc in processos_ordenados:
#         current_time += processos[proc]['tempo_execucao']
#         tempo_conclusao.append(current_time)

#     return tempo_conclusao

# def plot_gantt(processos, tempo_conclusao, operador):
#     fig, gnt = plt.subplots()

#     gnt.set_xlabel('Tempo')
#     gnt.set_ylabel('Processos')

#     max_conclusao = max(tempo_conclusao)
#     if isinstance(max_conclusao, int):
#         max_conclusao = max_conclusao + 3
#     else:
#         max_conclusao = max_conclusao[0] + 3

#     gnt.set_xticks(range(0, max_conclusao + 1, 1))
    
#     # Mapeamento de processos para posições únicas no eixo y
#     processos_map = {proc: i for i, proc in enumerate(processos)}
#     gnt.set_yticks([i + 0.5 for i in range(len(processos))])
#     gnt.set_yticklabels([str(proc) for proc in processos])
    
#     for proc, tempo in zip(processos, tempo_conclusao):
#         gnt.broken_barh([(0, tempo)], (processos_map[proc], 0.5), facecolors=('tab:blue'), edgecolor='black')
#         gnt.text(tempo/2, processos_map[proc] + 0.25, str(tempo), ha='center', va='center', color='white')

#     gnt.set_ylim(0, len(processos))
#     gnt.set_xlim(0, max_conclusao)

#     if operador == 'FCFS':
#         plt.title('Gráfico de Gantt (FCFS)')
#     elif operador == 'SJF':
#         plt.title('Gráfico de Gantt (SJF)')
#     else:
#         plt.title('Gráfico de Gantt (SRTF)')
#     plt.grid(True)
#     plt.show()

# # TESTE
# processos = {
#     'P1': {'tempo_chegada': 0, 'tempo_execucao': 3},
#     'P2': {'tempo_chegada': 2, 'tempo_execucao': 4},
#     'P3': {'tempo_chegada': 4, 'tempo_execucao': 2}
# }

# geraValor(processos, 'SJF')
###############################################################

import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict
from SRTF import srtf

def geraValor(processos, operador):
    if operador == 'FCFS':
        processos_ord = {}
        processos_ordenados = (sorted(processos.items(), key=lambda x: x[1]['tempo_chegada']))
        for ps in processos_ordenados:
            processos_ord[ps[0]] = ps[1]
        tempo_conclusao = calcula_tempo_conclusao(processos_ordenados)
        plot_gantt_fcfs(processos_ord, tempo_conclusao)
    # elif operador == 'SJF':
    #     processos_ordenados = sorted(processos.items(), key=lambda x: x[1]['tempo_execucao'])
    #     tempo_conclusao = calcula_tempo_conclusao(processos_ordenados)
    #     plot_gantt_sjf(processos, tempo_conclusao)
    elif operador == 'SRTF':
        processos, diagrama = srtf(len(processos))
        tempo_conclusao = calcula_tempo_conclusao_srtf(processos, diagrama)
        plot_gantt_srtf(processos, diagrama, tempo_conclusao)

    else:
        # Defina a lógica para outras políticas de escalonamento
        pass

def calcula_tempo_conclusao(processos_ordenados):
    tempo_conclusao = []
    current_time = 0

    for _, info in processos_ordenados:
        current_time = max(current_time, info['tempo_chegada']) + info['tempo_execucao']
        tempo_conclusao.append(current_time)

    return tempo_conclusao

def calcula_tempo_conclusao_srtf(processos, diagrama):
    tempo_conclusao = {proc: 0 for proc in processos}
    for i, proc in enumerate(diagrama):
        tempo_conclusao[proc] = i + 1  # Adiciona 1 porque o índice começa em 0
    return tempo_conclusao

def plot_gantt_fcfs(processos, tempo_conclusao):
    fig, gnt = plt.subplots()

    gnt.set_xlabel('Tempo')
    gnt.set_ylabel('Processos')

    max_conclusao = max(tempo_conclusao)
    if isinstance(max_conclusao, int):
        max_conclusao = max_conclusao + 5
    else:
        max_conclusao = max_conclusao[0] + 5

    gnt.set_xticks(range(0, max_conclusao + 1, 1))
    
    # Mapeamento de processos para posições únicas no eixo y
    processos_map = {proc: i for i, proc in enumerate(processos)}
    gnt.set_yticks([i + 0.5 for i in range(len(processos))])
    gnt.set_yticklabels([str(proc) for proc in processos])

    # Gerar cores únicas para cada processo
    cores = plt.cm.tab10(np.linspace(0, 1, len(processos)))

    tempo_corrente = 0
    # Adicionar barras para cada processo
    print(tempo_conclusao)
    
    for i, proc in enumerate(processos):
        start_time = max(tempo_corrente, processos[proc]['tempo_chegada'])
        for j, tempo in enumerate(tempo_conclusao):
            if tempo == start_time + processos[proc]['tempo_execucao']:
                gnt.broken_barh([(start_time, processos[proc]['tempo_execucao'])], (processos_map[proc], 0.5), facecolors=[cores[i]], edgecolor='black')
                gnt.text(start_time + (tempo - start_time) / 2, processos_map[proc] + 0.25, proc, ha='center', va='center', color='white')
                tempo_corrente = tempo
                break
            #start_time = max(start_time, tempo)  # O próximo processo só pode começar após o término do processo atual
    
    gnt.set_ylim(0, len(processos))
    gnt.set_xlim(0, max_conclusao)
    plt.title('Gráfico de Gantt (FCFS)')
    plt.grid(True)
    plt.show()

# Função para plotar o gráfico de Gantt para o algoritmo SJF

# Função para plotar o gráfico de Gantt para o algoritmo SRTF
def plot_gantt_srtf(processos, diagrama, tempo_conclusao):
    fig, gnt = plt.subplots()

    gnt.set_xlabel('Tempo')
    gnt.set_ylabel('Processos')

    max_conclusao = max(tempo_conclusao.values()) + 5

    gnt.set_xticks(range(0, max_conclusao + 1, 1))
    
    # Mapeamento de processos para posições únicas no eixo y
    processos_map = {proc: i for i, proc in enumerate(processos)}
    gnt.set_yticks([i + 0.5 for i in range(len(processos))])
    gnt.set_yticklabels([str(proc) for proc in processos])

    # Gerar cores únicas para cada processo
    cores = plt.cm.tab10(np.linspace(0, 1, len(processos)))

    # Adicionar barras para cada processo
    for proc in diagrama:
        start_time = max(0, processos[proc]['tempo_chegada'])
        for i, tempo in enumerate(proc):
            if tempo == start_time + 1:
                gnt.broken_barh([(start_time, 1)], (processos_map[proc], 0.5), facecolors=[cores[i]], edgecolor='black')
                gnt.text(start_time + 0.5, processos_map[proc] + 0.25, proc, ha='center', va='center', color='white')
            start_time += 1

    gnt.set_ylim(0, len(processos))
    gnt.set_xlim(0, max_conclusao)
    plt.title('Gráfico de Gantt (SRTF)')
    plt.grid(True)
    plt.show()
# processos = {
#     'P1': {'tempo_chegada': 0, 'tempo_execucao': 3},
#     'P2': {'tempo_chegada': 2, 'tempo_execucao': 4},
#     'P3': {'tempo_chegada': 4, 'tempo_execucao': 2}
# }

# geraValor(processos, 'SJF')