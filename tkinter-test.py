import tkinter as tk
from row import Row


def main():
    window = tk.Tk()
    row = Row(tk)
    row.get_view().pack()
    row.set_word('CRANE')
    window.mainloop()


if __name__ == "__main__":
    main()