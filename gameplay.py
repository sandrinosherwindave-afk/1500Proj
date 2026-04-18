import tkinter as tk
from quizStart_Intro import *
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
        self.MAX_LEVEL = 20

    def get_damage(self, level_rank):
        low, high = damage_range[level_rank]
        return random.randint(low, high) + (self.attack // 10)

    def calculate_growth(self, won_battle):
        if self.level >= self.MAX_LEVEL:
            return None
        BASE_HP_GAIN = 25
        BASE_ATK_GAIN = 12
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

# Initial Character Templates
mary = Character("Mary", "Achiever", "High", 5, {}, level=1, hp=100, attack=25)
john = Character("John", "Athletic", "Low", 6, {}, level=1, hp=150, attack=15)
nick = Character("Nick", "Street Smart", "Medium", 10, {}, level=1, hp=120, attack=20)

# ---------------------------------------------------------
# GLOBAL STATE & CONSTANTS
# ---------------------------------------------------------
PLAYER_MAX_HP = 100
ENEMY_MAX_HP = 120
unlocked_level = 1
current_player_hp = PLAYER_MAX_HP
unlocked_semester = 1
semesters_won_properly = []  # NEW TRACKER FOR ENDINGS


# Bypassing the quiz: Set Mary as the default player character
player = mary

QUESTIONS_BATTLE = {
    "easy": [{"q": "What is 2 + 2?", "a": "4"}, {"q": "What color is the sky?", "a": "blue"}, {"q": "Capital of France?", "a": "paris"}],
    "medium": [{"q": "12 x 12?", "a": "144"}, {"q": "Who wrote Romeo and Juliet?", "a": "shakespeare"}],
    "hard": [{"q": "Square root of 256?", "a": "16"}, {"q": "Red Planet?", "a": "mars"}]
}


class Gameplay:
    def __init__(self, master, active_quiz_instance ):
        self.master = master #root
        self.characterSprite = active_quiz_instance
        
    def story1(self, index):
        
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
        
    def show_ending(self):
        self.clear_screen()
        # Count how many times they actually won vs relied on Mercy
        actual_wins = semesters_won_properly.count(True)

        if actual_wins == 0:
            # BAD ENDING
            title = "THE 'BARE MINIMUM' ENDING"
            color = "#ff4444"
            msg = (
                f"Congratulations {player.name}...\n\n"
                "You technically graduated, but you relied on the mercy rule\n"
                "for every single semester. You have the degree,\n"
                "but you didn't actually learn a single thing.\n\n"
                "EMPLOYABILITY: 0%\n"
                "Regret: 100%"
            )
        else:
            # GOOD ENDING
            title = "THE ACADEMIC ELITE"
            color = "#00ff00"
            msg = (
                f"Incredible job, {player.name}!\n\n"
                f"You conquered the university with {actual_wins} true victories.\n"
                "You are graduating at the top of your class with honors!\n"
                "The future looks bright."
            )

        tk.Label(self.master,
                text=title,
                font=("Courier New", 24, "bold"),
                bg="black",
                fg=color).pack(pady=40)
        tk.Label(self.master,
                text=msg,
                font=("Courier New", 13),
                bg="black",
                fg="white",
                justify="center").pack(pady=20)
        tk.Button(self.master,
                text="QUIT GAME",
                command=self.master.quit,
                bg="#333333",
                fg="white",
                font=("Courier New", 12)).pack(
            pady=30)
    
    #MAIN MENU & COMMANDS
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

        hp_color = "#ffffff" if current_player_hp > 30 else "#ff0000"
        tk.Label(self.master,
                text=f"STUDENT HP: {current_player_hp}/{player.hp}",
                font=("Courier New", 14, "bold"),
                bg="#000000",
                fg=hp_color).pack(pady=10)

        btn_frame = tk.Frame(self.master, bg="#000000")
        btn_frame.pack(pady=30)
        tk.Button(btn_frame,
                text="👨‍🏫 GO TO CLASS",
                width=18,
                height=2,
                command=self.school_menu,
                bg="#ffffff",
                fg="#000000",
                font=("Courier New", 10, "bold")).pack(side="left", padx=10)
        tk.Button(btn_frame,
                text="🛌 REST IN DORM",
                width=18, height=2,
                command=self.dorm_room,
                bg="#ffffff",
                fg="#000000",
                font=("Courier New", 10, "bold")).pack(side="left", padx=10)
            

        sprite = self.characterSprite.get_character_label()
        sprite.pack(pady = 10)


        
        
    def dorm_room(self):
        global current_player_hp
        current_player_hp = player.hp
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
                            command=lambda s=sem_num: self.start_battle(s),
                            font=("Courier New", 9, "bold")).pack(pady=2)

        tk.Button(self.master,
                    text="BACK",
                    command=self.main_menu,
                    font=("Courier New", 10),
                    bg="#333333",
                    fg="white", 
                    width=10).pack(
        pady=20)
                    
                    
    #BATTLE SYSTEM 
    def start_battle(self, sem_id):
        global current_player_hp
        self.clear_screen()

        b_state = {
            "player_hp": current_player_hp,
            "enemy_hp": ENEMY_MAX_HP + (sem_id * 10),
            "current_answer": "",
            "monster_count": 1
        }

        canvas = tk.Canvas(self.master,
                            width=600,
                            height=400,
                            bg="#000000",
                            highlightthickness=1,
                            highlightbackground="#ffffff")
        canvas.pack(pady = 10)


        enemy_sprite = canvas.create_rectangle(420, 100, 480, 150, fill="#333333", outline="#ffffff", width=2)
        player_sprite = canvas.create_polygon(120, 350, 140, 300, 160, 280, 180, 300, 200, 350, fill="#ffffff")

        # UI Bars - Adjusted to match new sprite positions
        canvas.create_rectangle(38, 78, 222, 97, outline="#ffffff", width=1)
        canvas.create_rectangle(348, 318, 532, 337, outline="#ffffff", width=1)
        enemy_bar = canvas.create_rectangle(40, 80, 220, 95, fill="#ffffff", outline="")
        player_bar = canvas.create_rectangle(350, 320, 530, 335, fill="#ffffff", outline="")

        def shake(target, count=6, offset=5):
            if count > 0:
                direction = offset if count % 2 == 0 else -offset
                canvas.move(target, direction, 0)
                self.master.after(40, lambda: shake(target, count - 1, offset))

        diag_frame = tk.Frame(self.master, bg="#000000")
        diag_frame.pack(fill="both", padx=10, pady=10)
        qlbl = tk.Label(diag_frame,
                        text="",
                        fg="#ffffff",
                        bg="#000000",
                        font=("Courier New", 11, "bold"), wraplength=400)
        qlbl.pack(pady=10)

        battle_entry = tk.Entry(self.master,
                                font=("Courier New", 14),
                                bg="#111111",
                                fg="#ffffff",
                                insertbackground="white",
                                justify="center")
        battle_entry.pack(pady=5)
        battle_entry.focus_set()

        
        def update_bars():
            e_max = ENEMY_MAX_HP + (sem_id * 10)
            e_perc = max(0, b_state["enemy_hp"] / e_max)
            canvas.coords(enemy_bar, 40, 40, 40 + (e_perc * 180), 55)
            p_perc = max(0, b_state["player_hp"] / player.hp)
            canvas.coords(player_bar, 350, 180, 350 + (p_perc * 180), 195)

        def set_question():
            diff = "easy" if b_state["monster_count"] == 1 else "medium" if b_state["monster_count"] == 2 else "hard"
            q_data = random.choice(QUESTIONS_BATTLE[diff])
            b_state["current_answer"] = q_data["a"].lower()
            qlbl.config(text=f"SEMESTER {sem_id} | EXAM {b_state['monster_count']}/3\n\nQUESTION: {q_data['q']}")
            battle_entry.delete(0, tk.END)

        def check_ans(event=None):
            global current_player_hp
            user = battle_entry.get().strip().lower()
            if not user or user != b_state["current_answer"]:
                damage_taken = 15 + (sem_id * 2)
                b_state["player_hp"] = max(0, b_state["player_hp"] - damage_taken)
                current_player_hp = b_state["player_hp"]
                qlbl.config(text="WRONG! The monster attacks!")
                shake(player_sprite)  # Player shakes on hit
            else:
                dmg = player.get_damage(player.intelligence)
                b_state["enemy_hp"] = max(0, b_state["enemy_hp"] - dmg)
                shake(enemy_sprite)  # Enemy shakes on hit
            update_bars()
            self.master.after(600, process_turn_end)

        def process_turn_end():
            global unlocked_semester
            if b_state["player_hp"] <= 0:
                if player.level >= 5:
                    semesters_won_properly.append(False)  # Track as Mercy pass
                    is_final = (sem_id == 8)
                    if sem_id == unlocked_semester and unlocked_semester < 8:
                        unlocked_semester += 1
                    self.show_level_up_report(False, final=is_final)
                else:
                    self.show_level_up_report(False)
            elif b_state["enemy_hp"] <= 0:
                if b_state["monster_count"] < 3:
                    b_state["monster_count"] += 1
                    b_state["enemy_hp"] = ENEMY_MAX_HP + (sem_id * 10)
                    update_bars()
                    set_question()
                else:
                    semesters_won_properly.append(True)  # Track as True win
                    is_final = (sem_id == 8)
                    if sem_id == unlocked_semester and unlocked_semester < 8:
                        unlocked_semester += 1
                    self.show_level_up_report(True, final=is_final)
            else:
                set_question()

        tk.Button(self.master,
                text="SUBMIT ANSWER",
                command=check_ans,
                bg="#ffffff",
                fg="#000000",
                font=("Courier New", 10, "bold"), width=20).pack(pady=10)
        tk.Button(self.master,
                text="🏃 DROP CLASS",
                command=self.school_menu,
                bg="#333333",
                fg="#ffffff",
                font=("Courier New", 10, "bold"), width=20, relief="flat").pack(pady=5)
        
        battle_entry.bind("<Return>", check_ans)
          
        shake(enemy_sprite, count=4)
        shake(player_sprite, count=4)

        update_bars()
        set_question()
    
    def show_level_up_report(self,won, final=False):
        self.clear_screen()
        growth = player.calculate_growth(won)

        # Message for Mercy Progression
        mercy_msg = ""
        if not won and player.level >= 5:
            mercy_msg = "\n(Mercy Rule: Passed with low grades, continue with caution!!)"

        title = "SEMESTER PASSED" if won else "SEMESTER FAILED"
        title_color = "white" if won else "#ff6666"

        tk.Label(self.master,
                text=f"--- {title} ---",
                font=("Courier New", 20, "bold"),
                bg="black",
                fg=title_color).pack(pady=30)

        if growth:
            report = (
                f"Result: {growth['status']}\n"
                f"Efficiency: {growth['efficiency']}\n"
                f"New Level: {player.level}\n\n"
                f"HP: {growth['old_hp']} -> {player.hp} (+{growth['hp_gain']})\n"
                f"ATK: {growth['old_atk']} -> {player.attack} (+{growth['atk_gain']})\n"
                f"{mercy_msg}"
            )
            tk.Label(self.master,
                    text=report,
                    font=("Courier New", 12),
                    bg="black",
                    fg="white",
                    justify="center").pack(pady=10)
            
        # Routing button
        btn_txt = "GRADUATE" if final else "CONTINUE"
        btn_cmd = self.show_ending if final else self.main_menu
        
        tk.Button(self.master,
                text=btn_txt,
                command=btn_cmd,
                bg="white",
                fg="black",
                font=("Courier New", 12, "bold"),
                width=15).pack(pady=30)
                    





            

            
        
        
           


        
            
        