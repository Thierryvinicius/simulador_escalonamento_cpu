import tkinter as tk 
from main import main
from tkinter import messagebox

class Quadrado:
    def __init__(self, canvas, x, y, tamanho, texto, cor):
        self.canvas = canvas
        self.cor = cor
        self.retangulo = canvas.create_rectangle(x, y, x + tamanho, y + tamanho, fill=cor)
        self.texto = canvas.create_text(x + tamanho / 2, y + tamanho / 2, text=texto, fill="black")

global selectedValue,quadrados,posicao,numberColor,x,y,limparCanvas,widgets_grid,processos,qtdIsert,existDiagrama
qtdIsert = 0
processos = {}
widgets_grid = []

existDiagrama = False
limparCanvas = False

x = 10
y = 50
numberColor = 0
posicao = 0
quadrados = []
selectedValue = 'FCFS'

def centralizar_janela(janela,largura,altura):
    largura_janela = largura
    altura_janela = altura

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
        global processo,diagrama,nomeAnterior,widgets_grid

        qtd = qtdtxt.get()
        if qtd.isdigit():
            janelaqtd.destroy()
            processo,diagrama = main(selectedValue,int(qtd)+1)
            nomeAnterior = diagrama[0]
            limpar_grid(widgets_grid)
            criar_grid(processo)
        else:
            messagebox.showinfo(title='popup',message='Insira Um numero')
            janelaqtd.lift()
    janelaqtd = tk.Toplevel(janela)
    janelaqtd.title('Inserir Quantidade')
    janelaqtd.grab_set()

    qtdLabel = tk.Label(janelaqtd,text='Quantida de Processo:')
    qtdLabel.pack()

    qtdtxt = tk.Entry(janelaqtd)
    qtdtxt.pack()

    buttonInserir = tk.Button(janelaqtd,text='Inseir',command=InserirAuto)
    buttonInserir.pack()
    
    centralizar_janela(janelaqtd,250,200)

def Insert():

    def InsertValue():
        global processos,qtdIsert,existDiagrama
        if ValorTempoChegada.get() == '' or ValorTempoExecucao.get() == '' or ValorPrioridade.get() == '':
            messagebox.showinfo('popup',message='Insira Todos os valores')
            InserPS.lift()
        elif ValorTempoChegada.get().isdigit() and ValorTempoExecucao.get().isdigit() and ValorPrioridade.get().isdigit():
            processos['P' + str(qtdIsert)] = {'tempo_chegada': int(ValorTempoChegada.get()), 'tempo_execucao': int(ValorTempoExecucao.get()), 'prioridade': int(ValorPrioridade.get())}
            qtdIsert+=1
            existDiagrama = True
            criar_grid(processos)

        else:
            messagebox.showinfo('popup',message='Insira Numeros Nos Valores:\n Tempo de chegada\n Tempo de execução\n Prioridade')
            InserPS.lift()
    InserPS = tk.Toplevel()
    centralizar_janela(InserPS,250,400)

    TempoChegadaLabel = tk.Label(InserPS,text='Tempo de Chegada:')
    TempoChegadaLabel.pack()
    ValorTempoChegada = tk.Entry(InserPS)
    ValorTempoChegada.pack()

    TempoExecucaoLabel = tk.Label(InserPS,text='Tempo de execução:')
    TempoExecucaoLabel.pack()
    ValorTempoExecucao = tk.Entry(InserPS)
    ValorTempoExecucao.pack()

    PrioridadeLabel = tk.Label(InserPS,text='Prioridade:')
    PrioridadeLabel.pack()
    ValorPrioridade = tk.Entry(InserPS)
    ValorPrioridade.pack()

    buttonInsert = tk.Button(InserPS,text='Inserir',command=InsertValue)
    buttonInsert.pack(pady=20)

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
    global quadrados,posicao,numberColor,x,y,limparCanvas,existDiagrama

    for i in range(0,len(diagrama)):
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
            
def limpar_grid(widgets_grid):
    # Destrua cada widget na lista
    for widget in widgets_grid:
        widget.destroy()

def criar_grid(processo):
    global widgets_grid
    widgets_grid = []  # Lista para armazenar os widgets criados

    # Adiciona uma linha para os rótulos de informações
    label_info = tk.Label(frameInfo, text='PS', bg='#A9A9A9', fg='white')
    label_info.grid(row=0, column=0, padx=0, pady=5)
    widgets_grid.append(label_info)

    label_info = tk.Label(frameInfo, text='Tempo Chegada', bg='#A9A9A9', fg='white')
    label_info.grid(row=0, column=1, padx=0, pady=5)
    widgets_grid.append(label_info)

    label_info = tk.Label(frameInfo, text='Tempo Execução', bg='#A9A9A9', fg='white')
    label_info.grid(row=0, column=2, padx=0, pady=5)
    widgets_grid.append(label_info)

    label_info = tk.Label(frameInfo, text='Prioridade', bg='#A9A9A9', fg='white')
    label_info.grid(row=0, column=3, padx=0, pady=5)
    widgets_grid.append(label_info)

    for i, (nome, tempo) in enumerate(processo.items(), start=1):  # Começa a partir da linha 1
        label_nome = tk.Label(frameInfo, text=nome, bg='#A9A9A9', fg="white")
        label_nome.grid(row=i, column=0, padx=0, pady=5)
        widgets_grid.append(label_nome)

        label_tempo_chegada = tk.Label(frameInfo, text=tempo['tempo_chegada'], bg='#A9A9A9', fg="white")
        label_tempo_chegada.grid(row=i, column=1, padx=0, pady=5)
        widgets_grid.append(label_tempo_chegada)

        label_tempo_execucao = tk.Label(frameInfo, text=tempo['tempo_execucao'], bg='#A9A9A9', fg="white")
        label_tempo_execucao.grid(row=i, column=2, padx=0, pady=5)
        widgets_grid.append(label_tempo_execucao)

        label_prioridade = tk.Label(frameInfo, text=tempo['prioridade'], bg='#A9A9A9', fg="white")
        label_prioridade.grid(row=i, column=3, padx=0, pady=5)
        widgets_grid.append(label_prioridade)

def plot():
    from plot_grafico import geraValor
    operador = opcao_selecionada.get()
    geraValor(processo, operador)

janela = tk.Tk()

janela.title('Simulador')
janela.state('zoomed')
janela.configure(background='#696969')

options = ['FCFS','SJF','SRTF']

opcao_selecionada = tk.StringVar(janela)
opcao_selecionada.set(options[0]) 

apbar = tk.Frame(janela,bg='#808080',height=100)
apbar.pack(side='top',fill='x')

frameInfo = tk.Frame(janela,bg='#A9A9A9')
frameInfo.pack(side='left',anchor='nw')

selectBox = tk.OptionMenu(apbar, opcao_selecionada, *options, command=mostrar_selecao)
selectBox.pack(padx=20,pady=10,side='left')

buttonInsert = tk.Button(apbar,text='Inserir',bg='white',command=Insert)
buttonInsert.pack(padx=20,pady=10,side='left')

buttonAuto = tk.Button(apbar,text='Auto',bg='white',command=auto)
buttonAuto.pack(padx=20,pady=10,side='left')

buttonPlot = tk.Button(apbar,text='Plot',bg='white',command=plot)
buttonPlot.pack(padx=20,pady=10,side='left')

frameCanvas = tk.Frame(janela,bg='#696969',width=500)
frameCanvas.pack()

canvas = tk.Canvas(frameCanvas,width=500,height=500)
canvas.pack(padx=10)

buttonProx = tk.Button(frameCanvas,text='Iniciar',command=proximo)
buttonProx.pack()

selectedValue = 'FCFS'
janela.mainloop()