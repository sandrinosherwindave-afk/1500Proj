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
    def __init__(self, master):
        self.master = master #startgame.win
    
    def story1(self, index):
        
        Year1story_1 = tk.Label(
        self.master,
        text = "",
        font = ("Courier", 16),
        fg = "white",
        bg = "black"
        )
        
        def story1_animation(index, Year1story_1):
            fullintro_story1 = "Day 1\n You start your day when you encountered a professor"

                
            if index < len(fullintro_story1):
                Year1story_1.config(text=Year1story_1.cget("text") + fullintro_story1[index])
                # Schedule the next character after 100ms
            self.master.after(30, lambda: self.master(index + 1, Year1story_1))
        
        self.Year1story_1.pack(pady = 10)    
        story1_animation(index, Year1story_1)
        
            
        