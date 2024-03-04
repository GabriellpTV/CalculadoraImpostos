from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyperclip

def calcular(e):
    if not valor_entry.get():  
        valor_copiado = pyperclip.paste()
        valor_entry.delete(0, tk.END)
        valor_entry.insert(0, valor_copiado)
        calcular_impostos()
    else:
        calcular_impostos()

def labels(e):
    calcular_impostos()

def calcular_impostos():
    print('RQWERQWERQ')


root = tk.Tk()
root.title('Calculadora de impostos')

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

window_w = 700
window_h = 250
center_x = int(screen_w/2 - window_w/2)
center_y = int(screen_h/2 - window_h/2)

root.geometry(f'{window_w}x{window_h}+{center_x}+{center_y}')
root.resizable(False, False)
# root.attributes('-alpha', 0.9)

irrf_var = tk.BooleanVar()
pis_var = tk.BooleanVar()
cofins_var = tk.BooleanVar()
csll_var = tk.BooleanVar()
iss_var = tk.BooleanVar()
inss_var = tk.BooleanVar()



titulo = ttk.Label(root, text='Bem Vindo(a), Essa é Sua Calculadora de Impostos').pack()


container_valores = tk.Frame(root)
container_valores.pack(side='left')


valor_container = tk.Frame(container_valores)
valor_container.pack(anchor=tk.W, padx= 5)
labelValor = ttk.Label(valor_container, text='Digite o Valor Bruto: ').pack(anchor=tk.W)
valor = BooleanVar()

valor_entry = tk.Entry(valor_container, width=30)
valor_entry.pack(pady= 15)
valor_entry.focus()
valor_entry.bind('<Return>', calcular)


impostos_container = tk.Frame(container_valores)
impostos_container.pack()

checkbox_container = tk.Frame(impostos_container)
checkbox_container.pack(side='left')

irrf_checkbox = tk.Checkbutton(checkbox_container, text="IRRF - 1.5%", variable=irrf_var, command=calcular_impostos)
irrf_checkbox.pack(anchor=tk.W)
pis_checkbox = tk.Checkbutton(checkbox_container, text="PIS - 0.65%", variable=pis_var, command=calcular_impostos)
pis_checkbox.pack(anchor=tk.W)
cofins_checkbox = tk.Checkbutton(checkbox_container, text="COFINS - 3%", variable=cofins_var, command=calcular_impostos)
cofins_checkbox.pack(anchor=tk.W)
csll_checkbox = tk.Checkbutton(checkbox_container, text="CSLL - 1%", variable=csll_var, command=calcular_impostos)
csll_checkbox.pack(anchor=tk.W)

entry_container = tk.Frame(impostos_container)
entry_container.pack(side='left')


labelISS = ttk.Label(entry_container, text='Valor do ISS: ').pack(anchor=tk.W, padx=25)

iss_entry = tk.Entry(entry_container, width=30)
iss_entry.pack(anchor=tk.W, padx=25)
iss_entry.bind('<Return>', labels)


labelINSS = ttk.Label(entry_container, text='Valor do INSS: ').pack(anchor=tk.W, padx=25)

inss_entry = tk.Entry(entry_container, width=30)
inss_entry.pack(anchor=tk.W, padx=25)
inss_entry.bind('<Return>', labels)

print(valor)
root.mainloop()


