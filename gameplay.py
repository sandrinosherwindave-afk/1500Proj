import tkinter as tk
from quizStart_Intro import *
from startquiz_functions import *



  
'''
After a _forget ang mga label:
top: 1st year
side: display model nga na kwa ka player
center: typing animation ka story, highlight key points
after center animation: show a button next part (fight)


'''

quizIntro_result = QuizFunctions()
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
            self.master.after(30, lambda: story1_animation(index + 1, Year1story_1))
        
        Year1story_1.pack(pady = 10)    
        story1_animation(index, Year1story_1)
        if quizIntro_result.result is not None:
            quizIntro_result.result.pack(pady=10)
        else:
            print("Debug: quizIntro_result.result is still None!")

        
            
        