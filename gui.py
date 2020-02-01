import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import Importer as importer


class Mainpage:
    def __init__(self, master):
        self.HEIGHT = 700
        self.WIDTH = 500
        self.master = master

        # A canvas for a default size while starting
        self.canvas = tk.Canvas(self.master, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        # In this frame the other objects will be added
        self.frame = tk.Frame(self.master, bg='white')
        self.frame.place(relwidth=1, relheight=1)

        # the image of the foods will be called from the get_food_image function of importer module
        self.food_image = tk.PhotoImage(file=importer.get_food_image(2))
        self.food_label = tk.Label(self.frame, image=self.food_image)
        self.food_label.place(relx=0.5, rely=0.3, width=400, height=400, anchor='n')

        # Button to close this and go to the next page
        self.button2 = tk.Button(self.frame, text='Show the recipe', command=self.button_clicked)
        self.button2.place(relx=0.5, rely=0.9, relwidth=0.8, relheight=0.05, anchor='n')

        # Its the code for dropdown menu
        self.dropdown_selected = tk.StringVar()
        self.dropdown_selected.set("Select the desired recipe")  # Default value
        self.food_list = ("yoyoyo", 2, 3)

        self.list_of_food = tk.OptionMenu(self.frame, self.dropdown_selected, *self.food_list)
        # StringVar().trace() : https://kite.com/python/docs/Tkinter.StringVar.trace
        self.dropdown_selected.trace("w", self.option_changed)
        self.list_of_food.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.05, anchor='n')

    def button_clicked(self):
        print("you clicked")

    def option_changed(self, *args):
        print("the user chose the value {}".format(self.dropdown_selected.get()))
