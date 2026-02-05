import tkinter as tk
from game_logic import GameLogic
from gameplay_frames import GameplayFrames
from start_frames import StartFrames 
from settings_frames import SettingsFrames


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("430x500") 
        self.root.config(bg="#19191D")

        self.player1_symbol = tk.StringVar(value='')
        self.player2_symbol = tk.StringVar(value = '')
        self.starting_player = tk.StringVar(value='')
        self.player1_name = tk.StringVar(value='Player1')
        self.player2_name = tk.StringVar(value='Player2')

        self.circle_symbol = '○' 
        self.cross_symbol = '✕'

        self.current_frame = None
        self.frame_history = []
        self.logic = GameLogic()
        self.gameplay = GameplayFrames(self.root, self, self.COLORS)
        self.settings = SettingsFrames(self.root, self, self.COLORS)
        self.start = StartFrames(self.root, self, self.COLORS)
  

    COLORS = { 
            'red': '#931F1D',
            'btn_topbar_bg': '#2b2b2b',
            'graphite': '#3a3a3a',
            'bg_main': '#19191D',
            'charcoal': '#2B2B2F',
            'blue': '#1565c0',
            'dark_blue': '#052242',
            'dark_red': '#520A09',
            'gray': '#555555',
            'green': '#154C1D',
            'dark_green': '#0C2B11',
            'yellow': '#BF9625',
            'silver': '#C9C9C9',
            'off-white': '#EAEAEA',
            'dim_gray':'#646466',
            'white': '#FFFFFF',
            'rosy_granite': '#9E9C9C'
        }


    def show_frame(self, new_frame):
            if self.current_frame is not None:
                self.current_frame.pack_forget()
                if self.current_frame != self.gameplay.game_over_frame:
                    self.frame_history.append(self.current_frame)
                else:
                    self.frame_history.pop()
                    
            self.current_frame = new_frame
            self.current_frame.pack(expand = True, fill = 'both')


    def go_to_previous_frame(self):
        if self.frame_history:
            self.current_frame.pack_forget()
            self.current_frame = self.frame_history.pop()
            if self.current_frame == self.settings.difficulty_level_frame:
                self.settings.clean_choices()
                self.settings.symbol_selection_subframe.pack(pady = 20, fill = 'x')
                self.settings.who_starts_subframe.pack_forget()
                self.settings.start_game_button.pack_forget()
            self.current_frame.pack(expand = True, fill = 'both')


    #-------------------------------------------------------
    #--------------------TOPBAR SUBFRAME--------------------
    def create_topbar(self, parent, bgc, show_back = False, show_rules = False, back_command = None):
        topbar = tk.Frame(parent, pady = 5, bg = bgc)

        btn_style = {
            'font' : ('Comic Sans', 17, 'bold'),
            'relief': 'flat', 
            'bd': 0,
            'highlightthickness':0,
            'bg': self.COLORS['btn_topbar_bg'],
            'fg' :self.COLORS['white'],
            'activebackground': self.COLORS['graphite'],
            'activeforeground': self.COLORS['white'],
            'cursor': 'hand2'
        }
        if show_back:
            if back_command:
                back_button = tk.Button(topbar, text ='<', command = back_command, **btn_style)
            else:
                back_button = tk.Button(topbar, text ='<', command = self.go_to_previous_frame, **btn_style)
            back_button.pack(side = 'left')

        if show_rules:
            rules_button = tk.Button(topbar, **btn_style, text = '?', command = lambda: self.show_frame(self.start.rules_frame),)
            rules_button.pack(side = 'right')

        topbar.pack(fill = 'x')






if __name__ == '__main__':
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()















