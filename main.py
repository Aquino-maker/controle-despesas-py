from tkinter import *
from tkinter import Tk, ttk

color1 = "#000000"  # Preto
color2 = "#FFFFFF"  # Branco
color3 = "#1F77B4"  # Azul médio
color4 = "#FF7F0E"  # Laranja
color5 = "#2CA02C"  # Verde
color6 = "#D62728"  # Vermelho
color7 = "#9467BD"  # Roxo
color8 = "#8C564B"  # Marrom
color9 = "#17BECF"  # Ciano

window = Tk()
window.title('Aquino Controller')
window.geometry('900x650')
window.configure(background=color3)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")

window.mainloop()