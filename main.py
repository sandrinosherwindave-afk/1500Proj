import tkinter as tk
from drawings import *
from characters import *
from main_functions import QuizFunctions, StartFunctions


quiz = QuizFunctions()
start_game = StartFunctions()
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

entry = tk.Entry(root,
                 font=("Courier New", ),
                 bg = "black",
                 fg = "white",
                 )

result_label = tk.Label(
    root,
    text="",
    font=("Courier New", 12),
    fg="white",
    bg = "black"
)

btn = tk.Button(root,
                text=">-Submit-<",
                font = ("Courier New",9),
                command= quiz.next_question,
                bg = "black",
                fg = "white",
                relief = "groove"
                )

start_btn = tk.Button(root,
                      text = "Start Game",
                      font = ("Courier New", 10),
                      command = start_game.start,
                      bg = "black",
                      fg ="white",
                      relief= "groove")


title = tk.Label(root,
                    text = title ,
                    font = ("Courier New", 8),
                    fg = "white",
                    bg = "black"
                    )

#Function Access from main_functions.py
start_btn.config(command = lambda: 
    start_game.start(start_btn,
                     root,  
                     question_label, 
                     entry, 
                     btn, 
                     result_label,
                     title))

btn.config(command=lambda: 
    quiz.next_question(entry, 
                       result_label, 
                       question_label, 
                       title, 
                       btn, 
                       root,
                       start_btn))
def handle_enter(event):
    if start_btn.winfo_manager():
        start_game.start(start_btn, root, question_label, entry, btn, result_label,)
    else:
        quiz.next_question(entry, result_label, question_label, title, btn, root, start_btn)

root.bind("<Return>", handle_enter)



#Packing and Positioning
title.pack(pady=30)
question_label.pack(pady=20)
entry.pack()
result_label.pack(pady=10)
btn.pack(pady=8)


# Start first question
question_label.config(text=questions[0][0])

root.mainloop()


