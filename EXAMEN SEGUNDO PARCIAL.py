import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from time import  sleep

#Crear instancia
win=tk.Tk()
win.geometry("360x300")


#Agregar un titulo
win.title("EXAMEN SEGUNDO PARCIAL")


#Creando marco contenedor para contener todos los demas widgets
mighty = ttk.LabelFrame(win, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

def __Cancel(event=None): pass
#Desactive el cambio de tamaño de la GUI
win.resizable(0,0)



#Modifica la funcion del boton
def click_me():
    action.configure(text=number.get())

#Agregando un button
action=ttk.Button(win, text="Dame click", command=click_me)
action.grid(column=2, row=1)
    
#Modificando la etiqueta
ttk.Label(win, text="Porcentaje de llenado: ").grid(column=0, row=0)


#Agregando una entrada a text box
number=tk.StringVar()
number_entered=ttk.Entry(win,width=12,textvariable=number)
number_entered.grid(column=0, row=1)

progress_bar = ttk.Progressbar(win, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=3, row=10, pady=2) 

def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        progress_bar.update()       # have to call update() in loop
    progress_bar["value"] = 0       # reset/clear progressbar


buttons_frame = ttk.LabelFrame()
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)  

ttk.Button(buttons_frame, text="Click me", command=run_progressbar).grid(column=0, row=0, sticky='W')  





#Iniciar GUI
win.mainloop()
