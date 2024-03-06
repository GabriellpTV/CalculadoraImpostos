from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyperclip


#  pyinstaller --onefile --noconsole impostos.py
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
    labelirrf.config(text='')
    labelpis.config(text='')
    labelcofins.config(text='')
    labelcsll.config(text='')
    labeliss.config(text='')
    labelinss.config(text='')
    titulo_retencoes.config(text='')
    label_impostos.config(text='')
    label_liquido.config(text='')
    irrf_checkbox.config(text="IRRF - 1.5%")
    imposto = 0
    valor_bruto = 0
    try:
        copia = float(valor_entry.get())
        valor = 0 #Colocar um formatador de valor aqui dps
        valor_bruto += valor
        titulo_retencoes.config(text=(f"Valor Bruto: {valor_bruto}"))
    except:
        print("Nenhum valor Adicionado")
    
    try:
        iss = 0
        valor_iss = float(iss_entry.get())
        iss += valor_iss
        print(f'ISS: {iss}')
        irrf_checkbox.config(text="IRRF - 1%")
        labeliss.config(text=(f"Valor ISS: {iss}"))
    except:
        print("Não Exite retenção de ISS")
    
    try:
        inss = 0
        valor_inss = float(inss_entry.get())
        inss += valor_inss
        print(f'INSS: {inss}')
        irrf_checkbox.config(text="IRRF - 1%")
        labelinss.config(text=(f"Valor INSS: {inss}"))
    except:
        print("Não existe retenção de INSS")
    
    if irrf_var.get() == 1:
        if iss != 0 or inss != 0:
            irrf = valor_bruto / 100
            imposto += irrf
            labelirrf.config(text=(f"Valor IRRF: {irrf}"))
        else:
            irrf = (valor_bruto * 1.5) / 100
            imposto += irrf
            labelirrf.config(text=(f"Valor IRRF: {irrf}"))
            
    if pis_var.get() == 1:
        pis = (valor_bruto * 0.65) / 100
        imposto += pis
        labelpis.config(text=(f"Valor PIS: {pis}"))
        
    if cofins_var.get():
        cofins = (valor_bruto * 3) / 100
        imposto += cofins
        labelcofins.config(text=(f"Valor COFINS: {cofins}"))
        
    if csll_var.get():
        csll = valor_bruto / 100   
        imposto  += csll
        labelcsll.config(text=(f"Valor CSLL: {csll}"))
        
    imposto += iss + inss
    label_impostos.config(text=(f"Valor Impostos: {imposto}"))
    conta = valor_bruto - imposto
    valor_liquido = round(conta, 2)
    label_liquido.config(text=(f"Valor Liquido: {valor_liquido}"))
    
    


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

irrf_var = tk.DoubleVar()
pis_var = tk.DoubleVar()
cofins_var = tk.DoubleVar()
csll_var = tk.DoubleVar()
iss_var = tk.DoubleVar()
inss_var = tk.DoubleVar()




titulo = ttk.Label(root, text='Bem Vindo(a), Essa é Sua Calculadora de Impostos').pack()


box = tk.Frame(root)
box.pack(side='left')

container_valores = tk.Frame(box)
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


labelISS = tk.Label(entry_container, text='Valor do ISS: ').pack(anchor=tk.W, padx=25)

iss_entry = tk.Entry(entry_container, width=30)
iss_entry.pack(anchor=tk.W, padx=25)
iss_entry.bind('<Return>', labels)


labelINSS = tk.Label(entry_container, text='Valor do INSS: ').pack(anchor=tk.W, padx=25)

inss_entry = tk.Entry(entry_container, width=30)
inss_entry.pack(anchor=tk.W, padx=25)
inss_entry.bind('<Return>', labels)

container_resultados = tk.Frame(box)
container_resultados.pack(padx=25)

container_impostos = tk.Frame(container_resultados)
container_impostos.pack(side='left', padx=25)

labelirrf = tk.Label(container_impostos, text='')
labelirrf.pack(anchor=tk.W)
labelpis = tk.Label(container_impostos, text='')
labelpis.pack(anchor=tk.W)
labelcofins = tk.Label(container_impostos, text='')
labelcofins.pack(anchor=tk.W)
labelcsll = tk.Label(container_impostos, text='')
labelcsll.pack(anchor=tk.W)
labeliss = tk.Label(container_impostos, text='')
labeliss.pack(anchor=tk.W)
labelinss = tk.Label(container_impostos, text='')
labelinss.pack(anchor=tk.W)


container_totais = tk.Frame(container_resultados)
container_totais.pack(padx=25)

titulo_retencoes = tk.Label(container_totais, text='')
titulo_retencoes.pack(anchor=tk.W)
label_impostos = tk.Label(container_totais, text='')
label_impostos.pack(anchor=tk.W)
label_liquido = tk.Label(container_totais, text='')
label_liquido.pack(anchor=tk.W)


root.mainloop()


