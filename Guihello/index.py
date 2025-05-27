import tkinter as tk
from tkinter import messagebox

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Saludo Interactivo")
    ventana.geometry("350x180")
    ventana.configure(bg="#E8F0FE")

    # Título
    tk.Label(
        ventana,
        text="Nombre:",
        font=("Calibri", 11),
        bg="#E8F0FE"
    ).grid(row=0, column=0, padx=20, pady=(25, 10), sticky="e")

    # Campo de texto
    campo_nombre = tk.Entry(ventana, font=("Calibri", 11), width=25)
    campo_nombre.grid(row=0, column=1, pady=(25, 10), padx=10)

    # Función de saludo
    def procesar_saludo():
        nombre = campo_nombre.get().strip()
        if nombre:
            messagebox.showinfo("Saludos", f"¡Hola {nombre}!")
        else:
            messagebox.showwarning("Error", "Debes ingresar un nombre.")

    # Botón Saludar
    btn_saludar = tk.Button(
        ventana,
        text="Saludar",
        command=procesar_saludo,
        bg="#4A90E2",
        fg="white",
        font=("Calibri", 10, "bold"),
        width=12
    )
    btn_saludar.grid(row=1, column=0, pady=20, padx=10)

    # Botón Cerrar
    btn_cerrar = tk.Button(
        ventana,
        text="Salir",
        command=ventana.destroy,
        bg="#D64541",
        fg="white",
        font=("Calibri", 10, "bold"),
        width=12
    )
    btn_cerrar.grid(row=1, column=1, pady=20, padx=10)

    ventana.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    crear_interfaz()
