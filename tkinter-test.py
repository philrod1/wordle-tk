import tkinter as tk
from game_area import GameArea
from grid import Grid
from data import words_list


def main():

    window = tk.Tk()
    game_area = GameArea(tk, window)
    game_area.get_view().grid(column=0, row=0)
    game_area.set_words(words_list)

    def enter_key(event):
        word = entry_text.get()
        if len(word) == 5 and word.lower() in words_list:
            game_area.set_word(word)
            entry_text.set('')

    entry_text = tk.StringVar()
    entry_widget = tk.Entry(window, width = 20, textvariable = entry_text)
    entry_widget.bind('<Return>', enter_key)
    def character_limit(entry_text):
        if len(entry_text.get()) > 5:
            entry_text.set(entry_text.get()[:5])

    entry_text.trace("w", lambda *args: character_limit(entry_text))
    entry_widget.grid(column=0, row=1)
    entry_widget.focus()

    window.mainloop()


if __name__ == "__main__":
    main()