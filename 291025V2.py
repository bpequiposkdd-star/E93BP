#importar las bibliotecas
import tkinter as tk

# definir las funciones 

# ventana de bienvenida 
ventanabien = tk.Tk()
ventanabien.title("1-VENTANA DE BIENVENIDA")
ventanabien.geometry("600x400")

tk.Label(ventanabien, text="bienvenido al software de deteccion de adicciones a redes sociales ")
tk.Label(ventanabien, text="aqui colocamos la descripcion de tu software")
btn1= tk.Button (ventanabien, text= "Iniciar", command= lambda: ir_a (ventanabien, ventana2))
btn1.pack(pady=30)

#ventana de registro
ventana2= tk.Toplevel(ventanabien)
ventana2.title("2-VENTANA DE REGISTRO")
ventanabien.geometry("600x400")

tk.Label(ventana2, text="Registro de usuario").pack("pady =20")
tk.Label(ventana2, text="nombre:").pack()
tk.Entry (ventana2).pack()
tk. Label(ventana2, text="edad:").pack()
tk.Entry(ventana2).pack()
tk.Label(ventana2, text="E-mail:").pack()
tk.Entry (ventana2). pack()

tk.Button(ventana2, text=" regresar", command= lambda: regresar( ventana2, ventanabien)).pack(side=left, padx=50, pady=40)
tk.Button(ventana2, text="continuar ", command= lambda: ir_a(ventana2, ventana3)).pack(side="right", padx=50, pady=40) 


#ventana del test


#ventana de resultados


# ventana de sintomas y señales 


# historias hispiradoras 


# ventana de ayuda 


#llamar a traer las ventanas