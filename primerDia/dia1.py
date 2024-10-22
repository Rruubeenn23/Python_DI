import tkinter as tk

# Variable de estado para verificar si se ha mostrado un resultado
resultado_mostrado = False

# Función para actualizar el cuadro de texto
def boton_clicado(valor):
    global resultado_mostrado

    if resultado_mostrado:
        # Si el resultado ha sido mostrado, limpiar la pantalla antes de escribir
        entrada.delete(0, tk.END)
        resultado_mostrado = False

    # Obtener el valor actual en la pantalla
    actual = entrada.get()
    # Concatenar el valor del botón presionado
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, actual + valor)

# Función para evaluar la expresión matemática
def calcular():
    global resultado_mostrado
    try:
        # Obtener el contenido actual de la pantalla
        expresion = entrada.get()
        # Evaluar la expresión y mostrar el resultado
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        resultado_mostrado = True  # Indicar que se ha mostrado un resultado
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        resultado_mostrado = False

# Función para limpiar el cuadro de texto
def limpiar():
    global resultado_mostrado
    entrada.delete(0, tk.END)
    resultado_mostrado = False  # Limpiar también el estado de resultado

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.config(bg="#333333")
root.geometry("320x420+0+0")  # Ajustar la ventana para que aparezca en la esquina (0, 0)

# Crear un cuadro de texto para la entrada y resultados
entrada = tk.Entry(root, width=16, font=('Helvetica', 24, 'bold'), borderwidth=2, relief="solid", justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
entrada.config(bg="#1e1e1e", fg="#ffffff")

# Crear los botones de la calculadora
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Colores personalizados
boton_color_bg = "#4CAF50"  # Verde suave
boton_color_fg = "#FFFFFF"  # Texto blanco
boton_operador_bg = "#FF9800"  # Naranja para operadores
boton_igual_bg = "#F44336"  # Rojo para igual
boton_igual_fg = "#FFFFFF"  # Texto blanco en igual
boton_hover_bg = "#81C784"  # Color al pasar el ratón

# Estilo para los botones
boton_estilo = {
    "bg": boton_color_bg,
    "fg": boton_color_fg,
    "activebackground": "#2E7D32",  # Cambiar de color al presionar
    "activeforeground": "#FFFFFF",  # Color de texto al presionar
    "font": ('Helvetica', 18, 'bold'),
    "relief": "raised",
    "bd": 4
}

# Función para aplicar el efecto hover (cambio de color al pasar el ratón)
def on_hover(event, widget):
    widget.config(bg=boton_hover_bg)

def on_leave(event, widget):
    widget.config(bg=boton_color_bg)

# Posicionar los botones en una cuadrícula
fila = 1
columna = 0
for boton in botones:
    if boton == "=":
        # Botón de igual (evaluar)
        boton_igual = tk.Button(root, text=boton, width=5, height=2, bg=boton_igual_bg, fg=boton_igual_fg,
                                activebackground="#C62828", activeforeground=boton_igual_fg,
                                font=('Helvetica', 18, 'bold'), relief="raised", bd=4,
                                command=calcular)
        boton_igual.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
    elif boton == "C":
        # Botón de limpiar
        boton_limpiar = tk.Button(root, text=boton, width=5, height=2, **boton_estilo, command=limpiar)
        boton_limpiar.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
        boton_limpiar.bind("<Enter>", lambda e, w=boton_limpiar: on_hover(e, w))
        boton_limpiar.bind("<Leave>", lambda e, w=boton_limpiar: on_leave(e, w))
    else:
        # Botones numéricos y de operaciones
        if boton in ['+', '-', '*', '/']:
            color_bg = boton_operador_bg  # Color especial para operadores
        else:
            color_bg = boton_color_bg
        
        boton_numero = tk.Button(root, text=boton, width=5, height=2, bg=color_bg, fg=boton_color_fg,
                                 activebackground="#388E3C" if boton not in ['+', '-', '*', '/'] else "#FB8C00",
                                 activeforeground=boton_color_fg, font=('Helvetica', 18, 'bold'),
                                 relief="raised", bd=4,
                                 command=lambda valor=boton: boton_clicado(valor))
        boton_numero.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
        
        # Añadir efecto hover
        boton_numero.bind("<Enter>", lambda e, w=boton_numero: on_hover(e, w))
        boton_numero.bind("<Leave>", lambda e, w=boton_numero: on_leave(e, w))

    # Mover el botón a la siguiente posición en la cuadrícula
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Configurar el tamaño dinámico de las filas y columnas
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
