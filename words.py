import tkinter
from tkinter.scrolledtext import ScrolledText

class Words:

    def __init__(self, tk: tkinter, window):
        self.tk = tk
        self.words = []
        self.view = ScrolledText(window, wrap = tk.WORD, width = 8, height = 15)
        self.view.configure(state=self.tk.DISABLED)


    def get_view(self):
        return self.view
    

    def set_words(self, words: list):
        self.view.configure(state=self.tk.NORMAL)
        self.words = words
        self.view.delete(0.0, self.tk.END)
        for word in words:
            self.view.insert(self.tk.INSERT, word + "\n")
        self.view.configure(state=self.tk.DISABLED)
