import tkinter as tk
from drawings import *
from characters import *
from main_functions import QuizFunctions, StartFunctions


quiz = QuizFunctions()
start = StartFunctions()
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
                      command = start.start,
                      bg = "black",
                      fg ="white",
                      relief= "groove")

#Function Access from main_functions.py

btn.config(command=lambda: 
    quiz.next_question(entry, 
                       result_label, 
                       question_label, 
                       title, 
                       btn, 
                       root,
                       start_btn))
for key in ("<Return>", "<space>"):
    root.bind(key, lambda event: quiz.next_question(entry, result_label, question_label, title, btn, root, start_btn))

title = tk.Label(root,
                    text = title ,
                    font = ("Courier New", 8),
                    fg = "white",
                    bg = "black"
                    )

#Packing and Positioning
title.pack(pady=30)
question_label.pack(pady=20)
entry.pack()
result_label.pack(pady=10)
btn.pack(pady=8)


# Start first question
question_label.config(text=questions[0][0])

root.mainloop()


