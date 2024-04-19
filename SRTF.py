import random
import copy

def srtf(qtd):
    processos = {}
    processos_ordenados = []
    processos2 = {}
    # Inicializando processos com tempos de chegada e execução aleatórios
    for i in range(1, qtd):
        processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 'tempo_execucao': random.randint(1, 5), 'prioridade': random.randint(1,5)}
    processos2 = copy.deepcopy(processos)
    tempo_atual = 0
    processos_restantes = list(processos.keys())
    diagrama = []
    while processos_restantes:
        menor_tempo = None
        processo_atual = None
        for processo in processos_restantes:
            #percorre os processos
            if processos[processo]['tempo_chegada'] <= tempo_atual:
                #verifica se o processo ja chegou
                if menor_tempo is None or processos[processo]['tempo_execucao'] < menor_tempo:
                    #inicializo a menor_tempo com o tempo de execução do processo q chegou
                    menor_tempo = processos[processo]['tempo_execucao']
                    processo_atual = processo
        
        if processo_atual is None:
            #caso nenhum processo tenha chegado, tempo_atual += 1
            tempo_atual += 1
        else: 
            #executa o algoritmo diminuindo cpu-burst a cada +1 de tempo_atual
            processos[processo_atual]['tempo_execucao'] -= 1
            tempo_atual += 1
            if processos[processo_atual]['tempo_execucao'] <= 0:
                #cpu_burst = 0, ele remove do processo
                processos_ordenados.append(processo_atual)
                processos_restantes.remove(processo_atual)   
            diagrama.append(processo_atual)  
    orq = {}
    for chave in processos_ordenados:
        orq[chave] = processos2[chave] 
    return processos2,diagrama,orq
