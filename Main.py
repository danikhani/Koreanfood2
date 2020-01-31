import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
import Importer as importer

HEIGHT = 700
WIDTH = 500


def button_clicked():
    print("you clicked")


# Beginning of the firstpage

root = tk.Tk()
root.title('Korean Recipe')

# A canvas for a default size while starting
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# In this frame the other objects will be added
frame = tk.Frame(root, bg='white')
frame.place(  relwidth=1, relheight=1)

# the image of the foods will be called from the get_food_image function of repoter module
food_image = tk.PhotoImage(file=importer.get_food_image(2))
food_label = tk.Label(frame, image = food_image)
food_label.place(relx=0.5, rely=0.3, width=400, height=400, anchor = 'n')

# Button to close this and go to the next page
button2 = tk.Button(frame, text='Show the recipe', command=button_clicked)
button2.place(relx=0.5, rely=0.9, relwidth=0.8, relheight=0.05, anchor = 'n')

# Its the code for dropdown menu
dropdown_selected = tk.StringVar()
dropdown_selected.set("Select the desired recipe")  # Default value
food_list = ("yoyoyo",2,3)


def option_changed(*args):
    print("the user chose the value {}".format(dropdown_selected.get()))

list_of_food = tk.OptionMenu(root, dropdown_selected, *food_list)
# StringVar().trace() : https://kite.com/python/docs/Tkinter.StringVar.trace
dropdown_selected.trace("w", option_changed)
list_of_food.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.05, anchor = 'n')




root.mainloop()