'''En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener 
una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.'''

import tkinter as tk

window = tk.Tk()
window.title("CheckList")

label = tk.Label(window, text="Selecciona los lenguajes de programación que conozcas:", font=("Arial", 10), fg="black", bg="white")

listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "C#")
listbox.insert(5, "JavaScript")

label.pack(pady=5, padx=5, side=tk.TOP)
listbox.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

window.mainloop()