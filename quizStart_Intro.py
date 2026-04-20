import tkinter as tk
from gameplay import Gameplay
from startquiz_functions import questions

  

def start_quiz(startgame_win):
    from startquiz_functions import QuizFunctions
    from drawings import title
    startgame_win.destroy()

    
    # Tkinter window
    root = tk.Tk()
    root.title("CCS Crawler")
    root.state('zoomed')
    root.attributes("-fullscreen", True)
    root.iconbitmap("necromancer.ico")
    root.configure(background="black")    
    quiz = QuizFunctions(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (root.quit(), root.destroy()))

    question_label = tk.Label(root,
                            text="",
                            font=("Courier New", 14,),
                            fg="white",
                            bg = "black"
                            )

    entry = tk.Entry(root,
                    font=("Courier New",),
                    bg = "black",
                    fg = "white",
                    insertbackground="white",
                    justify="center"
                    )

    

    result_label = tk.Label(
        root,
        text="",
        font=("Courier New", 12),
        fg="white",
        bg = "black"
    )

    btn = tk.Button(root,
                    text=">> ✅Submit <<",
                    font = ("Courier New",10),
                    command= quiz.next_question,
                    bg = "white",
                    fg = "black",
                    relief = "groove"
                    )  
    def removeprevious_labels():
        for widget in root.winfo_children():
                widget.pack_forget()
                widget.place_forget()

        # 2. Initialize the Gameplay class
        # Replace 'root' with whatever your main Tkinter window variable is named in this file
        # 'quiz' is already defined in your scope based on your snippet
        game_session = Gameplay(master=root, active_quiz_instance=quiz)

        # 3. Call the method to display the "CONTINUE TO CAMPUS" button
        game_session.story1(0)
        

    
    
    start_btn = tk.Button(root,
                        text = "LET'S GO",
                        font = ("Courier New", 10),
                        command= removeprevious_labels,
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

    btn.config(command=lambda: 
        quiz.next_question(entry, 
                        result_label, 
                        question_label, 
                        title, 
                        btn, 
                        root,
                        start_btn,
                        introquiz))
    def handle_enter(event):
        if start_btn.winfo_manager():
            pass
        else:
            quiz.next_question(entry, 
                               result_label, 
                               question_label,
                               title,
                               btn, 
                               root, 
                               start_btn,
                               introquiz)

    root.bind("<Return>", handle_enter)
    
    
    introquiz = tk.Label(
        root,
        text = "",
        font = ("Courier", 10),
        fg = "white",
        bg = "black"
    )
    
    def introquiz_animations(index1, introquiz):
        fullintroquiz = "Before we begin your journey\n We must first determine who you are by answering these simple quiz"

        
        if index1 < len(fullintroquiz):
            introquiz.config(text=introquiz.cget("text") + fullintroquiz[index1])
            # Schedule the next character after 100ms
        root.after(10, lambda: introquiz_animations(index1 + 1, introquiz))
        

    #Packing and Positioning
    title.pack(pady=10)
    introquiz_animations(0, introquiz)
    introquiz.pack(pady=5)
    def quiz_packs(): question_label.pack(pady=20), entry.pack(), entry.focus_set(), result_label.pack(pady=10), btn.pack(pady=8)
    root.after(10, quiz_packs)


    # Start first question
    question_label.config(text=questions[0][0])

    root.mainloop()


