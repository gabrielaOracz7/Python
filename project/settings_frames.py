import tkinter as tk
from tkinter import messagebox


class SettingsFrames:
    def __init__(self, master, app, colors):
        self.master = master
  
        self.COLORS = colors
        self.app = app
        self.create_difficulty_level_frame()


    #----------------------------------------------------------------------
    #--------------------DIFFICULTY LEVEL FRAME----------------------------
    def create_difficulty_level_frame(self):
        self.difficulty_level_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = self.COLORS['bg_main'])
        
    #------------TOPBAR SUBFRAME--------------------
        self.app.create_topbar(self.difficulty_level_frame, show_back = True, bgc = self.COLORS['bg_main'])

        difficulty_title_label = tk.Label(
            self.difficulty_level_frame, 
            text = 'SELECT DIFFICULTY', 
            font = ('Courier New', 25, 'bold'), 
            bg = self.COLORS['bg_main'], 
            fg = self.COLORS['silver']
        )
        difficulty_title_label.pack(pady = 20)

        levels = ['EASY', 'MEDIUM', 'HARD']
        colors = {
            'EASY': self.COLORS['green'],    
            'MEDIUM': self.COLORS['yellow'],  
            'HARD': self.COLORS['red']    
            }
        for lvl in levels:
            btn = tk.Button(self.difficulty_level_frame, 
                            text = lvl, 
                            bg = colors[lvl], 
                            font = ('Sans-serif', 15, 'bold'), 
                            command = lambda l = lvl: self.select_difficulty(l),
                            activebackground=self.COLORS['gray'],  
                            activeforeground=self.COLORS['white'],
                            relief='flat',
                            bd=0,
                            padx=20,
                            pady=12,
                            cursor='hand2'
                            )        
            btn.pack(pady = 10, padx = 50, fill = 'x')


    def select_difficulty(self, lvl):
        self.app.logic.selected_difficulty = lvl
        self.app.show_frame(self.game_settings_frame)




 

    #----------------------------------------------------------------------
    #-----------------------GAME SETTINGS FRAME----------------------------
    def clean_choices(self):
        self.app.player1_symbol.set('')  
        self.app.player2_symbol.set('')  
        self.app.starting_player.set('')


    def create_game_settings_frame(self):
        self.clean_choices()
        self.game_settings_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = self.COLORS['bg_main'])
           
        self.app.create_topbar(self.game_settings_frame, show_back = True, bgc = self.COLORS['bg_main'])

        if self.app.logic.game_mode == 'friend':
            self.create_nicknames_subframe()
        else:
            self.app.player1_name.set('You')
            self.app.player2_name.set('Computer')

        label_kwargs = {
            'font' : ('Courier New', 20, 'bold'), 
            'bg' : self.COLORS['bg_main'],
            'fg': self.COLORS['silver']
        }

    #------------SYMBOL SELECTION SUBFRAME------------
        self.symbol_selection_subframe = tk.Frame(self.game_settings_frame, pady = 5, bg = self.COLORS['bg_main'])

        symbol_selection_label = tk.Label(self.symbol_selection_subframe, text = '', **label_kwargs )
        symbol_selection_label.grid(row = 0, column = 0, columnspan = 2)

        if self.app.logic.game_mode == 'computer':
            symbol_selection_label.config(text = 'PICK YOUR SYMBOL')
        else:
            symbol_selection_label.config(text = f'PICK SYMBOL FOR Player1')

        button_style = {
            'font': ('Segoe UI', 28, 'bold'),
            'bg': self.COLORS['charcoal'],
            'fg': self.COLORS['white'],
            'width': 6,
            'indicatoron': 0,   
            'relief': 'flat',
            'activebackground': self.COLORS['graphite'],
            'activeforeground': self.COLORS['white'],
            'selectcolor': self.COLORS['blue'],  
            'cursor': 'hand2',
            'command': self.show_who_starts_sf
        }
        x_button = tk.Radiobutton(self.symbol_selection_subframe, text=self.app.cross_symbol, variable=self.app.player1_symbol, value= self.app.cross_symbol, **button_style)
        o_button = tk.Radiobutton(self.symbol_selection_subframe, text=self.app.circle_symbol, variable=self.app.player1_symbol, value= self.app.circle_symbol,  **button_style)

        self.symbol_selection_subframe.columnconfigure(0, weight=1)
        self.symbol_selection_subframe.columnconfigure(1, weight=1)

        x_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        o_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        self.symbol_selection_subframe.pack(pady=20, fill='x')

        if self.app.logic.game_mode == 'friend':
            self.symbol_selection_subframe.config(pady=10)

    #--------------WHO STARTS SUBFRAME------------------
        self.who_starts_subframe = tk.Frame(self.game_settings_frame, bg = self.COLORS['bg_main'])
        
        who_starts_label = tk.Label(self.who_starts_subframe,  text = 'WHO STARTS?', **label_kwargs)
        who_starts_label.grid(row = 0, column = 0, columnspan = 3)

        ws_button_style = {
            'font': ('Segoe UI', 13, 'bold'),
            'bg': self.COLORS['charcoal'],
            'fg': self.COLORS['white'],
            'width': 8,
            'indicatoron': 0,   
            'relief': 'flat',
            'activebackground': self.COLORS['graphite'],
            'activeforeground': self.COLORS['white'],
            'selectcolor': self.COLORS['red'],  
            'cursor': 'hand2',
            'command': self.show_start_game_btn,
            'pady' : 5
        }
        ws1_button = tk.Radiobutton(
            self.who_starts_subframe,
            variable=self.app.starting_player,
            value='player1',
            **ws_button_style
        )
        ws2_button = tk.Radiobutton(
            self.who_starts_subframe,
            variable=self.app.starting_player,
            value='player2',
            **ws_button_style
        )
        ws3_button = tk.Radiobutton(
            self.who_starts_subframe,
            text='?',
            variable=self.app.starting_player,
            value='random',
            **ws_button_style
        )

        if self.app.logic.game_mode == 'friend':
            ws1_button.config(text = 'PLAYER 1')
            ws2_button.config(text = 'PLAYER 2')

        else:
            ws1_button.config(text = 'YOU')
            ws2_button.config(text = 'COMPUTER')

        self.who_starts_subframe.columnconfigure(0, weight=1)
        self.who_starts_subframe.columnconfigure(1, weight=1)
        self.who_starts_subframe.columnconfigure(2, weight=1)

        ws1_button.grid(row=1, column=0, padx=5, pady=5, sticky = 'nsew')
        ws2_button.grid(row=1, column=1, padx=5, pady=5, sticky = 'nsew')
        ws3_button.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = 'nsew')

        self.start_game_button = tk.Button(
            self.game_settings_frame, 
            text = 'START GAME', 
            font = ('Segoe UI', 20, 'bold'), 
            bg = self.COLORS['green'],
            activebackground= self.COLORS['dark_green'],  
            relief = 'flat',
            bd=0,
            fg = self.COLORS['silver'],
            padx=30,
            pady=12,
            cursor='hand2',
            activeforeground= self.COLORS['dim_gray'],
            command = self.app.gameplay.start_game
        )


    #--------------NICKNAMES SUBFRAME------------------
    def create_nicknames_subframe(self): 
        nicknames_subframe = tk.Frame(self.game_settings_frame, bg = self.COLORS['bg_main'], pady=5)

        nicknames_title_label = tk.Label(
            nicknames_subframe, 
            text = 'SET NICKNAMES', 
            bg = self.COLORS['bg_main'], 
            font = ('Courier New', 20, 'bold'),
            fg = self.COLORS['silver']
        )
        nicknames_title_label.grid(row = 0, column = 0, columnspan = 2, pady = (5, 10))
        nicknames_subframe.columnconfigure(0, weight=1)
        nicknames_subframe.columnconfigure(1, weight=1)

        self.app.player1_name.set('Player1')
        self.app.player2_name.set('Player2')

        label_kwargs = {
            'bg':self.COLORS['bg_main'],
            'fg' : self.COLORS['off-white'],
            'font': ('Sans-serif', 12, 'bold'),
            'padx' : 10,
            'pady': 5
        }
        tk.Label(nicknames_subframe, text="Player1:", **label_kwargs).grid(row = 1, column = 0, padx=5, sticky = 'nsew')
        tk.Label(nicknames_subframe, text="Player2:", **label_kwargs).grid(row=1, column=1, padx=5, sticky = 'nsew')

        entry_kwargs = {
            'font':('Segoe UI', 12),
            'bg':self.COLORS['charcoal'],
            'fg':self.COLORS['white'],
            'insertbackground':self.COLORS['white'],   
            'relief':'flat',
            'bd':0,
            'highlightbackground': self.COLORS['white'],  
            'highlightcolor': self.COLORS['white'],      
            'highlightthickness' :1
        }
        tk.Entry(nicknames_subframe, textvariable=self.app.player1_name, **entry_kwargs).grid(row = 2, column=0, padx=5, sticky = 'nsew')
        tk.Entry(nicknames_subframe, textvariable=self.app.player2_name, **entry_kwargs).grid(row=2, column=1, padx=5, sticky = 'nsew')
        
        nicknames_subframe.pack(fill = 'x')


    def validate_nicknames(self):
        max_length = 10
        nick1 = self.app.player1_name.get().strip()
        nick2 = self.app.player2_name.get().strip()
        if len(nick1) > max_length or len(nick2) > max_length:
            messagebox.showwarning(
            "Invalid nickname",
            f"Nicknames cannot be longer than {max_length} characters!\n"
            )
            return False
        if nick1 == "":
            self.app.player1_name.set('Player1')
        if nick2 == "":
            self.app.player2_name.set('Player2')
        return True


    def show_who_starts_sf(self):
        self.app.player2_symbol.set(self.get_opposite_symbol(self.app.player1_symbol.get())) 
        if not self.who_starts_subframe.winfo_ismapped():
            self.who_starts_subframe.pack(pady = 0, fill = 'x')


    def get_opposite_symbol(self, symbol):
        return self.app.circle_symbol if symbol == self.app.cross_symbol else self.app.cross_symbol


    def show_start_game_btn(self):
        if not self.start_game_button.winfo_ismapped():
            if self.app.logic.game_mode == 'computer':
                pady_value = (60, 10)
            else:
                pady_value = (15,5)
            self.start_game_button.pack(pady = pady_value, padx = 30, fill = 'x')    


