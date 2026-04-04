from characters import *
from drawings import *
import tkinter as tk


class QuizFunctions:
    def __init__(self):
        self.score = 0
        self.q_index = 0
        self.current_model = "" 
        self.model_title = ""
    
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
        
        display_text = ""
              
        
        if self.score == 0:
            self.current_model = mary_model
            self.model_title = tk.Label(root, 
                                        text="RANK: ACHIEVER", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black")
            mary_player = tk.Label(root,
                                   text = self.current_model,
                                   font = ("Courier New", 14),
                                   fg = "white",
                                   bg = "black"
                                   )
            
            self.model_title.pack(pady = 3)
            result_label.config(text=f"Final Score: {self.score}/3\n You Got Mary", fg="white")
            mary_player.place(x= 590, y = 192)
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
        
    def start(self, start_btn, root, title, question_label, entry, btn, result_label):
        
        
        start_btn.pack_forget()
        question_label.pack_forget()
        result_label.pack_forget()
        model = self.quiz.model_title
        model.pack_forget()
        self.quiz.current_model.place_forget()
        
        
        # 3. Create the display_model label
        # Note: 'nick_model' or 'mary_model' must be passed or imported
        display_label = tk.Label(root,
                                 text=model_to_show, # Example: showing the Nick model
                                 font=("Courier New", 14),
                                 fg="white",
                                 bg="black",
                                 justify=tk.LEFT)
        
        # 4. Use .place() to put it where you want
        title.pack(pady=30)
        
    


        

        
        