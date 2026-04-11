import tkinter as tk
from drawings import *
from quizStart_Intro import *
from gameplay import FirstYear

startgame_win = tk.Tk()
startgame_win.title("CCS CRAWLER")
startgame_win.geometry("400x300")
startgame_win.iconbitmap("necromancer.ico")
startgame_win.configure(bg="black")
startgame_win.state('zoomed')

def start():
    def intro():
        return f"Welcome to {title}"
    

    # Add widgets to the new window
    label = tk.Label(startgame_win, 
                    text= intro(), 
                    font=("Courier New", 18), 
                    fg= "#FFFFFF", 
                    bg="black")

    
    button_start = tk.Button(
        startgame_win,
        text = "Start Game",
        width=10, 
        height=1, 
        font = ("Courier New", 15),
        command = start_quiz,
        bg = "black",
        fg ="white",
        relief= "groove"
    )    
    
    quit_game = tk.Button(
        startgame_win,
        text = "Quit",
        command = lambda: startgame_win.destroy(),
        bg = "black",
        fg = "white",
        relief = "groove"
        
    )
        
    intro_story = tk.Label(
        startgame_win,
        text = "",
        font = ("Courier", 16),
        fg = "white",
        bg = "black"
    )
    
    startgame_win.bind("<Return>", lambda event: button_start.invoke())    
    label.pack(pady = 10)
    intro_story.pack(pady =10, padx= 5)
    
    start_animations(0, intro_story)
    
    button_start.config(command = lambda:
        start_quiz(startgame_win))
    startgame_win.after(2000, lambda: button_start.pack(pady = 20))
    startgame_win.after(3000, lambda: quit_game.pack(pady = 5))

    
    startgame_win.mainloop()
    

def start_animations(index, intro_story):
    fullintro_story = "You are now enrolled at CPU! \nThe worst will now come"

        
    if index < len(fullintro_story):
        intro_story.config(text=intro_story.cget("text") + fullintro_story[index])
        # Schedule the next character after 100ms
    startgame_win.after(30, lambda: start_animations(index + 1, intro_story))
   
start()
  

    
    