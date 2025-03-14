import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

# Crear la ventana principal de la aplicación
app = tk.Tk()
app.geometry("400x500")
app.configure(background="lightblue")
app.title("Registro de Usuario")

# Etiquetas y campos de texto para ingresar los datos del usuario
tk.Label(app, text="Nombre:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
nombre_entry = ttk.Entry(app, font=("Arial", 10))
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Apellido:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
apellido_entry = ttk.Entry(app, font=("Arial", 10))
apellido_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Correo Electrónico:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
correo_entry = ttk.Entry(app, font=("Arial", 10))
correo_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Número de teléfono:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
numero_entry = ttk.Entry(app, font=("Arial", 10))
numero_entry.grid(row=3, column=1, padx=10, pady=10)

# Lista de usuarios con un scrollbar para visualizar los registros
scrollbar = tk.Scrollbar(app)
scrollbar.grid(row=6, column=2, sticky="ns", padx=10, pady=10)

lista_usuarios = tk.Listbox(app, yscrollcommand=scrollbar.set, font=("Arial", 10), height=8, bg="white", fg="black")
lista_usuarios.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

scrollbar.config(command=lista_usuarios.yview)

# Función para validar el formato del correo electrónico
def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo)

# Función para agregar un usuario a la lista
def agregar_usuario():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    correo = correo_entry.get()
    numero = numero_entry.get()

    if nombre and apellido and correo and numero:
        if not validar_correo(correo):
            messagebox.showerror("Correo Inválido", "Por favor, ingrese un correo electrónico válido.")
            return

        lista_usuarios.insert(tk.END, f"{nombre} {apellido}, {correo}, {numero}")
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        correo_entry.delete(0, tk.END)
        numero_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos Incompletos", "Por favor, complete todos los campos.")

# Función para limpiar la lista de usuarios
def limpiar_lista():
    lista_usuarios.delete(0, tk.END)

# Botones de la aplicación
ttk.Button(app, text="Agregar", command=agregar_usuario).grid(row=4, column=0, columnspan=2, pady=10)
ttk.Button(app, text="Limpiar", command=limpiar_lista).grid(row=5, column=0, columnspan=2, pady=10)

# Añadir padding a los widgets
for child in app.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Ejecutar la interfaz gráfica
app.mainloop()
