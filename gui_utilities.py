import tkinter as tk


class text_with_scrollbar(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        scrollbar = tk.Scrollbar(self)
        textfield = tk.Text(self, height=4, width=50)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        textfield.pack(side=tk.LEFT, fill=tk.Y)
        scrollbar.config(command=textfield.yview)
        textfield.insert(tk.END, 'text')

    def insert_text(self, listname):
        for x in listname:
            self.textfield.insert(tk.END, x + '\n')

