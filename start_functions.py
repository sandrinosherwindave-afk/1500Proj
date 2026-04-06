from main_functions import QuizFunctions
import tkinter as tk
from drawings import *


def start(root):
    global startgame_win
    startgame_win = tk.Tk()
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
    
    intro_story = tk.Label(
    startgame_win,
    text = "",
    font = ("Courier", 16),
    fg = "white",
    bg = "black"
    )
    
    
    
    label.pack(pady = 20)
    intro_story.pack(pady =10, padx= 5)
    root.destroy()
    start_animations(0, intro_story)
    startgame_win.mainloop()
    

def start_animations(index, intro_story):
    fullintro_story = "You are now enrolled at CPU! \nThe worst will now come"

        
    if index < len(fullintro_story):
        intro_story.config(text=intro_story.cget("text") + fullintro_story[index])
        # Schedule the next character after 100ms
    startgame_win.after(150, lambda: start_animations(index + 1, intro_story))    
    
    

  

    
    