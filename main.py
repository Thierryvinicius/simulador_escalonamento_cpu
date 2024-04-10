from FCFS import FCFS
from SJF import SJF
from SRTF import srtf
def main(operador,qtd):

    if operador == 'FCFS':
        processo,diagrama = FCFS(qtd)
    elif operador == 'SJF':
        processo,diagrama = SJF(qtd)
    else:
        processo,diagrama = srtf(qtd)
        
    return processo,diagrama