import tkinter as tk
from drawings import *
from quizStart_Intro import *

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
        text = ">>> PRESS ANY KEY TO START GAME <<<",
        font = ("Courier New", 15, "bold"),
        height = 1,
        bg = "black",
        fg = "white",
        relief = "solid",
        command= start_quiz,
        )


    
    quit_game = tk.Button(
        startgame_win,
        text = "Quit",
        font = ("Courier New",10, "bold"),
        command = lambda: startgame_win.destroy(),
        bg = "gray",
        fg = "black",
        width = 10,
        height = 1,
        relief = "solid"
    )
        
    intro_story = tk.Label(
        startgame_win,
        text = "",
        font = ("Courier", 16),
        fg = "white",
        bg = "black"
    )
    
    startgame_win.bind("<Key>", lambda event: button_start.invoke())    
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
    startgame_win.after(10, lambda: start_animations(index + 1, intro_story))
   
start()
  

    
    