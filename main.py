import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.title('Café Los Hermanos Camaleón')
window.geometry('600x800')
 
var = tk.StringVar()
titulo = tk.Label(window, bg='brown', fg='white', width=100, text='Bienvenido al Café Los Hermanos Camaleón ', font = ("sansserif", 18, "bold"))
titulo.pack(fill='x', ipadx=15, ipady=25)
l = tk.Label(window, bg='brown', width=100, text='Ordena tu café favorito ', font = ("sansserif", 14, "bold"))
l.pack(fill='x', ipadx=15, ipady=15)

def borrarPedido():
    l.config(text=' ')

def enviarPedido():
    l.config(text='Gracias por tu preferencia \n Tu pedido ha sido enviado')
    
def pedido():
    l.config(text='Costo de ' + var.get())
    
 
r1 = tk.Radiobutton(window, bg='yellow', width=100, text='Capuccino', variable=var, value='$60 MXN', command=pedido)
r1.pack(fill='x', ipadx=5, ipady=10)
r2 = tk.Radiobutton(window, bg='yellow', width=100, text='Expresso', variable=var, value='$50 MXN', command=pedido)
r2.pack(fill='x', ipadx=5, ipady=10)
r3 = tk.Radiobutton(window, bg='yellow', width=100, text='Latte', variable=var, value='$37 MXN', command=pedido)
r3.pack(fill='x', ipadx=5, ipady=10)
r4 = tk.Radiobutton(window, bg='yellow', width=100, text='Americano', variable=var, value='$35 MXN', command=pedido)
r4.pack(fill='x', ipadx=5, ipady=10)
r5 = tk.Radiobutton(window, bg='yellow', width=100, text='Machiatto', variable=var, value='$65 MXN', command=pedido)
r5.pack(fill='x', ipadx=5, ipady=10)

btn_borrar = tk.Button(window, bg='white', fg='red', width=20, text = 'Borrar pedido',
                command = borrarPedido)
btn_borrar.pack(side=tk.LEFT, padx=50)

btn_enviar = tk.Button(window, bg='green', fg='white', width=20, text = 'Enviar pedido',
                command = enviarPedido)
btn_enviar.pack(side=tk.RIGHT, padx=50)
 
window.mainloop()
