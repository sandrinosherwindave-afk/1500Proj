from characters import *
from drawings import *

class Functions:
    def __init__(self):
        self.score = 0
        self.q_index = 0
    
    def next_question(self):
        from main import entry, result_label, question_label
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
        from main import question_label, character, entry, btn, root, result_label
        question_label.pack_forget()
        character.pack_forget()
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
            nick_title = tk.Label(root, 
                                        text="RANK: STREET SMART", 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black"
                                        )
            nick_msg = tk.Label(root, 
                                      text=f"Perfect! You unlocked Nick!",
                                      font = ("Courier New", 10),
                                      fg="white", 
                                      bg="black"
                                      )
            nick_player = tk.Label(root,
                                   text = nick_model,
                                   font = ("Courier New", 4),
                                   fg = "white",
                                   bg = "black"
                                   )
            
        nick_title.pack(side = "top", pady=20)
        nick_msg.pack(side = "top", pady = 10)
        result_label.config(text=f"Final Score: {self.score}/3", fg="white")
        nick_player.pack(pady = 5)