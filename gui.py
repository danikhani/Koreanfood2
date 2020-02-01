import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import Importer as importer
import gui_utilities as Gui_utilities
import tkinter.scrolledtext as scrolledtext


class Mainpage:

    def __init__(self, master):
        self.HEIGHT = 700
        self.WIDTH = 500
        self.master = master
        self.gimbab = importer.food('gimbab')



        # A canvas for a default size while starting
        self.canvas = tk.Canvas(self.master, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        # In this frame the other objects will be added
        self.frame = tk.Frame(self.master, bg='white')
        self.frame.place(relwidth=1, relheight=1)

        self.image_frame = tk.Frame(self.master, bg='white')
        self.image_frame.place(relx=0.5, rely=0.2, width=400, height=450, anchor='n')

        # the image of the foods will be called from the get_food_image function of importer module
        #self.food_image = tk.PhotoImage(file=importer.get_food_image('food'))
        self.food_image = tk.PhotoImage(file=importer.get_food_image_path('food2'))
        self.food_label = tk.Label(self.image_frame, image=self.food_image)
        self.food_label.pack()
        #self.food_label.place(relx=0.5, rely=0.3, width=400, height=400, anchor='n')

        # Button to close this and go to the next page
        self.button2 = tk.Button(self.frame, text='Show the recipe', command=self.button_clicked)
        # this keeps the bottom disabled at the beginninng. when user selects a food button will get enabled
        self.button2["state"] = "disabled"
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
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        app = Secondpage(toplevel, self.dropdown_selected.get())
        #print("you clicked")

    def option_changed(self, *args):
        # This makes the bottom usable after the user selected a menu
        self.button2["state"] = "normal"
        val = self.dropdown_selected.get()
        print("the user chose the value {}".format(self.dropdown_selected.get()))
        #self.food_label['image']=self.food_image2


class Secondpage:
    def __init__(self, master, foodtype):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.place(relwidth=1, relheight=1)
        self.foodtype = foodtype


        print('you clicked ' + self.foodtype)

        # The needed stuff to make the food:
        self.needed_stuff = Gui_utilities.text_with_scrollbar(self.frame)
        self.needed_stuff.place(relx=0.01, y=0.01, relwidth=0.8, height=200, anchor='nw')

        # The steps to make the food
        self.cooking_steps = Gui_utilities.text_with_scrollbar(self.frame)
        self.cooking_steps.place(relx=0.01, y=210, relwidth=0.9, height=450, anchor='nw')

    def close_windows(self):
        self.master.destroy()








