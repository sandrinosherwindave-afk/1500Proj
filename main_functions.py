from characters import *
from drawings import *
import tkinter as tk


class QuizFunctions:
    def __init__(self):
        self.score = 0
        self.q_index = 0
        self.model_title = None     # Store the Rank Label
        self.player_drawing = None   # Store the ASCII Label
    
    def next_question(self, entry, result_label, question_label,title, btn, root, start_btn):
        user = entry.get().lower()
        entry.delete(0, tk.END)

        if user == questions[self.q_index][1]:
            self.score += 1
            result_label.config(text="Correct!")
        else:
            result_label.config(text="Wrong!")

        self.q_index += 1

        if self.q_index < len(questions):
            question_label.config(text=questions[self.q_index][0])
        else:
            self.show_result(question_label, title, entry, btn, root, result_label, start_btn)

    def show_result(self, question_label, title, entry, btn, root, result_label, start_btn):
        question_label.pack_forget()
        title.pack_forget()
        entry.pack_forget()
        btn.pack_forget()
              
        
        if self.score == 0:
            self.current_model = mary_model
            self.model_title = tk.Label(root, 
                                        text="RANK: ACHIEVER", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black")
            self.player_drawing = tk.Label(root,
                                   text = self.current_model,
                                   font = ("Courier New", 14),
                                   fg = "white",
                                   bg = "black"
                                   )
            
            self.model_title.pack(pady = 3)
            result_label.config(text=f"Final Score: {self.score}/3\n You Got Mary", fg="white")
            self.player_drawing.place(x= 590, y = 192)
            start_btn.pack(side = "top",pady = 4)
            
        elif self.score == 2:
            player = john
            display_model = "You got John!"
            
        elif self.score == 3:
            self.current_model = nick_model
            self.model_title = tk.Label(root, 
                                        text="RANK: STREET SMART", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black"
                                        )
            nick_player = tk.Label(root,
                                   text = self.current_model,
                                   font = ("Courier New", 14),
                                   fg = "white",
                                   bg = "black",
                                   justify= tk.LEFT,
                                   )
            
            self.model_title.pack(pady = 3)
            result_label.config(text=f"Final Score: {self.score}/3\n You Got Nick!", fg="white")
            nick_player.place(x= 660, y = 192)
            start_btn.pack(side = "top",pady = 4)
            
            
        
        
        
class StartFunctions:
    def __init__(self):
        self.quiz = QuizFunctions()
        self.settings_win = None

    def start(self, start_btn, root, question_label, entry, btn, result_label):
        root.iconify()

        startgame_win = tk.Toplevel(root)
        startgame_win.title("Settings")
        startgame_win.geometry("400x300")
        startgame_win.configure(bg="black")
        startgame_win.state('zoomed')
        def intro():
            return f"Welcome to {title}"
        

        # Add widgets to the new window
        label = tk.Label(startgame_win, 
                        text= intro(), 
                        font=("Courier New", 18), 
                        fg="white", 
                        bg="black")
        
        label.pack(pady = 20)
        
         
        
        
        
        
    


        

        
        