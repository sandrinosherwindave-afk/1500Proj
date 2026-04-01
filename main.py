import tkinter as tk
from drawings import *
from characters import *



# Tkinter window
root = tk.Tk()
root.title("Quiz Game")
root.state('zoomed')
root.configure(background="black")

question_label = tk.Label(root,
                          text="",
                          font=("Courier New", 14,),
                          fg="white",
                          bg = "black"
                          )
question_label.pack(pady=20)


entry = tk.Entry(root,
                 font=("Courier New", ),
                 bg = "black",
                 fg = "white",

                 )
entry.pack()



result_label = tk.Label(
    root,
    text="",
    font=("Courier New", 12),
    fg="white",
    bg = "black"
)
result_label.pack(pady=10,)

class Functions:
    def __init__(self):
        self.score = 0
        self.q_index = 0
    
    def next_question(self):
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
            self.show_result()

    def show_result(self):
        question_label.pack_forget()
        entry.pack_forget()
        btn.pack_forget()

        if self.score == 3:
            player = mary
            msg = "Perfect! You unlocked Mary!"
        elif self.score == 2:
            player = john
            msg = "You got John!"
        else:
            player = nick
            final_title = tk.Label(root, 
                                        text="RANK: ACHIEVER", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black"
                                        )
            final_msg = tk.Label(root, 
                                      text=f"Perfect! You unlocked Nick!",
                                      font = ("Courier New", 10),
                                      fg="white", 
                                      bg="black"
                                      )
            
            
        final_title.pack(side = "top", pady=20)
        result_label.config(text=f"Final Score: {self.score}/3", fg="white")
        character.config(text = mary_player,
                         fg = "white",
                        bg = "black")
        character.config.pack(side = "top", pady = 10)
        result_label.config(text=f"Score: {self.score}/3\n{msg}")
        
quiz = Functions()

btn = tk.Button(root,
                text=">-Submit-<",
                font = ("Courier New",9),
                command= quiz.next_question,
                bg = "black",
                fg = "white",
                relief = "groove"
                )
btn.pack(pady=8)

root.bind("<Return>", lambda event: quiz.next_question())

character = tk.Label(root,
                    text = dragon ,
                    font = ("Courier New", 8),
                    fg = "white",
                    bg = "black"
                    )
character.pack(pady=30)


# Start first question
question_label.config(text=questions[0][0])

root.mainloop()
'''
this may or may not be a comment

'''

