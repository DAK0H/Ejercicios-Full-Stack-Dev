'''En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y 
que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.'''

import tkinter as tk

window = tk.Tk()
window.title("RadioButton")

selected = tk.StringVar()

# Se crea el comando para el botón de reinicio
def reset():
    selected.set(None)

# Se crean los botones de radio
radio1 = tk.Radiobutton(window, text="Python", variable=selected, value="Python")
radio2 = tk.Radiobutton(window, text="Java", variable=selected, value="Java")
radio3 = tk.Radiobutton(window, text="C++", variable=selected, value="C++")
radio4 = tk.Radiobutton(window, text="C#", variable=selected, value="C#")
radio5 = tk.Radiobutton(window, text="JavaScript", variable=selected, value="JavaScript")
button = tk.Button(window, text="Reset", command=reset)

# Se resetea la selección inicial
selected.set(None)

# Se da formato a los elementos
radio1.grid(column=0, row=1, pady=5, padx=5, sticky=tk.W)
radio2.grid(column=0, row=2, pady=5, padx=5, sticky=tk.W)
radio3.grid(column=0, row=3, pady=5, padx=5, sticky=tk.W)
radio4.grid(column=0, row=4, pady=5, padx=5, sticky=tk.W)
radio5.grid(column=0, row=5, pady=5, padx=5, sticky=tk.W)
button.grid(column=1, row=6, pady=5, padx=5, sticky=tk.W)

window.mainloop()