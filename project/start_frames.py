import tkinter as tk

class StartFrames:
    def __init__(self, master, app, colors):
        self.master = master
  
        self.COLORS = colors
        self.app = app
        self.create_rules_frame()
        self.create_start_frame()
        self.app.show_frame(self.start_frame)
        
    #----------------------------------------------------------------------
    #---------------------------START FRAME--------------------------------
    def create_start_frame(self):
        self.start_frame = tk.Frame(self.master, padx = 20, pady = 20, bg = self.COLORS['bg_main'])

    #------------TOPBAR SUBFRAME----------------
        self.app.create_topbar(self.start_frame, show_back = False, show_rules = True, bgc = self.COLORS['bg_main'])

    #----------MAIN CONTENT SUBFRAME------------
        main_content_subframe = tk.Frame(self.start_frame, pady = 5, bg = self.COLORS['bg_main'])

        title_label = tk.Label(main_content_subframe, text = 'TIC TAC TOE', font = ('Courier New', 35, 'bold'), bg = self.COLORS['bg_main'], fg = self.COLORS['off-white'])
        title_label.pack(pady = 40)

        gm_button_style = {
            'font': ('Sans-serif', 15, 'bold'), 
            'relief': 'flat',
            'bd': 0,
            'padx': 25,
            'activeforeground' :self.COLORS['white'],
            'pady' :12,
            'cursor':'hand2', 
            'fg' : self.COLORS['white']
        }

        single_player_button = tk.Button(main_content_subframe, 
                                         text = '▶ PLAY WITH COMPUTER', 
                                         bg = self.COLORS['blue'], 
                                         command = lambda: self.set_game_mode('computer'),
                                         activebackground=self.COLORS['dark_blue'],
                                         **gm_button_style
                                         )           
        single_player_button.pack(pady = 15, padx = 30,fill = 'x')

        with_friend_button = tk.Button(main_content_subframe, 
                                       text = '▶ PLAY WITH FRIEND', 
                                       bg = self.COLORS['red'],  
                                       command = lambda: self.set_game_mode('friend'),
                                       activebackground=self.COLORS['dark_red'],
                                       **gm_button_style
                                        )
        with_friend_button.pack(pady = 15, padx = 30, fill = 'x')
        main_content_subframe.pack(fill = 'x')


    def set_game_mode(self, mode):
        self.app.logic.game_mode = mode
        self.app.settings.create_game_settings_frame()
        if mode == 'computer':    
            self.app.show_frame(self.app.settings.difficulty_level_frame)
        else:
            self.app.show_frame(self.app.settings.game_settings_frame)


  #----------------------------------------------------------------------
    #---------------------------RULES FRAME--------------------------------
    def create_rules_frame(self):
        self.rules_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = self.COLORS['charcoal'])

    #------------TOPBAR SUBFRAME----------------------
        self.app.create_topbar(self.rules_frame, show_back = True, bgc = self.COLORS['charcoal'])
    
    #------------MAIN CONTENT SUBFRAME----------------
        main_content_subframe = tk.Frame(self.rules_frame, pady = 5, bg = self.COLORS['charcoal'])

        rules_title_label = tk.Label(main_content_subframe, text = 'HOW TO PLAY?', font = ('Courier New', 28, 'bold'), bg = self.COLORS['charcoal'], fg = self.COLORS['off-white'])
        rules_title_label.pack(pady = (5, 20))

        rules_explanation_label = tk.Label(main_content_subframe, 
                                           text = "Tic Tac Toe is a simple game for two players on a 3x3 board.\n"
                                                "Players take turns placing their symbols in empty spaces.\n"
                                                "The first to get three of their symbols in a row — horizontally, vertically, or diagonally — wins.\n"
                                                "If all spaces are filled and no one wins, the game ends in a tie.\n\n"
                                                "You can play with a friend or challenge the computer, which definitely won't let you win easily.", 
                                            bg = self.COLORS['charcoal'], 
                                            justify='center', 
                                            fg = '#B6B6B8',
                                            wraplength=350, 
                                            font = ('Courier New', 12, 'bold')
                                            )
        rules_explanation_label.pack(pady = 10)

        main_content_subframe.pack(fill = 'x')


