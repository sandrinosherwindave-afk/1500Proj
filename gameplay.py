import tkinter as tk

questions = [
    ("What is 5 + 3?", "8"),
    ("What is the capital of France?", "paris"),
    ("What is 10 * 2?", "20")
]


'''
After a _forget ang mga label:
top: 1st year
side: display model nga na kwa ka player
center: typing animation ka story, highlight key points
after center animation: show a button next part (fight)


'''
class FirstYear:
    def __init__(self, master = None):
        self.master = master #startgame.win
    
    def story1(self):
        Year1story_1 = tk.Label(
        self.master,
        text = "Hello",
        font = ("Courier", 16),
        fg = "white",
        bg = "black"
        )
        
        Year1story_1.pack(pady = 10)