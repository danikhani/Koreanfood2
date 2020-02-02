import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import Importer as importer
import gui_utilities as Gui_utilities
import tkinter.scrolledtext as scrolledtext


class Mainpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        # From here starts the code
        self.gimbab = importer.food('Gimbab')
        self.bulgogi = importer.food('Bulgogi')
        self.kimchi = importer.food('Kimchi_Jjigae')

        # In this frame the other objects will be added
        self.frame = tk.Frame(self, bg='white')
        self.frame.place(relwidth=1, relheight=1)

        self.image_frame = tk.Frame(self, bg='white')
        self.image_frame.place(relx=0.5, rely=0.2, width=400, height=450, anchor='n')

        # the image of the foods will be called from the get_food_image function of importer module
        # default image
        self.food_image = importer.get_food_image_path('food2')
        self.food_label = tk.Label(self.image_frame, image=self.food_image)
        self.food_label.pack()

        # Button to close this and go to the next page
        self.button2 = tk.Button(self.frame, text='Show the recipe', command=lambda: controller.show_frame("Secondpage"))
        # this keeps the bottom disabled at the beginninng. when user selects a food button will get enabled
        self.button2["state"] = "disabled"
        self.button2.place(relx=0.5, rely=0.9, relwidth=0.8, relheight=0.05, anchor='n')

        # Its the code for dropdown menu
        self.dropdown_selected = tk.StringVar()
        self.dropdown_selected.set("Select the desired recipe")  # Default value
        self.food_list = (self.gimbab.foodname, self.kimchi.foodname, self.bulgogi.foodname)

        self.list_of_food = tk.OptionMenu(self.frame, self.dropdown_selected, *self.food_list)
        # StringVar().trace() : https://kite.com/python/docs/Tkinter.StringVar.trace
        self.dropdown_selected.trace("w", self.option_changed)
        self.list_of_food.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.05, anchor='n')

    def option_changed(self, *args):
        # This makes the bottom usable after the user selected a menu
        self.button2["state"] = "normal"
        val = self.dropdown_selected.get()
        print("the user chose the value {}".format(self.dropdown_selected.get()))

        # Here comes the logic for the selected value in the dropdown menu
        if self.dropdown_selected.get() == self.gimbab.foodname:
            self.food_label['image'] = self.gimbab.picture
            self.controller.which_frame("Secondpage").change_needed_stuff(self.gimbab.needed_ingredient)
            self.controller.which_frame("Secondpage").change_cooking_steps(self.gimbab.making_steps)
        if self.dropdown_selected.get() == self.bulgogi.foodname:
            self.food_label['image'] = self.bulgogi.picture
            self.controller.which_frame("Secondpage").change_needed_stuff(self.bulgogi.needed_ingredient)
            self.controller.which_frame("Secondpage").change_cooking_steps(self.bulgogi.making_steps)
        if self.dropdown_selected.get() == self.kimchi.foodname:
            self.controller.which_frame("Secondpage").change_needed_stuff(self.kimchi.needed_ingredient)
            self.controller.which_frame("Secondpage").change_cooking_steps(self.kimchi.making_steps)
            self.food_label['image'] = self.kimchi.picture


class Secondpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        # codes start from here
        self.frame = tk.Frame(self)
        self.frame.place(relwidth=1, relheight=1)

        # The needed stuff to make the food:
        self.needed_stuff = Gui_utilities.text_with_scrollbar(self.frame)
        self.needed_stuff.place(relx=0.01, y=0.01, relwidth=0.8, height=200, anchor='nw')

        # The steps to make the food
        self.cooking_steps = Gui_utilities.text_with_scrollbar(self.frame)
        self.cooking_steps.place(relx=0.01, y=210, relwidth=0.9, height=450, anchor='nw')

        # Button to close this and go to the next page
        self.button2 = ttk.Button(self.frame, text='Main Page',
                                 command=lambda: controller.show_frame("Mainpage"))
        self.button2.place(relx=0.90, rely=0.01, width=80, height=30, anchor='n')

    # These two functions will set the ingredients and cooking steps.
    def change_needed_stuff(self, list_name):
        self.needed_stuff.insert_text(list_name)

    def change_cooking_steps(self, list_name):
        self.cooking_steps.insert_text(list_name)









