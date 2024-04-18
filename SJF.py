# import random

# def SJF(qtd):
#     processos = {}
#     repetido = False
#     for i in range(1, qtd):
#         processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 'tempo_execucao': random.randint(1, 5), 'prioridade': random.randint(1,5)}


#     processos_ordenados = dict(sorted(processos.items(), key=lambda x: x[1]['tempo_execucao']))
#     CpuBurst = []

#     for ps in processos_ordenados:
#         CpuBurst.append(processos_ordenados[ps]['tempo_execucao'])
#     numeros_repetidos = []
#     for numero in CpuBurst:
#         if CpuBurst.count(numero) > 1 and numero not in numeros_repetidos:
#             numeros_repetidos.append(numero)
#             repetido = True
   
#     Diagrama = []
   
#     if repetido == True:
       
#         listaFinal =[]
       
#         for number in numeros_repetidos:
#             listaTemp = []
#             for ps in processos_ordenados:
#                 if processos_ordenados[ps]['tempo_execucao'] == number:
#                     listaTemp.append(ps)
#             listaFinal.append(listaTemp)

#         for lista in listaFinal:
#             for ps in lista:
#                 for i in range(lista.index(ps)+1,len(lista)):
#                     if processos_ordenados[ps]['tempo_chegada'] < processos_ordenados[lista[i]]['tempo_chegada']:
#                         processos_ordenados[lista[i]], processos_ordenados[ps] = processos_ordenados[ps], processos_ordenados[lista[i]]

#         for ps in processos_ordenados:
#             for i in range(processos_ordenados[ps]['tempo_execucao']):
#                 Diagrama.append(ps)
#     else:  
#         for ps in processos_ordenados:
#             for i in range(processos_ordenados[ps]['tempo_execucao']):
#                 Diagrama.append(ps)
#     return processos,Diagrama

import random

def SJF(qtd):
    processos = {}
    repetido = False
    for i in range(1, qtd + 1):  # Corrigindo o intervalo
        processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 'tempo_execucao': random.randint(1, 5), 'prioridade': random.randint(1,5)}

    processos_ordenados = dict(sorted(processos.items(), key=lambda x: x[1]['tempo_execucao']))
    CpuBurst = [processos_ordenados[ps]['tempo_execucao'] for ps in processos_ordenados]

    numeros_repetidos = {x for x in CpuBurst if CpuBurst.count(x) > 1}  # Usando um conjunto para verificar tempos de execução repetidos

    Diagrama = []

    if numeros_repetidos:  # Simplificando a condição de repetição
        for number in numeros_repetidos:
            listaFinal = []
            for ps in processos_ordenados:
                if processos_ordenados[ps]['tempo_execucao'] == number:
                    listaFinal.append(ps)

            listaFinal.sort(key=lambda x: processos_ordenados[x]['tempo_chegada'])  # Ordenando a lista com base no tempo de chegada

            for i in range(len(listaFinal)):
                for j in range(i+1, len(listaFinal)):
                    if processos_ordenados[listaFinal[i]]['tempo_chegada'] > processos_ordenados[listaFinal[j]]['tempo_chegada']:
                        listaFinal[i], listaFinal[j] = listaFinal[j], listaFinal[i]

            Diagrama.extend(listaFinal)

    else:
        Diagrama = list(processos_ordenados.keys())

    return processos, Diagrama