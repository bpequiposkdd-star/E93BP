import tkinter as tk
from tkinter import ttk

COLOR_FONDO = "#FCFBC8"
COLOR_MENU = "#F36464"
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
    
    try:
        imagen = tk.PhotoImage(file="AdiccionALasRedes.png")  
        label_imagen = tk.Label(contenido_frame, image=imagen, bg=COLOR_FONDO)
        label_imagen.image = imagen 
        label_imagen.pack(pady=20)
    except Exception as e:
        tk.Label(contenido_frame, text="(No se encontró la imagen)", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=20)

    tk.Label(contenido_frame, text="Bienvenido a Adicciones a las redes sociales", 
             font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=10)
    tk.Label(contenido_frame, text="Comenzamos", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="📝 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    
    entradas = {}
    for campo in ["Nombre", "Edad", "Correo", "Número celular"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        entrada = tk.Entry(contenido_frame, width=40)
        entrada.pack(pady=5)
        entradas[campo] = entrada

    tk.Button(contenido_frame, text="Iniciando cuenta", font=FUENTE_TEXTO,
              bg="#CC7400", fg="white", relief="raised", cursor="hand2").pack(pady=20)


def pagina_test():
   
    canvas = tk.Canvas(contenido_frame, bg=COLOR_FONDO, highlightthickness=0)
    scrollbar = ttk.Scrollbar(contenido_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_FONDO)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text="🧠 Test de Adicciones", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(scroll_frame, text="Responde las siguientes preguntas para conocer tu nivel de bienestar.", 
             wraplength=600, bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)
    
    preguntas = [
        ("¿Con qué frecuencia usas las redes sociales al día?",
         ["Menos de 1 hora", "Entre 1 y 3 horas", "Entre 3 y 6 horas", "Más de 6 horas"]),
        ("¿Qué red social utilizas con mayor frecuencia?",
         ["TikTok", "Instagram", "Facebook", "Otras"]),
        ("¿Qué te motiva más a usar las redes sociales?",
         ["Comunicarte con amigos o familiares", "Pasar el tiempo / entretenerme", "Mantenerme informada", "Subir contenido"]),
        ("¿Te consideras adicto(a) a las redes sociales?",
         ["Sí", "Un poco", "No, pero paso mucho tiempo en ellas", "No en absoluto"]),
        ("¿Qué sientes cuando pasas un tiempo sin usar las redes?",
         ["Tranquilidad", "Ansiedad o aburrimiento", "Indiferencia"]),
        ("¿Sueles revisar el celular mientras haces otra actividad (comer, estudiar, etc.)?",
         ["Siempre", "A veces", "Rara vez", "Nunca"]),
        ("¿Has intentado reducir tu tiempo en redes sociales?",
         ["Sí, con éxito", "Sí, pero no pude", "No lo he intentado"])
    ]
    
   
    for i, (pregunta, opciones) in enumerate(preguntas, start=1):
        tk.Label(scroll_frame, text=f"{i}. {pregunta}", bg=COLOR_FONDO, 
                 font=FUENTE_TEXTO, wraplength=700, justify="left").pack(anchor="w", padx=20, pady=5)
        var = tk.StringVar(value="")  
        for opcion in opciones:
            tk.Radiobutton(scroll_frame, text=opcion, variable=var, value=opcion, 
                           bg=COLOR_FONDO, font=("Arial", 11),
                           anchor="w", justify="left").pack(anchor="w", padx=40)

    tk.Button(scroll_frame, text="Enviar respuestas", font=FUENTE_TEXTO, 
              bg="#E2083E", fg="white", cursor="hand2").pack(pady=20)


paginas = {
    "Registro": pagina_registro,
    "Test": pagina_test,
}


for nombre in paginas:
    tk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

tk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)


pagina_bienvenida()

root.mainloop()