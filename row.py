import tkinter
from wordle_game import get_matches

class Row:

    def clicked(self, event):
        index = int(str(event.widget)[-1])
        self.increment_pattern_at(index)
        self.game_area.update_words()


    def __init__(self, tk: tkinter, game_area):
        self.game_area = game_area
        self.tk = tk
        self.word = None
        self.colours = ['white', 'yellow', 'green']
        self.view = tk.PanedWindow(orient=tk.HORIZONTAL, height=30, width=164, bd=1, bg='#FEFEFE')
        self.pattern = [0,0,0,0,0]


    def get_word(self):
        return self.word


    def get_pattern(self):
        return self.pattern        


    def increment_pattern_at(self, index: int):
        if self.word[index] != ' ':
            value = self.pattern[index]
            value = (value + 1) % 3
            self.pattern[index] = value
            self.text_boxes[index].configure(bg=self.colours[value])


    def get_view(self):
        return self.view
    

    def set_word(self, word: str):
        self.word = word
        self.text_boxes = []
        for i, ch in enumerate(self.word):
            text = self.tk.Text(self.view, height=1, width=1, padx=8, font=('Consolas', 16, 'bold'), name=str(i), bg='light gray')
            text.insert(self.tk.END, ch)
            text.configure(state=self.tk.DISABLED)
            text.bind("<Button-1>", self.clicked)
            self.text_boxes.append(text)
            self.view.add(text)


    def get_matches(self, words: list):
        if self.word is None:
            return words
        return get_matches(self.word, self.pattern, words)