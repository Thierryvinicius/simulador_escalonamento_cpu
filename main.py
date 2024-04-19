from FCFS import FCFS
from SJF import SJF
from SRTF import srtf
def main(operador,qtd):

    if operador == 'FCFS':
        processo,diagrama,orq = FCFS(qtd)
    elif operador == 'SJF':
        processo,diagrama,orq = SJF(qtd)
    else:
        processo,diagrama,orq = srtf(qtd)
        
    return processo,diagrama,orq