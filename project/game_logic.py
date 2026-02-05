import random

class GameLogic:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.current_symbol = None
   
        self.player1_symbol = None
        self.player2_symbol = None

        self.game_mode = None
        self.game_over = False

        self.game_history = []
   
        self.computer_strategies = {
            'EASY': self.computer_move_easy,
            'MEDIUM': self.computer_move_medium,
            'HARD': self.computer_move_hard
        }
        self.selected_difficulty = None



    def initialize_game(self, p1_symbol, p2_symbol):
        self.player1_symbol = p1_symbol
        self.player2_symbol = p2_symbol
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.game_history = []


    def is_board_full(self, board):
        return all(board[r][c] != "" for r in range(3) for c in range(3))

    def is_board_empty(self, board):
        return not any(board[r][c] for r in range(3) for c in range(3))
    
    def get_empty_cells(self, board):
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]

    def get_computer_symbol(self):
        return self.player2_symbol
    
    def get_human_symbol(self):
        return self.player1_symbol


    def make_move(self, row, col):
        if self.board[row][col] != "" or self.game_over:
            return False
        self.board[row][col] = self.current_symbol
        return True



    def check_winner(self, board, symbol, return_line = False):
        for r in range(3):
            if all(board[r][c] == symbol for c in range(3)):
                line = [(r, c) for c in range(3)]
                return line if return_line else True
        
        for c in range(3):
            if all(board[r][c] == symbol for r in range(3)):
                line = [(r, c) for r in range(3)]
                return line if return_line else True
            
        if all(board[i][i] == symbol for i in range(3)):
            line = [(i, i) for i in range(3)]
            return line if return_line else True
        if all(board[i][2 - i] == symbol for i in range(3)):
            line = [(i, 2 - i) for i in range(3)]
            return line if return_line else True

        return False    



    def is_computer_turn(self):
        return self.game_mode == 'computer' and self.current_symbol == self.player2_symbol


    def computer_move_easy(self):
        empty_cells = self.get_empty_cells(self.board)
        if not empty_cells:
            return
        return random.choice(empty_cells)
        

    def computer_move_medium(self): 
        return self.choose_best_move(max_depth = 2, randomness = 0.2)


    def computer_move_hard(self): 
        return self.choose_best_move()


    def minmax(self, board, curr_depth, max_depth, maximizing):
        computer = self.get_computer_symbol()
        human = self.get_human_symbol()

        if self.check_winner(board, computer):
            return 10 - curr_depth
        elif self.check_winner(board, human):
            return curr_depth - 10
        if self.is_board_full(board):
            return 0
        
        if max_depth and curr_depth >= max_depth:
            return 0
        
        empty_cells = self.get_empty_cells(board)
        if maximizing:
            best = -float('inf')
            for r, c in empty_cells:
                board[r][c] = computer
                score = self.minmax(board, curr_depth + 1, max_depth, maximizing = False)
                board[r][c] = ""
                best = max(best, score)
            return best
        else:
            best = float('inf')
            for r, c in empty_cells:
                board[r][c] = human
                score = self.minmax(board, curr_depth + 1, max_depth, maximizing = True)
                board[r][c] = ""
                best = min(best, score)
            return best



    def choose_best_move(self, max_depth = None, randomness = 0):
        computer = self.get_computer_symbol()
        empty_cells = self.get_empty_cells(self.board)

        if self.is_board_empty(self.board):
            return random.choice(empty_cells)

        best_score = -float('inf')
        best_moves = []

        for r, c in empty_cells:
            self.board[r][c] = computer
            score = self.minmax(self.board, 0, max_depth, maximizing = False)
            self.board[r][c] = ""
            if score > best_score:
                best_score = score
                best_moves = [(r, c)]
            elif score == best_score:
                best_moves.append((r, c))

        if best_moves:
            if max_depth and random.random() < randomness:
                    return random.choice(empty_cells)
            else:
                return random.choice(best_moves) 



    def get_best_human_move(self, board):
        human = self.get_human_symbol()
        empty_cells = self.get_empty_cells(board)
        
        if self.is_board_empty(board):
            return empty_cells
        best_score = float('inf') 
        best_moves = []
        for r, c in empty_cells:
            board[r][c] = human
            score = self.minmax(board, 0, max_depth = None, maximizing = True)
            board[r][c] = ""
            if score < best_score:
                best_score = score
                best_moves = [(r, c)]
            elif score == best_score:
                best_moves.append((r, c))

        if best_moves:
            return best_moves
        return None
