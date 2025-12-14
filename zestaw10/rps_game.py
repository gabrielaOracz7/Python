import tkinter as tk
from PIL import Image, ImageTk
import random



class RockPaperScissors(tk.Frame):
    def __init__(self, master = None, title = 'Rock - Paper - Scissors'):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title(title)
        self.master.geometry('500x450')

        self.win_limit = 3 # default value
        self.user_score = 0
        self.computer_score = 0

        self.question_mark_img = self.load_image('images/question_mark.png')
        
        choices = ['rock', 'paper', 'scissors']
        self.choice_images_user = {
            choice: self.load_image(f'images/{choice}.png')
            for choice in choices
        }
        self.choice_images_computer = {  #flipped images 
            choice: self.load_image(f'images/{choice}.png', flip = True)
            for choice in choices
        }

        self.create_start_frame()
        self.create_game_frame()
        self.create_end_frame()

        self.start_frame.pack(expand = True, fill = 'both')


    def load_image(self, path, flip = False, size = (217, 170)):
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        if flip:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        return ImageTk.PhotoImage(img)


#--------------------------START FRAME---------------------------------
    def create_start_frame(self):
        self.start_frame = tk.Frame(self.master, padx = 20, pady = 20, bg = '#D19C1D')

        self.error_label = tk.Label(self.start_frame, text='', font = ('MS Serif', 15, 'bold'), fg = "#5F1407", bg = '#D19C1D')
        self.error_label.pack(pady=5)

        title_label = tk.Label(self.start_frame, text = 'ROCK PAPER SCISSORS', font = ('MS Sans Serif', 25, 'bold'), bg = '#D19C1D', fg = '#F5E7BF')
        title_label.pack(pady = 50)

        rounds_label = tk.Label(self.start_frame, text = 'Play until how many wins? (default 3):', font = ('MS Serif', 15), bg = '#D19C1D', fg = '#2B2722')
        rounds_label.pack()

        self.rounds_entry = tk.Entry(self.start_frame, font = ('MS Serif', 18), justify = 'center')
        self.rounds_entry.pack(pady = 10)

        start_button = tk.Button(self.start_frame, text = 'START GAME', font = ('MS Sans Serif', 15, 'bold'), bg = '#5C5346', fg = 'white', command = self.start_game)
        start_button.pack(pady = 15)


    def start_game(self):
        txt = self.rounds_entry.get().strip()
        if txt == '':
            self.win_limit = 3 # default val
        elif not txt.isdigit() or  int(txt) == 0:
            self.error_label.config(text = 'Please enter a positive integer!')
            return
        else :
            self.win_limit = int(txt)

        self.error_label.config(text='')
        self.start_frame.pack_forget()
        self.game_frame.pack(expand=True, fill='both')

 
#---------------------------GAME FRAME---------------------------------
    def create_game_frame(self):
        self.game_frame = tk.Frame(self.master, padx = 10, pady = 10, bg = '#F5E7BF')

    #------------SCORE SUBFRAME---------------
        score_subframe = tk.Frame(self.game_frame,  pady = 5, bg = '#D19C1D')
        
        score_title_label = tk.Label(score_subframe, text = 'SCORE: ', font = ('MS Sans Serif', 23, 'bold'), bg = '#D19C1D', fg = '#F5E7BF')
        score_title_label.pack()

        self.user_score_var = tk.StringVar(value = f'You: {self.user_score}')
        self.computer_score_var = tk.StringVar(value = f'Computer: {self.computer_score}')
        user_score_label = tk.Label(score_subframe, textvariable = self.user_score_var, font = ('Arial', 15, 'bold'), fg = '#2B2722', bg = '#D19C1D')
        computer_score_label = tk.Label(score_subframe, textvariable = self.computer_score_var, font = ('Arial', 15, 'bold') , fg = '#2B2722', bg = '#D19C1D')
        user_score_label.pack(side = 'left', padx = 40)
        computer_score_label.pack(side = 'right', padx = 40)
        
        score_subframe.pack(fill = 'x', pady = 10)

    #----------CHOICES SUBFRAME----------------
        self.choices_subframe = tk.Frame(self.game_frame, pady = 5, bg = '#F5E7BF')

        user_choice_label = tk.Label(self.choices_subframe, text = 'Your choice: ', font = ('MS Serif', 13), bg = '#F5E7BF', fg = '#2B2722')
        computer_choice_label = tk.Label(self.choices_subframe, text = 'Computer choice: ', font = ('MS Serif', 13), bg = '#F5E7BF', fg = '#2B2722')
        user_choice_label.grid(row = 0, column = 0, pady = 3)
        computer_choice_label.grid(row = 0, column = 1, pady = 3)

        self.user_choice_img = tk.Label(self.choices_subframe,  image = self.question_mark_img, bg = "#F5E7BF")
        self.computer_choice_img = tk.Label(self.choices_subframe, image = self.question_mark_img, bg = '#F5E7BF')
        self.user_choice_img.grid(row = 1, column = 0, padx = 10, pady = 5)
        self.computer_choice_img.grid(row = 1, column = 1, padx = 10, pady = 5)

        self.choices_subframe.pack(fill = 'x')

    #-----------BUTTONS SUBFRAME---------------
        self.buttons_subframe = tk.Frame(self.game_frame, pady = 5, bg = '#F5E7BF')
        self.buttons_subframe.columnconfigure([0, 1, 2], weight = 1)

        choose_label = tk.Label(self.buttons_subframe, text = 'CHOOSE: ', font = ('MS Sans Serif', 16, 'bold'), bg = '#F5E7BF')
        choose_label.grid(row = 0, column = 0, columnspan = 3)

        tk.Button(self.buttons_subframe, text = 'ROCK', bg = '#7D5B0C', fg ='#F5E7BF', font = ('MS Sans Serif', 12, 'bold'), command = lambda: self.play_round('rock')).grid(row = 1, column = 0, sticky = 'ew', pady = 5, padx = 5)
        tk.Button(self.buttons_subframe, text = 'PAPER',  bg = '#D19C1D', fg ='#F5E7BF', font = ('MS Sans Serif', 12, 'bold'), command = lambda: self.play_round('paper')).grid(row = 1, column = 1, sticky = 'ew', pady = 5, padx = 5)
        tk.Button(self.buttons_subframe, text = 'SCISSORS',  bg = '#F5D383', fg ='#FFFFFF', font = ('MS Sans Serif', 12, 'bold'), command = lambda: self.play_round('scissors')).grid(row = 1, column = 2, sticky = 'ew', pady = 5, padx = 5)

        self.buttons_subframe.pack(fill = 'x', pady = 10)

    #---------ROUND RESULT SUBFRAME------------
        self.round_result_subframe = tk.Frame(self.game_frame, pady = 10, bg = '#453118')
        self.round_result_label = tk.Label(self.round_result_subframe, text = '', font = ('MS Serif', 18, 'bold'), fg = '#ECEAE4', bg = '#453118')
        self.round_result_label.pack(pady = 5)


    def show_round_result(self, msg):
        self.round_result_label.config(text = msg)
        self.buttons_subframe.pack_forget()
        self.round_result_subframe.pack(fill = 'x', pady = 5)
        self.master.after(2500, self.restore_choices_and_buttons)


    def restore_choices_and_buttons(self):
        self.user_choice_img.config(image = self.question_mark_img)
        self.computer_choice_img.config(image = self.question_mark_img)
        self.round_result_subframe.pack_forget()
        self.buttons_subframe.pack(fill = 'x', pady = 5)


    
    def play_round(self, user_choice):
        """Handle one round of the game: update choices, determine round winner, update scores, check for game end"""

        computer_choice = random.choice(list(self.choice_images_user.keys()))
        self.user_choice_img.config(image = self.choice_images_user[user_choice])
        self.computer_choice_img.config(image = self.choice_images_computer[computer_choice])

        if user_choice == computer_choice:
            result_msg = 'Tie!'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            self.user_score += 1
            result_msg = 'You win this round!'
        else:
            self.computer_score += 1
            result_msg = 'You lose this round!' 

        self.user_score_var.set(f'You: {self.user_score}')
        self.computer_score_var.set(f'Computer: {self.computer_score}')

        if self.user_score >= self.win_limit:
            self.show_round_result(result_msg)
            self.master.after(2500, lambda: self.show_game_result('Congratulations!\nYou win the game!'))
        elif self.computer_score >= self.win_limit:
            self.show_round_result(result_msg)    
            self.master.after(2500, lambda: self.show_game_result('You lose the game :(\nBetter luck next time!'))
        else:
            self.show_round_result(result_msg)



#----------------------------END FRAME---------------------------------
    def create_end_frame(self):
        self.end_frame = tk.Frame(self.master, padx = 20, pady = 50, bg = '#5C5346')
        
        self.final_result_message_label = tk.Label(self.end_frame, text = '', font = ('MS Serif', 28, 'bold'), bg = '#5C5346', fg = "#221E18")
        self.final_result_message_label.pack(pady = 30)

        self.play_again_button = tk.Button(self.end_frame, text = 'PLAY AGAIN!', font = ('Arial', 17, 'bold'), command = self.restart_game, bg = '#D19C1D', fg = '#ECEAE4')
        self.play_again_button.pack(pady = 40)


    def show_game_result(self, msg):
        self.game_frame.pack_forget()
        self.final_result_message_label.config(text = msg)
        self.end_frame.pack(expand = True, fill = 'both')


    def restart_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_var.set(f'You: {self.user_score}')
        self.computer_score_var.set(f'Computer: {self.computer_score}')

        self.end_frame.pack_forget()
        self.start_frame.pack(expand = True, fill = 'both')
        self.rounds_entry.delete(0, tk.END)
        self.user_choice_img.config(image = self.question_mark_img)
        self.computer_choice_img.config(image = self.question_mark_img)





if __name__ == '__main__':
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
