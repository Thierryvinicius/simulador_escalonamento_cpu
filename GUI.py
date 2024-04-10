import tkinter as tk 
from main import main
from tkinter import messagebox

class Quadrado:
    def __init__(self, canvas, x, y, tamanho, texto, cor):
        self.canvas = canvas
        self.cor = cor
        self.retangulo = canvas.create_rectangle(x, y, x + tamanho, y + tamanho, fill=cor)
        self.texto = canvas.create_text(x + tamanho / 2, y + tamanho / 2, text=texto, fill="black")

global selectedValue,quadrados,posicao,numberColor,x,y,limparCanvas

limparCanvas = False

x = 10
y = 50
numberColor = 0
posicao = 0
quadrados = []
selectedValue = 'FCFS'

def centralizar_janela(janela):
    largura_janela = 250
    altura_janela = 200

    # Obtenha as dimensões da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcule as coordenadas x e y para centralizar a janela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Defina a geometria da janela para as coordenadas calculadas
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")


def auto():
    def InserirAuto():
        global processo,diagrama,nomeAnterior
        qtd = qtdtxt.get()
        if qtd.isdigit():
            janelaqtd.destroy()
            processo,diagrama = main(selectedValue,int(qtd)+1)
            nomeAnterior = diagrama[0]
        else:
            janelaqtd.destroy()
            messagebox.showinfo(title='popup',message='Insira Um numero')
    janelaqtd = tk.Toplevel(janela)
    janelaqtd.title('Inserir Quantidade')
    janelaqtd.grab_set()

    qtdLabel = tk.Label(janelaqtd,text='Quantida de Processo:')
    qtdLabel.pack()

    qtdtxt = tk.Entry(janelaqtd)
    qtdtxt.pack()

    buttonInserir = tk.Button(janelaqtd,text='Inseir',command=InserirAuto)
    buttonInserir.pack()
    
    centralizar_janela(janelaqtd)

def Insert():
    InserPS = tk.Toplevel()


def mostrar_selecao(selecao):
    global selectedValue
    selectedValue = selecao


def gerar_quadrado():
    global numberColor,nomeAnterior,y,x,limparCanvas
    if limparCanvas == True:
        canvas.delete(tk.ALL)
        limparCanvas = False
    nomes = diagrama
    cores = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]

    largura_janela = canvas.winfo_reqwidth()  # largura da janela

    nome = nomes[posicao]
    cor = cores[numberColor]
    if quadrados:  # Se já houver quadrados, obter as coordenadas do último
        ultimo_quadrado = quadrados[-1]
        x = canvas.coords(ultimo_quadrado.retangulo)[2] + 10  # Posição x do último quadrado + 10 para o espaço entre quadrados
        if x + 90 > largura_janela:  # Se ultrapassar a largura da janela, vá para a próxima linha
            x = 10  # Reinicia a posição x
            y += 90  # Muda para a próxima linha
    if nomeAnterior == nome:
        quadrados.append(Quadrado(canvas, x, y, 20, nome, cor))
    else:
        if numberColor == len(cores)-1:
            numberColor = 0
        else:
            numberColor += 1
        cor = cores[numberColor]
        nomeAnterior = nome
        quadrados.append(Quadrado(canvas, x, y, 20, nome, cor))

def proximo():
    global quadrados,posicao,numberColor,x,y,limparCanvas

    if posicao < len(diagrama) - 1:
        posicao += 1
        gerar_quadrado()
    else:
        limparCanvas = True
        x = 10
        y = 50
        numberColor = 0
        posicao = 0
        quadrados = []
        messagebox.showinfo('popup',message='Processo Finalizado')
        



janela = tk.Tk()

janela.title('Simulador')
janela.attributes('-zoomed', True)

options = ['FCFS','SJF','SRTF']

opcao_selecionada = tk.StringVar(janela)
opcao_selecionada.set(options[0]) 

apbar = tk.Frame(janela,bg='black',height=100)
apbar.pack(side='top',fill='x')

selectBox = tk.OptionMenu(apbar, opcao_selecionada, *options, command=mostrar_selecao)
selectBox.pack(padx=20,pady=10,side='left')

buttonInsert = tk.Button(apbar,text='Inserir',bg='gray',command=Insert)
buttonInsert.pack(padx=20,pady=10,side='left')

buttonAuto = tk.Button(apbar,text='Auto',bg='gray',command=auto)
buttonAuto.pack(padx=20,pady=10,side='left')

frameCanvas = tk.Frame(janela,width=400,height=300)
frameCanvas.pack(expand=True)

canvas = tk.Canvas(frameCanvas, width=1200, height=500)
canvas.pack()

buttonProx = tk.Button(frameCanvas,text='ProximoPS',command=proximo)
buttonProx.pack()

selectedValue = 'FCFS'
janela.mainloop()