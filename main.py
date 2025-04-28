# Importação das bibliotecas necessárias
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk  # Para lidar com imagens no Tkinter
from tkinter.ttk import Progressbar  # Barra de progresso personalizada
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Para integrar gráficos do Matplotlib no Tkinter
import matplotlib.pyplot as plt  # Biblioteca de gráficos
from matplotlib.figure import Figure  # Para criação de figuras do Matplotlib

# Definição das cores utilizadas na interface
color1 = "#000000"  # Preto
color2 = "#FFFFFF"  # Branco
color3 = "#1F77B4"  # Azul médio
color4 = "#FF7F0E"  # Laranja
color5 = "#2CA02C"  # Verde
color6 = "#D62728"  # Vermelho
color7 = "#9467BD"  # Roxo
color8 = "#8C564B"  # Marrom
color9 = "#17BECF"  # Ciano

# Criação da janela principal da aplicação
window = Tk()
window.title('Aquino Controller')  # Define o título da janela
window.geometry('900x650')  # Define o tamanho da janela (largura x altura)
window.configure(background=color3)  # Define a cor de fundo da janela
window.resizable(width=FALSE, height=FALSE)  # Impede o redimensionamento da janela

# Configurações de estilo para widgets do ttk
style = ttk.Style(window)
style.theme_use("clam")  # Define o tema visual "clam" para os widgets

# Criação dos frames (áreas) principais da janela

# Frame superior (barra de título/logo)
top_frame = Frame(window, width=1043, height=50, background=color2, relief="flat")
top_frame.grid(row=0, column=0)

# Frame do meio (área principal de conteúdo)
middle_frame = Frame(window, width=1043, height=361, background=color2, pady=20, relief="raised")
middle_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Frame inferior (área adicional para conteúdo ou gráficos)
bottom_frame = Frame(window, width=1043, height=300, background=color2, relief="flat")
bottom_frame.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# Carregamento e configuração da imagem do aplicativo
app_img = Image.open('resource/grafico-de-negocios.png')  # Abre a imagem
app_img = app_img.resize((45, 45))  # Redimensiona a imagem
app_img = ImageTk.PhotoImage(app_img)  # Converte para formato compatível com Tkinter

# Criação do logo do aplicativo (imagem + texto)
app_logo = Label(
    top_frame, image=app_img, text=" Aquino Economic", width=900, compound=LEFT,
    padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),
    bg=color2, fg=color5
)
app_logo.place(x=0, y=0)  # Define a posição do logo no frame superior

# Função para exibir uma barra de progresso
def percentage():
    # Cria um rótulo acima da barra de progresso
    l_name = Label(middle_frame, text="Porcertagem em Gastos", height=1, anchor=NW,
                   font=('Verdana 12'), bg=color2, fg=color5)
    l_name.place(x=7, y=5)

    # Estilo para a barra de progresso
    style = ttk.Style()
    style.theme_use('default')  # Usa o tema padrão
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')  # Cor da barra
    style.configure("Tprogressbar", thickness=25)  # Espessura da barra

    # Cria e posiciona a barra de progresso
    bar = Progressbar(middle_frame, length=180)
    bar.place(x=10, y=35)
    bar['value'] = 10  # Define o valor inicial da barra (10%)

# Chama a função para criar a barra de progresso
percentage()

# Inicia o loop principal da aplicação Tkinter
window.mainloop()