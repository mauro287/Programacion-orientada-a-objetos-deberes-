#Es el módulo estándar de Python para crear interfaces gráficas de usuario (GUI)
import tkinter as tk
#Se utiliza para mostrar mensajes de confirmación al agregar o eliminar eventos
from tkinter import ttk, messagebox
# permite al usuario seleccionar la fecha de un evento de manera sencilla.
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x450")
        self.root.configure(bg="#1e1e2e")  # Fondo oscuro elegante

        # Frame de Entrada de Datos
        frame_input = tk.Frame(self.root, bg="#282a36")
        frame_input.pack(pady=10, padx=10, fill=tk.X)

        # Etiqueta y selector de fecha
        tk.Label(frame_input, text="Fecha:", bg="#282a36", fg="#ff79c6", font=("Arial", 10, "bold")).grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        self.date_entry = DateEntry(frame_input, width=12, background='#bd93f9', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Etiqueta y campo de entrada para la hora
        tk.Label(frame_input, text="Hora:", bg="#282a36", fg="#8be9fd", font=("Arial", 10, "bold")).grid(row=0,
                                                                                                         column=2,
                                                                                                         padx=5, pady=5,
                                                                                                         sticky="w")
        self.time_entry = tk.Entry(frame_input, width=15, bg="#ffffff", fg="#333")
        self.time_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Etiqueta y campo de entrada para la descripción del evento
        tk.Label(frame_input, text="Descripción:", bg="#282a36", fg="#50fa7b", font=("Arial", 10, "bold")).grid(row=1,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5,
                                                                                                                sticky="w")
        self.desc_entry = tk.Entry(frame_input, width=50, bg="#ffffff", fg="#333")
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        # Etiqueta y selector de categoría
        tk.Label(frame_input, text="Categoría:", bg="#282a36", fg="#ffb86c", font=("Arial", 10, "bold")).grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=5,
                                                                                                              pady=5,
                                                                                                              sticky="w")
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(frame_input, textvariable=self.category_var,
                                              values=("Trabajo", "Personal", "Recordatorio"), state="readonly")
        self.category_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.category_combobox.current(0)

        # Frame para los botones
        frame_buttons = tk.Frame(self.root, bg="#282a36")
        frame_buttons.pack(pady=5)

        # Botón para agregar evento
        tk.Button(frame_buttons, text="Agregar Evento", command=self.add_event, bg="#4caf50", fg="white",
                  font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        # Botón para eliminar evento seleccionado
        tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event, bg="#f44336", fg="white",
                  font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        # Botón para salir de la aplicación
        tk.Button(frame_buttons, text="Salir", command=self.root.quit, bg="#ff5555", fg="white",
                  font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

        # Configuración de estilos para la tabla de eventos
        style = ttk.Style()
        style.configure("Treeview", background="#44475a", foreground="white", rowheight=25, fieldbackground="#44475a")
        style.map("Treeview", background=[("selected", "#6272a4")])

        # Tabla para mostrar los eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción", "Categoría"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_event(self):
        """Función para agregar un evento a la tabla."""
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()
        categoria = self.category_var.get()

        if fecha and hora and descripcion and categoria:
            self.tree.insert("", "end", values=(fecha, hora, descripcion, categoria))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    def delete_event(self):
        """Función para eliminar el evento seleccionado en la tabla."""
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
