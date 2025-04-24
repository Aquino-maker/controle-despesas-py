from tkinter import *
from tkinter import Tk, ttk

# Definição de cores usadas na interface
color1 = "#000000"  # Preto
color2 = "#FFFFFF"  # Branco
color3 = "#1F77B4"  # Azul médio
color4 = "#FF7F0E"  # Laranja
color5 = "#2CA02C"  # Verde
color6 = "#D62728"  # Vermelho
color7 = "#9467BD"  # Roxo
color8 = "#8C564B"  # Marrom
color9 = "#17BECF"  # Ciano

# Criação da janela principal
window = Tk()
window.title('Aquino Controller')  # Título da janela
window.geometry('900x650')  # Tamanho da janela (largura x altura)
window.configure(background=color3)  # Cor de fundo da janela
window.resizable(width=FALSE, height=FALSE)  # Impede o redimensionamento

# Estilo para os componentes ttk
style = ttk.Style(window)
style.theme_use("clam")  # Tema usado para widgets ttk

# Frame superior
top_frame = Frame(window, width=1043, height=50, background=color2, relief="flat")
top_frame.grid(row=0, column=0)

# Frame do meio
middle_frame = Frame(window, width=1043, height=361, background=color2, pady=20, relief="raised")
middle_frame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

middle_baixo = Frame(window, width=1043, height=300, background=color2, relief="flat")
middle_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# Inicia o loop principal da aplicação
window.mainloop()