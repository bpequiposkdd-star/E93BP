import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

COLOR_FONDO = "#8EF7FF"
COLOR_MENU = "#E290C7"
COLOR_TEXTO = "#8EF7FF"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

root = tk.Tk()
root.title("Bienestar Total")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

def pagina_bienvenida():
    tk.Label(contenido_frame, text="Bienvenido a Adicciones a las redes sociales ", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Comenzamos", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)


    imagen = PhotoImage(file="AdiccionALasRedes.png")
    img_Label = tk.Label( image=imagen, bg= "#8EF7FF")
    img_Label.pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="📝 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    for campo in ["Nombre", "Edad","Correo", "Numero celular"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5) 

def pagina_test():
    tk.Label(contenido_frame, text="🧠 Test de Adicciones ", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para conocer tu nivel de conocimiento.", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    tk.Button(contenido_frame, text="Iniciar Test").pack(pady=20)


paginas = {
   
    "Registro": pagina_registro,
    "Test": pagina_test,
}


for nombre in paginas:
    tk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

tk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

pagina_bienvenida()

root.mainloop()