import tkinter as tk
import gui as gui
from Timer.Timer_gui import View
import tkinter.ttk as ttk
from pathlib import Path


def main():
    root = tk.Tk()
    root.title('Korean Recipe')
    app = gui.Mainpage(root)
    root.mainloop()


    view = View()


if __name__ == '__main__':
    main()