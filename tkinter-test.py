import tkinter as tk
from data import words_list
from qwordle import Qwordle


def main():

    window = tk.Tk()
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    qwordle = Qwordle(tk)

    qwordle.get_view().grid(column=0, row=0, sticky="n")

    def enter_key(event):
        word = entry_text.get()
        if len(word) == 5 and word.lower() in words_list:
            qwordle.set_word(word)
            entry_text.set('')

    entry_text = tk.StringVar()
    entry_widget = tk.Entry(window, width=20, textvariable=entry_text)
    
    entry_widget.bind('<Return>', enter_key)

    def character_limit(entry_text):
        if len(entry_text.get()) > 5:
            entry_text.set(entry_text.get()[:5])

    entry_text.trace("w", lambda *args: character_limit(entry_text))
    entry_widget.grid(column=0, row=1, sticky="s")
    entry_widget.focus()

    window.mainloop()


if __name__ == "__main__":
    main()