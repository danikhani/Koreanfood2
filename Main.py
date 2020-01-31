import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import Importer as importer

HEIGHT = 700
WIDTH = 500

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(  relwidth=1, relheight=1)

food_image = tk.PhotoImage(file=importer.getimage(2))
food_label = tk.Label(frame, image = food_image)
food_label.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

button2 = tk.Button(frame, text = 'Show the recipe')
button2.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.05)


list_of_food = ttk.Combobox(frame, state='readonly')
list_of_food['values'] = ("Plesae select a food",1,2,3)
list_of_food.current(0)
list_of_food.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)

#button = tk.Button(frame, text = 'test')
#button.pack(side='bottom', fill='x')


root.mainloop()