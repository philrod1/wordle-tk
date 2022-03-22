import tkinter
from data import words_list
from wordle_game import Wordle

class Row:

    def clicked(self, event):
        if self.active:
            index = int(str(event.widget)[-1])
            self.increment_pattern_at(index)
            self.set_after_words(Wordle.get_matches(self.word, self.pattern, self.before_words))


    def __init__(self, tk: tkinter):
        self.tk = tk
        self.before_words = []
        self.after_words = []
        self.active = False
        self.colours = ['white', 'yellow', 'green']
        self.word = '     '
        self.pattern = [0,0,0,0,0]
        self.text_boxes = []
        self.view = tk.PanedWindow(orient=tk.HORIZONTAL)
        for i, ch in enumerate(self.word):
            text = tk.Text(self.view, height=1, width=1, padx=8, font=('Courier', 16, 'bold'), name=str(i), bg='light gray')
            text.insert(tk.END, ch)
            text.configure(state=tk.DISABLED)
            text.bind("<Button-1>", self.clicked)
            self.text_boxes.append(text)
            self.view.add(text)

    
    def set_word(self, word: str):
        if len(word) == 5 and word.lower() in words_list:
            self.word = word.upper()
            for i, ch in enumerate(self.word):
                self.text_boxes[i].configure(state=self.tk.NORMAL)
                self.text_boxes[i].delete(1.0, self.tk.END)
                self.text_boxes[i].insert(self.tk.END, ch)
                self.text_boxes[i].configure(state=self.tk.DISABLED)


    def get_word(self):
        return self.word


    def get_pattern(self):
        return self.pattern


    def set_pattern_at(self, value: int, index: int):
        self.pattern[index] = value
        self.text_boxes[index].configure(bg=self.colours[value])


    def increment_pattern_at(self, index: int):
        value = self.pattern[index]
        value = (value + 1) % 3
        self.set_pattern_at(value, index)


    def get_view(self):
        return self.view
    

    def set_active(self, active: bool):
        self.active = active
        for i in range(5):
            self.set_pattern_at(self.pattern[i], i)
    

    def set_before_words(self, words: list):
        self.before_words = words
    

    def set_after_words(self, words: list):
        self.after_words = words
