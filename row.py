import tkinter


class Row:

    def clicked(self, event):
        print(event.widget)


    def __init__(self, tk: tkinter):
        self.tk = tk
        self.word = '12345'
        self.pattern = [0,0,0,0,0]
        self.text_boxes = []
        self.view = tk.PanedWindow(orient=tk.HORIZONTAL)
        for i, ch in enumerate(self.word):
            text = tk.Text(self.view, height=1, width=1, padx=8, font=('Courier', 16, 'bold'))
            text.insert(tk.END, ch)
            text.configure(state=tk.DISABLED)
            text.pack()
            text.bind("<Button-1>", self.clicked)
            self.text_boxes.append(text)
            self.view.add(text)

    
    def set_word(self, word: str):
        self.word = word
        for i, ch in enumerate(self.word):
            self.text_boxes[i].configure(state=self.tk.NORMAL)
            self.text_boxes[i].delete(1.0, self.tk.END)
            self.text_boxes[i].insert(self.tk.END, ch)
            self.text_boxes[i].configure(state=self.tk.DISABLED)


    def get_word(self):
        return self.word


    def set_pattern(self, pattern: list):
        self.pattern = pattern


    def get_pattern(self):
        return self.pattern


    def set_pattern_at(self, value: int, index: int):
        self.pattern[index] = value


    def get_view(self):
        return self.view
