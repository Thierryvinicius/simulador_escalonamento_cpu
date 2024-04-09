import random

def SJF():
    processos = {}
    repetido = False
    for i in range(1, 5):
        processos['P' + str(i)] = {'tempo_chegada': random.randint(0, 5), 'tempo_execucao': random.randint(1, 5), 'prioridade': random.randint(1,5)}


    processos_ordenados = dict(sorted(processos.items(), key=lambda x: x[1]['tempo_execucao']))
    CpuBurst = []
    print(processos_ordenados)
    input()

    for ps in processos_ordenados:
        CpuBurst.append(processos_ordenados[ps]['tempo_execucao'])
    numeros_repetidos = []
    for numero in CpuBurst:
        if CpuBurst.count(numero) > 1 and numero not in numeros_repetidos:
            numeros_repetidos.append(numero)
            repetido = True
   
    Diagrama = []
   
    if repetido == True:
       
        listaFinal =[]
       
        for number in numeros_repetidos:
            listaTemp = []
            for ps in processos_ordenados:
                if processos_ordenados[ps]['tempo_execucao'] == number:
                    listaTemp.append(ps)
            listaFinal.append(listaTemp)

        for lista in listaFinal:
            for ps in lista:
                for i in range(lista.index(ps)+1,len(lista)):
                    if processos_ordenados[ps]['tempo_chegada'] < processos_ordenados[lista[i]]['tempo_chegada']:
                        processos_ordenados[ps], processos_ordenados[lista[i]] = processos_ordenados[lista[i]], processos_ordenados[ps]
        
        for ps in processos_ordenados:
            for i in range(processos_ordenados[ps]['tempo_execucao']):
                Diagrama.append(ps)
    else:  
        for ps in processos_ordenados:
            for i in range(processos_ordenados[ps]['tempo_execucao']):
                Diagrama.append(ps)
    return processos,Diagrama