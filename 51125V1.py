# importamos las librerias necesarias
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# funcion que se ejecuta al presionar el boton
def iniciar_test():
    messagebox.showinfo("inicio del test", "bienvenido al test de adicciones ")
    ventanabienv.destroy()


#configurar la ventana
ventanabienv=tk.Tk()
ventanabienv.title("IU Bienvenida")
ventanabienv.geometry("600x400")
ventanabienv.config(bg="#CF4FCF") #color de fondo

#configurar posicion de la pantalla
ancho_pantalla = ventanabienv.winfo_screenwidth()
alto_pantalla = ventanabienv.winfo_screenheight()
x=(ancho_pantalla // 2) - (600 // 2)
y=(alto_pantalla//2) - (400 // 2)
ventanabienv.geometry(f"700x450+{x}+{y}")

#configurar los widgets o elementos graficos

#bienvenida principal
titulo = tk.Label(
    ventanabienv,
    text="BIENVENIDOS A MI SOFTWARE DE DETECCION DE ADICCIONES A LAS ADICCIONES A LAS REDES SOCIALES ",
    font=("Arial", 18, "bold"),
    bg="#A221C2",
    fg= "#7E1A44",
    wraplength= 550,
    justify="center"
)
titulo.pack(pady=30)

#insertar una imagen
try:
    imagen = PhotoImage(file="AdiccionALasRedes.png")
    img_label = tk.Label(ventanabienv, image=imagen, bg="#E8F0FE")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.Label(ventanabienv, text="no se encontro la imagen", bg="#E8F0FE", fg="gray")
    aviso.pack()

#texto descriptivo
texto = tk.Label(ventanabienv,text="nuestra mision sera es promover el uso responsable e equilibrar las redes sociales entre la vida virtual y en su vida real",)

font=("Arial", 12),
bg="#E8E8FE",
fg="#424242",
wraplength=500,
justify="center",

texto.pack(pady=20)
#elemento boton para iniciar el test
boton_iniciar = tk.Button(
    ventanabienv,
    text="Inicio TEST",
font=("Arial", 14, "bold"),
bg="#5A1EE5",
fg="white",
relief="raised",
bd=3,
padx=20,
pady=10,
command= iniciar_test
)
# ejecutar la interfaz de venta
ventanabienv.mainloop()