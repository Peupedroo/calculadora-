import tkinter as tk
from datetime import datetime
import winsound

#o a cria um arquivo
def salvar_historico(operacao,num1,num2,resultado):
    with open("historico_calculadora.txt","a")as file:
        file.write(f"{datetime.now()}-{operacao}-{num1}e{num2}={resultado}.\n")

def bip():
    winsound.Beep(100,1000)

def realizar_operacao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacao = operacao_var.get()
    resultado = 0

    if operacao == "add":
        resultado = num1 + num2
    elif operacao == "subtract":
        resultado = num1 -num2

    elif operacao == "multiply":
        resultado = num1 * num2
    elif operacao == "divide":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "erro nao pode dividir por zero"


    label_resultado.config(text=f"resultado: {resultado}")
    if isinstance(resultado, (int, float)):
        salvar_historico(operacao, num1, num2, resultado)
        bip()

# criacao da janela principal
root = tk.Tk()
root.title("calculadora simples")

# criar os famosos wigets
entry_num1 = tk.Entry(root, width=10)
entry_num2 = tk.Entry(root, width=10)
entry_num1.pack(pady=10)
entry_num2.pack(pady=10)

operacao_var = tk.StringVar(root)
operacao_var.set("add")# valor padrao

# criando botoes
tk.OptionMenu(root, operacao_var, "add", "subtract", "multiply", "divide").pack()
button_calcular = tk.Button(root, text="calcular", command=realizar_operacao)
button_calcular.pack(pady=20)


label_resultado = tk.Label(root, text="resultado:")
label_resultado.pack(pady=10)

#execucao do loop principal da interface
root.mainloop()