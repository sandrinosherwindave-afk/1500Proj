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

class FirstYear:
    def __init__(self, master):
        self.master = master #root
        
    
    def story1(self, index, quiz_result_obj):
        
        Year1story_1 = tk.Label(
        self.master,
        text = "",
        font = ("Courier", 16),
        fg = "white",
        bg = "black"
        )
        

        def story1_animation(index, Year1story_1):
            fullintro_story1 = "Day 1\n You start your day when you encountered a professor"
            
            if not Year1story_1.winfo_exists():
                return

            if index < len(fullintro_story1):
                Year1story_1.config(text=Year1story_1.cget("text") + fullintro_story1[index])
                # Schedule the next character after 100ms
                self.master.after(10, lambda: story1_animation(index + 1, Year1story_1))
                
            # else:
            #     if quiz_result_obj and quiz_result_obj.result:
            #         self.master.after(5, quiz_result_obj.result.place(relx=0.5, rely=0.5, anchor="center"))
        
        Year1story_1.pack(pady = 10)            
        story1_animation(index, Year1story_1)
        self.start_gameplay()
        
    def start_gameplay(self):

        def frame():
            def show_frame(frame):
                """Raises the specified frame to the front."""
                frame.tkraise()
                        
            frame = tk.Frame(self.master)
            frame.pack(fill = "both", expand = True)
            
            battle1 = tk.Frame(frame, bg = "lightblue")
            tk.Label(battle1, text="This is Page 1").pack()
            tk.Button(battle1, text="Next", command=lambda: show_frame(battle2)).pack()
            
            battle2 = tk.Frame(frame, bg = "lightgreen")
            tk.Label(battle2, text="This is Page 2").pack()
            tk.Button(battle2, text="Next", command=lambda: show_frame(battle1)).pack()
            
            for F in (battle1, battle2):
                F.grid(row=0, column=0, sticky="nsew")
            
                
            show_frame(battle1)
                
        game_start = tk.Button(
        self.master,
        font = ("Courier", 10),
        fg = "white",
        bg = "black",
        relief = "groove",
        command = frame,
        text = "Show next frame"
        )
        
        game_start.pack(pady = 10)
        
           


        
            
        