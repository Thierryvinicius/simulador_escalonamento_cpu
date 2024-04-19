import random

def SJF(qtd):
    processos = {}
    repetido = False
    
    # Gerar processos aleatórios
    for i in range(1, qtd):  # Corrigido o intervalo para incluir qtd
        processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 
                                    'tempo_execucao': random.randint(1, 5), 
                                    'prioridade': random.randint(1, 5)}

    # Ordenar os processos pelo tempo de execução
    processos_ord = dict(sorted(processos.items(), key=lambda x: x[1]['tempo_execucao']))
    
    # Verificar se há tempos de execução repetidos
    CpuBurst = [processos[ps]['tempo_execucao'] for ps in processos]
    numeros_repetidos = [numero for numero in CpuBurst if CpuBurst.count(numero) > 1]
    repetido = bool(numeros_repetidos)

    Diagrama = []
    chaves = list(processos_ord.keys())  # Obter a lista de chaves ordenadas

    # Se houver processos com o mesmo tempo de execução
    if repetido:
        for i, processo in enumerate(chaves):
            for j in range(i + 1, len(chaves)):
                outro_processo = chaves[j]
                if processos_ord[processo]['tempo_execucao'] == processos_ord[outro_processo]['tempo_execucao']:
                    if processos_ord[processo]['tempo_chegada'] > processos_ord[outro_processo]['tempo_chegada']:
                        # Trocar as chaves
                        chaves[i], chaves[j] = chaves[j], chaves[i]
    for ps in chaves:
        for _ in range(processos_ord[ps]['tempo_execucao']):
            Diagrama.append(ps)
    ord = {}
    for ps in chaves:
        ord[ps] = processos_ord[ps]

    return processos,Diagrama,ord
