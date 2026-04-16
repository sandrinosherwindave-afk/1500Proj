import tkinter as tk
from quizStart_Intro import *
from startquiz_functions import *
import textwrap 
import random

  
'''
After a _forget ang mga label:
top: 1st year
side: display model nga na kwa ka player
center: typing animation ka story, highlight key points
after center animation: show a button next part (fight)


'''

damage_range = {
    "High": (15, 20),
    "Medium": (10, 12),
    "Low": (5, 10)
}

class Character:
    def __init__(self, name, ctype, intelligence, luck, subjects, level=1, hp=100, attack=20):
        self.name = name
        self.ctype = ctype
        self.intelligence = intelligence
        self.luck = luck
        self.subjects = subjects
        self.level = level
        self.hp = hp
        self.attack = attack
        self.MAX_LEVEL = 10

    def get_damage(self, level_rank):
        low, high = damage_range[level_rank]
        return random.randint(low, high) + (self.attack // 10)

    def calculate_growth(self, won_battle):
        if self.level >= self.MAX_LEVEL:
            return None
        BASE_HP_GAIN = 20
        BASE_ATK_GAIN = 10
        level_efficiency = max(0.2, 1.0 - ((self.level - 1) * 0.1))
        multiplier = 1.0 if won_battle else 0.5
        status_text = "VICTORY" if won_battle else "DEFEATED"
        final_hp_gain = int(BASE_HP_GAIN * multiplier * level_efficiency)
        final_atk_gain = int(BASE_ATK_GAIN * multiplier * level_efficiency)

        data = {
            "status": status_text,
            "efficiency": f"{level_efficiency * 100:.0f}%",
            "old_hp": self.hp,
            "old_atk": self.attack,
            "hp_gain": final_hp_gain,
            "atk_gain": final_atk_gain,
            "new_level": self.level + 1
        }
        self.hp += final_hp_gain
        self.attack += final_atk_gain
        self.level += 1
        return data

    def get_dialogue(self, won_battle):
        if self.level >= self.MAX_LEVEL:
            return f"{self.name}: I have reached the peak of my potential."
        if won_battle:
            if self.name == "Mary": return "Mary: I feel the surge of victory! My power grows."
            if self.name == "John": return "John: Another foe fallen. I am getting stronger."
            if self.name == "Nick": return "Nick: Easy work. On to the next one!"
        return f"{self.name}: That... didn't go as planned. I need to train harder."

# Initial Character Templates
mary = Character("Mary", "Achiever", "High", 5, {}, level=1, hp=100, attack=25)
john = Character("John", "Athletic", "Low", 6, {}, level=1, hp=150, attack=15)
nick = Character("Nick", "Street Smart", "Medium", 10, {}, level=1, hp=120, attack=20)

# ---------------------------------------------------------
# GLOBAL STATE & CONSTANTS
# ---------------------------------------------------------
PLAYER_MAX_HP = 140
ENEMY_MAX_HP = 120
unlocked_level = 1
current_player_hp = PLAYER_MAX_HP
unlocked_semester = 1 

# Bypassing the quiz: Set Mary as the default player character
player = mary

QUESTIONS_BATTLE = {
    "easy": [{"q": "What is 2 + 2?", "a": "4"}, {"q": "What color is the sky?", "a": "blue"}, {"q": "Capital of France?", "a": "paris"}],
    "medium": [{"q": "12 x 12?", "a": "144"}, {"q": "Who wrote Romeo and Juliet?", "a": "shakespeare"}],
    "hard": [{"q": "Square root of 256?", "a": "16"}, {"q": "Red Planet?", "a": "mars"}]
}


class Gameplay:
    def __init__(self, master):
        self.master = master #root
        self.characterSprite = QuizFunctions(self.master)
        
    def story1(self, index, quiz_result_obj):
        
        Year1story_1 = tk.Label(
        self.master,
        text = "",
        font = ("Courier", 16),
        fg = "white",
        bg = "black"
        )
        Year1story_1.pack(pady = 10)

        def story1_animation(index, Year1story_1):
            fullintro_story1 = "Day 1\n You start your day when you encountered a professor"
            
            if not Year1story_1.winfo_exists():
                return

            if index < len(fullintro_story1):
                Year1story_1.config(text=Year1story_1.cget("text") + fullintro_story1[index])
                # Schedule the next character after 100ms
                self.master.after(10, lambda: story1_animation(index + 1, Year1story_1))
                
            else:
                self.start_gameplayButton()
  
            # else:
            #     if quiz_result_obj and quiz_result_obj.result:
            #         self.master.after(5, quiz_result_obj.result.place(relx=0.5, rely=0.5, anchor="center"))
        
        
        story1_animation(index, Year1story_1)
        
    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.forget()
        
    def start_gameplayButton(self):       
        continueTocampus = tk.Button(self.master, 
                text="🏫 CONTINUE TO CAMPUS",  
                bg="#ffffff", 
                fg="#000000",
                command=self.main_menu,
                font=("Courier New", 12, "bold"), relief="raised", bd=2)
        
        continueTocampus.pack(pady = 10)
        
    def main_menu(self):
        self.clear_screen()
        tk.Label(self.master, 
                 text="UNIVERSITY HUB", 
                 font=("Courier New", 26, "bold"), 
                 bg="#000000", 
                 fg="#ffffff").pack(pady=40)
        tk.Label(self.master, 
                 text=f"STUDENT: {player.name} | LEVEL: {player.level}", 
                 font=("Courier New", 12), 
                 bg="#000000", 
                 fg="#ffffff").pack()
        tk.Label(self.master, 
                 text=f"STUDENT HP: {current_player_hp}/{PLAYER_MAX_HP}", 
                 font=("Courier New", 14, "bold"), 
                 bg="#000000", 
                 fg="#ffffff").pack()

        btn_frame = tk.Frame(self.master, bg="#000000")
        btn_frame.pack(pady=30)
        tk.Button(btn_frame, 
                  text="👨‍🏫 GO TO CLASS", 
                  width=18, 
                  height=2, 
                  command=self.school_menu, 
                  bg="#ffffff", 
                  fg="#000000", 
                  font=("Courier New", 10, "bold"), 
                  relief="flat").pack(side="left", padx=10)
        tk.Button(btn_frame, 
                  text="🛌 REST IN DORM", 
                  width=18, 
                  height=2, 
                  command=self.dorm_room, 
                  bg="#ffffff", 
                  fg="#000000", 
                  font=("Courier New", 10, "bold"), 
                  relief="flat").pack(side="left", padx=10)
        
        if self.characterSprite and self.characterSprite.result:
            self.characterSprite.result.pack(pady = 20)
        
        
    def dorm_room(self):
        global current_player_hp
        current_player_hp = PLAYER_MAX_HP
        self.clear_screen()
        tk.Label(self.master, 
                 text="DORM ROOM", 
                 font=("Courier New", 20, "bold"), 
                 bg="#000000", 
                 fg="white").pack(pady=40)
        tk.Label(self.master, 
                 text="RECOVERY COMPLETE", 
                 bg="#000000", 
                 fg="#ffffff", 
                 font=("Courier New", 12, "bold")).pack(pady=10)
        tk.Button(self.master, 
                  text="BACK", 
                  command=self.main_menu, 
                  font=("Courier New", 10, "bold"), 
                  bg="#ffffff", 
                  fg="#000000").pack(pady=20)
        
    def school_menu(self):
        self.clear_screen()
        tk.Label(self.master,
                    text="ACADEMIC CAREER (4 YEARS)",
                    font=("Courier New", 20, "bold"),
                    bg="#000000",
                    fg="#ffffff").pack(
            pady=10)

        container = tk.Frame(self.master, bg="black")
        container.pack(pady=10)

        # Generate 4 Years, 2 Semesters each
        for year in range(1, 5):
            year_frame = tk.LabelFrame(container, text=f"YEAR {year}", bg="black", fg="white",
                                        font=("Courier New", 10, "bold"), padx=10, pady=5)
            year_frame.grid(row=(year - 1) // 2, column=(year - 1) % 2, padx=10, pady=10)

            for sem in range(1, 3):
                sem_num = ((year - 1) * 2) + sem
                is_unlocked = sem_num <= unlocked_semester

                btn_text = f"Semester {sem}"
                btn_bg = "#ffffff" if is_unlocked else "#222222"
                btn_fg = "#000000" if is_unlocked else "#666666"

                tk.Button(year_frame,
                            text=btn_text,
                            width=15,
                            state="normal" if is_unlocked else "disabled",
                            bg=btn_bg,
                            fg=btn_fg,
                            command=lambda s=sem_num: start_battle(s),
                            font=("Courier New", 9, "bold")).pack(pady=2)

        tk.Button(self.master,
                    text="BACK",
                    command=self.main_menu,
                    font=("Courier New", 10),
                    bg="#333333",
                    fg="white", 
                    width=10).pack(
        pady=20)
                    





            

            
        
        
           


        
            
        