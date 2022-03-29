import tkinter
from grid import Grid
from words import Words

class GameArea:

    def __init__(self, tk: tkinter, words: list):
        self.tk = tk
        self.words = words
        self.view = tk.PanedWindow(orient=tk.HORIZONTAL, bd=1, bg='black')
        self.words_panel = Words(tk)
        self.words_panel.set_words(words)
        self.grid = Grid(tk, self)
        self.view.add(self.grid.get_view())
        self.view.add(self.words_panel.get_view())

    
    def get_view(self):
        return self.view
    

    def set_word(self, word: str):
        self.grid.set_word(word)
        print(str(self) + " " + word)
    

    def update_words(self):
        self.words_panel.set_words(self.grid.get_matches(self.words))
