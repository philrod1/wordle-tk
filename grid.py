import tkinter
from row import Row
from data import words_list

class Grid:

    def __init__(self, tk: tkinter):
        self.tk = tk
        self.view = tk.PanedWindow(orient=tk.VERTICAL)
        self.rows = []
        for _ in range(8):
            row = Row(tk)
            self.view.add(row.get_view())
            # row.get_view().pack()
            self.rows.append(row)
        self.rows[0].set_active(True)
        self.active_row = 0
    

    def get_view(self):
        return self.view
    

    def set_word(self, word: str):
        if len(word) == 5 and word.lower() in words_list:
            self.rows[self.active_row].set_word(word)
            self.active_row = self.active_row + 1
            self.rows[self.active_row].set_active(True)