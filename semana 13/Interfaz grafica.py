import tkinter as tk

# Crear la ventana principal de la aplicación
app = tk.Tk()
app.geometry("400x500")  # Tamaño de la ventana
app.configure(background="lightblue")  # Color de fondo
app.title("Registro de Usuario")  # Título de la ventana

# Etiquetas y campos de texto para ingresar los datos del usuario
tk.Label(app, text="Nombre:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
nombre_entry = tk.Entry(app, font=("Arial", 10))  # Campo de texto para el nombre
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Apellido:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
apellido_entry = tk.Entry(app, font=("Arial", 10))  # Campo de texto para el apellido
apellido_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Correo Electrónico:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
correo_entry = tk.Entry(app, font=("Arial", 10))  # Campo de texto para el correo electrónico
correo_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Número de teléfono:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
numero_entry = tk.Entry(app, font=("Arial", 10))  # Campo de texto para el número de teléfono
numero_entry.grid(row=3, column=1, padx=10, pady=10)

# Lista de usuarios con un scrollbar para visualizar los registros
scrollbar = tk.Scrollbar(app)
scrollbar.grid(row=6, column=2, sticky="ns", padx=10, pady=10)

lista_usuarios = tk.Listbox(app, yscrollcommand=scrollbar.set, font=("Arial", 10), height=8)  # Lista para mostrar usuarios
lista_usuarios.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

scrollbar.config(command=lista_usuarios.yview)

# Función para agregar un usuario a la lista
def agregar_usuario():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    correo = correo_entry.get()
    numero = numero_entry.get()

    # Verificamos que todos los campos estén completos antes de agregar
    if nombre and apellido and correo and numero:
        lista_usuarios.insert(tk.END, f"{nombre} {apellido}, {correo}, {numero}")  # Agregar usuario a la lista
        # Limpiar los campos de texto después de agregar
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        correo_entry.delete(0, tk.END)
        numero_entry.delete(0, tk.END)
    else:
        # Si faltan campos, mostrar un mensaje de advertencia en la consola
        print("Por favor, complete todos los campos.")

# Función para limpiar la lista de usuarios
def limpiar_lista():
    lista_usuarios.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Botones de la aplicación
tk.Button(app, text="Agregar", command=agregar_usuario, font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(app, text="Limpiar", command=limpiar_lista, font=("Arial", 12)).grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar la interfaz gráfica
app.mainloop()
