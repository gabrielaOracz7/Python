import tkinter as tk
from tkinter import messagebox
import random


class GameplayFrames:
    def __init__(self, master, app, colors):
        self.master = master
        self.COLORS = colors
        self.app = app
        self.create_game_over_frame()
        self.create_game_frame()

    CELL_SIZE = 80
    PADDING = 5
    RADIUS = 25

    #----------------------------------------------------------------------
    #-----------------------------GAME FRAME-------------------------------
    def create_game_frame(self):
        self.game_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = self.COLORS['bg_main'])

        self.app.create_topbar(self.game_frame, show_back = True, bgc = self.COLORS['bg_main'], back_command = self.confirm_exit_game)  

    #----------------PLAYERS SUBFRAME------------------
        self.players = self.create_players_panel(self.game_frame, show_turn_label = True)
        self.canvas, self.cells = self.create_board(parent = self.game_frame, clickable = True)


    def create_players_panel(self, parent, show_turn_label = True):
        panel = tk.Frame(parent, bg = self.COLORS['bg_main'])
        panel.pack(fill = 'x', pady = (0, 10))
        panel.columnconfigure(0, weight = 1, minsize = 150)
        panel.columnconfigure(1, weight = 1, minsize = 150)

        player_sl_style = {
            'font': ('Segoe', 30, 'bold'),
            'bg': self.COLORS['bg_main'],
            'fg': self.COLORS['silver']
        }

        player_nl_style = {
            'font': ('Sans-serif', 15, 'bold'),
            'bg': self.COLORS['bg_main'],
            'fg': self.COLORS['white']
        }

        p1_tile = tk.Frame(panel, bg = self.COLORS['bg_main'], padx = 10, pady = 10)
        p1_tile.grid(row = 0, column = 0, sticky = 'nsew', padx = 5)

        p1_symbol = tk.Label(p1_tile, textvariable = self.app.player1_symbol, **player_sl_style)
        p1_symbol.pack(fill = 'both', expand = True)

        p1_name = tk.Label(p1_tile, textvariable = self.app.player1_name, **player_nl_style)
        p1_name.pack(fill = 'both', expand = True)

        p2_tile = tk.Frame(panel, bg = self.COLORS['bg_main'], padx = 10, pady = 10)
        p2_tile.grid(row = 0, column = 1, sticky = 'nsew', padx = 5)

        p2_symbol = tk.Label(p2_tile, textvariable = self.app.player2_symbol, **player_sl_style)
        p2_symbol.pack(fill = 'both', expand = True)

        p2_name = tk.Label(p2_tile, textvariable = self.app.player2_name, **player_nl_style)
        p2_name.pack(fill = 'both', expand = True)

        turn_label = None
        if show_turn_label:
            turn_label = tk.Label(
                panel,
                text = '',
                bg = self.COLORS['bg_main'],
                fg = self.COLORS['silver'],
                font = ('Segoe UI', 12)
            )

        return {
            'panel': panel,
            'p1_tile': p1_tile,
            'p2_tile': p2_tile,
            'turn_label': turn_label
        }


    def create_board(self, parent, clickable = True):
        canvas = tk.Canvas(
            parent, 
            width = 3 * self.CELL_SIZE, 
            height = 3 * self.CELL_SIZE, 
            bg = self.COLORS['bg_main'], 
            highlightthickness = 0
        )      
        canvas.pack(pady = 20)
        cells = {}

        for r in range(3):
            for c in range(3):
                x1 = c * self.CELL_SIZE + self.PADDING
                y1 = r * self.CELL_SIZE + self.PADDING
                x2 = x1 + self.CELL_SIZE - 2 * self.PADDING
                y2 = y1 + self.CELL_SIZE - 2 * self.PADDING

                rect = self.rounded_rect(canvas, x1, y1, x2, y2, self.RADIUS, fill = self.COLORS['gray'], outline = '')
                symbol = canvas.create_text(
                    (x1 + x2) // 2,
                    (y1 + y2) // 2,
                    text = '',
                    font = ('Segoe UI', 28, 'bold'),
                    fill = self.COLORS['white']
                )
                cells[(r, c)] = (rect, symbol)
                
                if clickable:
                    canvas.tag_bind(rect, '<Button-1>', lambda e, row = r, col = c: self.handle_move(row, col))
                    canvas.tag_bind(symbol, '<Button-1>', lambda e, row = r, col = c: self.handle_move(row, col))
        return canvas, cells



    def rounded_rect(self, canvas, x1, y1, x2, y2, rad, **args):
        points = [
            x1 + rad, y1, x2 - rad, y1, x2, y1,
            x2, y1 + rad, x2, y2 - rad, x2, y2,
            x2 - rad, y2, x1 + rad, y2, x1, y2,
            x1, y2 - rad, x1, y1 + rad, x1, y1 
        ]
        return canvas.create_polygon(points, smooth = True, **args)



    def start_game(self):
        if self.app.logic.game_mode == 'friend' and not self.app.settings.validate_nicknames():
            return

        self.app.logic.initialize_game(self.app.player1_symbol.get(), self.app.player2_symbol.get())

        for rect, symbol in self.cells.values():
            self.canvas.itemconfig(symbol, text='')
            self.canvas.itemconfig(rect, fill='grey')     
        
        chosen_player = self.app.starting_player.get()
        if chosen_player == 'random':
            chosen_player = random.choice(['player1', 'player2'])
        if chosen_player == 'player1':
            self.app.logic.current_player = self.app.player1_name.get()
            self.app.logic.current_symbol = self.app.player1_symbol.get()
        else:
            self.app.logic.current_player = self.app.player2_name.get()
            self.app.logic.current_symbol = self.app.player2_symbol.get()           
 
        self.app.show_frame(self.game_frame)
        self.update_turn_label()

        if self.app.logic.is_computer_turn():
            self.master.after(500, self.computer_move)



    def handle_move(self, row, col): 
        if not self.app.logic.make_move(row, col):
            return

        player_id = 1 if self.app.logic.current_player == self.app.player1_name.get() else 2
        self.app.logic.game_history.append({
            'board': [r.copy() for r in self.app.logic.board], 
            'move': (row, col),  
            'player_id': player_id
        })
        _, symbol_id = self.cells[(row, col)]
        self.canvas.itemconfig(symbol_id, text = self.app.logic.current_symbol)

        winner = self.app.logic.check_winner(self.app.logic.board, self.app.logic.current_symbol, return_line = True)
        if winner:
            self.highlight_winner(winner)
            self.app.logic.game_over = True
            self.result_label.config(text = f"{self.app.logic.current_player} {'WIN!' if self.app.logic.current_player == 'You' else 'WINS!'}")
            self.update_analyze_button_visibility()
            self.master.after(1000, lambda: self.app.show_frame(self.game_over_frame))
            return
        if self.app.logic.is_board_full(self.app.logic.board):
            self.app.logic.game_over = True
            self.result_label.config(text = "It's a draw!")
            self.update_analyze_button_visibility()
            self.master.after(1000, lambda: self.app.show_frame(self.game_over_frame))
            return

        self.switch_turn()
        self.update_turn_label()

        if self.app.logic.is_computer_turn():
            self.master.after(500, self.computer_move)



    def change_tile_colors(self, p1_color, p2_color, panel):
        gp = panel

        gp['p1_tile'].config(bg = p1_color)
        gp['p2_tile'].config(bg = p2_color)

        for widget in gp['p1_tile'].winfo_children():
            widget.config(bg=p1_color)

        for widget in gp['p2_tile'].winfo_children():
            widget.config(bg=p2_color)



    def update_turn_label(self):
        if self.app.logic.current_player == self.app.player1_name.get():
            turn_text = f"{self.app.player1_name.get()}'s turn" if self.app.logic.game_mode == 'friend' else "Your turn"
            self.players['turn_label'].config(text=turn_text)            
            self.change_tile_colors(self.COLORS['blue'], self.COLORS['bg_main'], self.players)
            self.players['turn_label'].grid_configure(column = 0)
        else:
            self.players['turn_label'].config(text=f"{self.app.player2_name.get()}'s turn")
            self.change_tile_colors(self.COLORS['bg_main'], self.COLORS['red'], self.players)
            self.players['turn_label'].grid_configure(column = 1)
 


    def computer_move(self):
        r, c = self.app.logic.computer_strategies[self.app.logic.selected_difficulty]()
        self.handle_move(r, c)


    def switch_turn(self):
        if self.app.logic.current_player == self.app.player1_name.get():
            self.app.logic.current_player = self.app.player2_name.get()
            self.app.logic.current_symbol = self.app.player2_symbol.get()
        else:
            self.app.logic.current_player = self.app.player1_name.get()
            self.app.logic.current_symbol = self.app.player1_symbol.get()



    def highlight_winner(self, line):
        for r, c in line:
            rect, _ = self.cells[(r, c)]
            self.canvas.itemconfig(rect, fill = self.COLORS['green'])



    def confirm_exit_game(self):
        if messagebox.askyesno(
            "Exit game",
            "Are you sure you want to leave the game?\nYour progress will be lost :("
        ):
            self.app.go_to_previous_frame()





    #----------------------------------------------------------------------------------------
    #-------------------------------GAME OVER FRAME------------------------------------------
    def create_game_over_frame(self):
        self.game_over_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = self.COLORS['bg_main'])

        self.result_label = tk.Label(
            self.game_over_frame, 
            text = "", 
            bg = self.COLORS['bg_main'], 
            fg = self.COLORS['dim_gray'],
            font = ('Courier New', 28, 'bold')
        )
        self.result_label.pack(fill = 'x', expand = True)

        go_btn_style = {
            'font': ('Segoe UI', 15, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'cursor': 'hand2',
            'padx': 20,
            'pady': 12,
            'activeforeground': self.COLORS['white'],
            'fg' : self.COLORS['silver']
        }

        play_again_button = tk.Button(
            self.game_over_frame, 
            text = 'PLAY AGAIN', 
            bg = self.COLORS['green'],
            activebackground = self.COLORS['dark_green'],
            command = self.start_game, 
            **go_btn_style
        )
        play_again_button.pack(pady = 10, padx = 30, fill = 'x')
        
        new_game_button = tk.Button(
            self.game_over_frame, 
            text = 'START NEW GAME', 
            bg = self.COLORS['red'], 
            activebackground = self.COLORS['dark_red'],
            command = lambda: self.app.show_frame(self.app.start.start_frame),
            **go_btn_style
        )
        new_game_button.pack(pady = (0, 10), padx = 30, fill = 'x')
        
        self.analyze_game_button = tk.Button(
            self.game_over_frame, 
            text = 'ANALYZE GAME', 
            bg = self.COLORS['yellow'],
            activebackground = self.COLORS['dark_blue'],
            command = self.start_analysis_mode, 
            **go_btn_style
        )



    def update_analyze_button_visibility(self):
        if self.app.logic.game_mode == 'computer':
            self.analyze_game_button.pack(pady=(0, 10), padx=30, fill='x')
        else:
            self.analyze_game_button.pack_forget()



    #----------------------------------------------------------------------------------------
    #------------------------------GAME ANALYSIS FRAME---------------------------------------
    def start_analysis_mode(self):
        self.current_analysis_index = 0
        self.analysis_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = self.COLORS['bg_main'])
        
        self.app.create_topbar(self.analysis_frame, show_back = True, back_command = lambda: self.app.show_frame(self.game_over_frame), bgc = self.COLORS['bg_main'])
        self.analysys_players = self.create_players_panel(self.analysis_frame, show_turn_label = True)

        self.analysis_canvas, self.analysis_cells =  self.create_board(parent = self.analysis_frame, clickable = False)
        
        nav_frame = tk.Frame(self.analysis_frame, bg = self.COLORS['bg_main'])
        nav_frame.pack(fill = 'x', pady = (0,10))

        btn_style = {
            'font': ('Comic Sans', 17, 'bold'),
            'relief': 'flat',
            'bd': 0,
            'highlightthickness': 0,
            'bg': self.COLORS['btn_topbar_bg'],
            'fg': self.COLORS['white'],
            'activebackground': self.COLORS['graphite'],
            'activeforeground': self.COLORS['white'],
            'cursor': 'hand2'
        }

        prev_btn = tk.Button(nav_frame, text = '⟵', command = self.prev_move, **btn_style)
        prev_btn.pack(side = 'left', padx = 20)
        
        next_btn = tk.Button(nav_frame, text = '⟶', command = self.next_move, **btn_style)
        next_btn.pack(side = 'right', padx = 20)

        self.best_move_label = tk.Label(nav_frame, text = '', bg = self.COLORS['bg_main'], fg = self.COLORS['off-white'], font = ('Segoe UI', 12, 'bold'))
        self.best_move_label.pack(side = 'top', pady = (5,0))

        self.show_move(0)
        self.app.show_frame(self.analysis_frame)

    

    def show_move(self, index):
        history = self.app.logic.game_history
        if not history or index < 0 or index >= len(history):
            return
        board_state = history[index]['board']
        move = history[index]['move']
        player_id = history[index]['player_id']

        for (r, c), (rect, symbol) in self.analysis_cells.items():
            self.analysis_canvas.itemconfig(symbol, text = '')
            self.analysis_canvas.itemconfig(rect, fill = self.COLORS['gray'])

        for r in range(3):
            for c in range(3):
                symbol = board_state[r][c]
                if symbol:
                    _, symbol_id = self.analysis_cells[(r, c)]
                    self.analysis_canvas.itemconfig(symbol_id, text = symbol)

        if move:
            r, c = move
            rect, _ = self.analysis_cells[(r, c)]
            self.analysis_canvas.itemconfig(rect, fill = self.COLORS['rosy_granite'])

        if player_id == 1:  #tylko człowiek
            board_before = history[index-1]['board'] if index > 0 else [[''] * 3 for _ in range(3)]
            best_moves = self.app.logic.get_best_human_move(board_before)

            if best_moves:
                if move in best_moves:
                    r_best, c_best = move
                else:    
                    r_best, c_best = random.choice(best_moves)
                rect, _ = self.analysis_cells[(r_best, c_best)]
                self.analysis_canvas.itemconfig(rect, fill = self.COLORS['green'])
                self.best_move_label.config(text = f"Best move {r_best}, {c_best}")
        else:
            self.best_move_label.config(text = "")
        self.update_analysis_player_colors(player_id)



    def update_analysis_player_colors(self, player_id):
        if player_id == 1:
            self.change_tile_colors(self.COLORS['blue'], self.COLORS['bg_main'], self.analysys_players)
        else:
            self.change_tile_colors(self.COLORS['bg_main'], self.COLORS['red'], self.analysys_players)

                
                    
    def prev_move(self):
        if self.current_analysis_index > 0:
            self.current_analysis_index -= 1
            self.show_move(self.current_analysis_index)

    def next_move(self):
        if self.current_analysis_index < len(self.app.logic.game_history) - 1:
            self.current_analysis_index += 1
            self.show_move(self.current_analysis_index)
