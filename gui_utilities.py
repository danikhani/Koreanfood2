import tkinter as tk


class text_with_scrollbar(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.scrollbar = tk.Scrollbar(self)
        self.textfield = tk.Text(self, height=4, width=50)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textfield.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.config(command=self.textfield.yview)
        self.textfield.insert(tk.END, 'text')

    def insert_text(self, listname):
        for x in listname:
            self.textfield.insert(tk.END, x + '\n')

