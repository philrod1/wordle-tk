import tkinter
from row import Row
from data import words_list

class Grid:

    def __init__(self, tk: tkinter, game_area):
        self.tk = tk
        self.view = tk.PanedWindow(orient=tk.VERTICAL)
        self.rows = []
        for _ in range(8):
            row = Row(tk, game_area)
            self.rows.append(row)
            self.view.add(row.get_view())
        self.row_index = 0
    

    def get_view(self):
        return self.view
    

    def set_word(self, word: str):
        if len(word) == 5 and word.lower() in words_list:
            row = self.rows[self.row_index] 
            row.set_word(word.upper())
            self.row_index += 1
    

    def get_matches(self, words: list):
        matches = words
        for row in self.rows:
            matches = row.get_matches(matches)
        return matches