from pathlib import Path
import tkinter as tk


def get_food_image(food_name):
    try:
        base_path = Path(__file__)
        file_path = (base_path / f"../images/{food_name}.png").resolve()
        return tk.PhotoImage(file=file_path)
    except IOError as error:
        print(str(error))


def get_food_ingredient_list(food_name):
    ingredient_list = []
    try:
        base_path = Path(__file__)
        file_path = (base_path / f"../images/{food_name}.txt").resolve()
        # To open the text file
        with open(file_path) as food_doc:
            # make splitted lines out of the file without \n
            lines = food_doc.read().splitlines()
            # add lines to a list. and check to not go to the steps
            for line in lines:
                if line == '|':
                    break
                ingredient_list.append(line)
        return ingredient_list
    except IOError as error:
        print(str(error))


def get_food_cooking_steps(food_name):
    ingredient_list = []
    try:
        base_path = Path(__file__)
        file_path = (base_path / f"../images/{food_name}.txt").resolve()
        # To open the text file
        with open(file_path) as lines:
            # this will ignore the first half of the text file and adds the second half to a list
            for line in lines:
                if "|" in line:
                    break
            for line in lines:
                line = line.strip('\n')
                # make splitted lines out of the file without \n
                ingredient_list.append(line)

        return ingredient_list
    except IOError as error:
        print(str(error))


class food:
    def __init__(self, foodname, needed_material, making_steps, picture):
        self.foodname = foodname
        self.needed_material = needed_material
        self.making_steps = making_steps
        self.picture = picture





