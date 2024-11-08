import tkinter as tk
from tkinter import messagebox

class Elevador:
    def __init__(self, total_capacidade, total_andar):
        self.total_capacidade = total_capacidade 
        self.atual_capacidade = 0 
        self.total_andar = total_andar
        self.atual_andar = 0

    def subir(self):
        if self.atual_andar < self.total_andar - 1:
            self.atual_andar += 1
            return "Subindo"
        else:
            return "VOCÊ ESTÁ NO ANDAR MAIS ALTO!"

    def descer(self):
        if self.atual_andar > 0:
            self.atual_andar -= 1
            return "Descendo"
        else:
            return "VOCÊ JÁ ESTÁ NO TÉRREO!"

    def entrar(self):
        if self.atual_capacidade < self.total_capacidade:
            self.atual_capacidade += 1
            return "Entrando uma pessoa"
        else:
            return "O ELEVADOR ESTÁ CHEIO!"

    def sair(self):
        if self.atual_capacidade > 0:
            self.atual_capacidade -= 1
            return "Saindo uma pessoa"
        else:
            return "NÃO TEM NINGUÉM"

def update_status():
    status = f"Andar Atual: {elevador.atual_andar}, Capacidade Atual: {elevador.atual_capacidade}/{elevador.total_capacidade}"
    status_label.config(text=status)

def subir():
    message = elevador.subir()
    messagebox.showinfo("Ação", message)
    update_status()

def descer():
    message = elevador.descer()
    messagebox.showinfo("Ação", message)
    update_status()

def entrar():
    message = elevador.entrar()
    messagebox.showinfo("Ação", message)
    update_status()

def sair():
    message = elevador.sair()
    messagebox.showinfo("Ação", message)
    update_status()

root = tk.Tk()
root.title("Controle de Elevador")

elevador = Elevador(total_capacidade=5, total_andar=10)

# Criando botões
btn_subir = tk.Button(root, text="Subir", command=subir)
btn_subir.pack(pady=5)

btn_descer = tk.Button(root, text="Descer", command=descer)
btn_descer.pack(pady=5)

btn_entrar = tk.Button(root, text="Entrar", command=entrar)
btn_entrar.pack(pady=5)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=20)

update_status()

root.mainloop()