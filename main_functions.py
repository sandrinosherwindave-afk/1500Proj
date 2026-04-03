from characters import *
from drawings import *
import tkinter as tk


class QuizFunctions:
    def __init__(self):
        self.score = 0
        self.q_index = 0
    
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
            self.show_result(question_label, title, entry, btn, root, result_label,start_btn)

    def show_result(self, question_label, title, entry, btn, root, result_label,start_btn):
        question_label.pack_forget()
        title.pack_forget()
        entry.pack_forget()
        btn.pack_forget()
        
        display_text = ""
        display_model = ""

        if self.score == 3:
            display_model = mary_model
            display_text = "Perfect! You unlocked Mary!"
            mary_title = tk.Label(root, 
                                        text="RANK: ACHIEVER", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black")
            mary_msg = tk.Label(root, 
                                      text=display_text,
                                      font = ("Courier New", 10),
                                      fg="white", 
                                      bg="black"
                                      )
            mary_player = tk.Label(root,
                                   text = display_model,
                                   font = ("Courier New", 14),
                                   fg = "white",
                                   bg = "black"
                                   )
            
            mary_title.pack(pady = 3)
            mary_msg.pack(pady = (0, 10))
            result_label.config(text=f"Final Score: {self.score}/3", fg="white")
            mary_player.place(x= 590, y = 192)
            start_btn.pack(side = "top",pady = 4)
            
        elif self.score == 2:
            player = john
            display_model = "You got John!"
            
        elif self.score == 0:
            display_model = nick_model
            display_text = "Sadly, you got Nick"
            nick_title = tk.Label(root, 
                                        text="RANK: STREET SMART", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black"
                                        )
            nick_msg = tk.Label(root, 
                                      text=display_text,
                                      font = ("Courier New", 10),
                                      fg="white", 
                                      bg="black"
                                      )
            nick_player = tk.Label(root,
                                   text = display_model,
                                   font = ("Courier New", 14),
                                   fg = "white",
                                   bg = "black",
                                   justify= tk.LEFT,
                                   )
            
            nick_title.pack(pady = 3)
            nick_msg.pack(pady = (0, 10))
            result_label.config(text=f"Final Score: {self.score}/3", fg="white")
            nick_player.place(x= 660, y = 192)
            start_btn.pack(side = "top",pady = 4)
        
        
        
class StartFunctions:
    def __init__(self):
        self.quiz = QuizFunctions()
    
    def start(self):
        self.quiz.question_label.pack_forget()
        self.quiz.title.pack_forget()
        self.quiz.entry.pack_forget()
        self.quiz.btn.pack_forget()
        
        self.quiz.question_label.pack()
        self.quiz.title.pack()
        self.quiz.entry.pack()
        self.quiz.btn.pack()
        
        