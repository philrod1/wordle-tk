from game_area import GameArea
from data import words_list

class Qwordle:

    def __init__(self, tk):
        self.view = tk.PanedWindow()
        
        self.game_areas = [
            GameArea(tk, words_list),
            GameArea(tk, words_list), 
            GameArea(tk, words_list), 
            GameArea(tk, words_list)]

        self.game_areas[0].get_view().grid(column=0, row=0, sticky="n")
        self.game_areas[1].get_view().grid(column=1, row=0, sticky="n")
        self.game_areas[2].get_view().grid(column=0, row=1, sticky="n")
        self.game_areas[3].get_view().grid(column=1, row=1, sticky="n")
    

    def get_view(self):
        return self.view
    

    def set_word(self, word: str):
        for game_area in self.game_areas:
            game_area.set_word(word)
            game_area.update_words()