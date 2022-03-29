from tkinter.scrolledtext import ScrolledText

class Words:

    def __init__(self, tk):
        self.tk = tk
        self.words = []
        self.view = tk.PanedWindow()
        self.text = ScrolledText(self.view, wrap = tk.WORD, width = 8, height = 15)
        self.text.configure(state=self.tk.DISABLED)
        self.view.add(self.text)


    def get_view(self):
        return self.view
    

    def set_words(self, words: list):
        self.text.configure(state=self.tk.NORMAL)
        self.words = words
        self.text.delete(0.0, self.tk.END)
        for word in words:
            self.text.insert(self.tk.INSERT, word + "\n")
        self.text.configure(state=self.tk.DISABLED)
