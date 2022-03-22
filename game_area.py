import tkinter
from grid import Grid
from words import Words

class GameArea:

    def __init__(self, tk: tkinter, window):
        self.tk = tk
        self.view = tk.PanedWindow(orient=tk.HORIZONTAL)
        self.grid = Grid(tk)
        self.words = Words(tk, window)
        self.view.add(self.grid.get_view())
        self.view.add(self.words.get_view())
        self.grid.get_view().grid(column=0, row=0)
        self.words.get_view().grid(column=1, row=0)
        # self.grid.get_view().pack(side=tk.LEFT)
        # self.words.get_view().pack(side=tk.RIGHT)

    
    def get_view(self):
        return self.view
    

    def set_word(self, word: str):
        self.grid.set_word(word)
    

    def set_words(self, words: list):
        self.words.set_words(words)
