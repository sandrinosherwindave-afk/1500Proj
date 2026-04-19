import tkinter as tk
from quizStart_Intro import *
import random
from drawings import *
from gamplay_texts import *
  
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
ENEMIES = {
    1: {
        "Prelim": enemy1,
        "Midterm": enemy2,
        "Sem 1 Boss": enemy3
    },
    2: {
        "Midterm Moth": "  @_@  \n /|||\\ \n  / \\ ",
        "Paper Phantom": "  ^o^  \n \\_|_/ \n  / \\ ",
        "Sem 2 Boss": "  0_0  \n =|=|= \n  / \\ "
    },
    3: {
        "Sleepy Specter": "  x_x  \n /| |\\ \n  / \\ ",
        "Cramming Creep": "  -_o  \n \\| |/ \n  | | ",
        "Sem 3 Boss": "  T_T  \n /_|_\\ \n  | | "
    },
    4: {
        "Tuition Troll": "  $_$  \n /|||\\ \n  / \\ ",
        "Thesis Terror": "  *_* \n \\_|_/ \n  / \\ ",
        "Sem 4 Boss": "  !_!  \n =|=|= \n  / \\ "
    },
    "default": {
        "Generic Grunt": "  ?_?  \n /| |\\ \n  / \\ ",
        "Standard Spirit": "  #_#  \n \\| |/ \n  | | ",
        "Final Fiend": "  &_&  \n /_|_\\ \n  | | "
    }
}

#Tracker for repeating questions
question_usage = {}

class Gameplay:
    def __init__(self, master, active_quiz_instance):
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
        global sprite
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
                            width=20,
                            height=2,
                            state="normal" if is_unlocked else "disabled",
                            bg=btn_bg,
                            fg=btn_fg,
                            command=lambda s=sem_num: self.start_battle(s),
                            font=("Courier New", 10, "bold")).pack(pady=8)

        tk.Button(self.master,
                    text="BACK",
                    command=self.main_menu,
                    font=("Courier New", 10),
                    bg="#333333",
                    fg="white", 
                    width=12).pack(
        pady=20)
    def semester_intro(self, sem_id):
        self.clear_screen()

        # Create a label for the typing animation
        intro_label = tk.Label(
            self.master,
            text="",
            font=("Courier", 18, "bold"),
            fg="white",
            bg="black"
        )
        # expand=True centers the text vertically and horizontally
        intro_label.pack(expand=True)

        # 2. Fetch the specific text for this semester. 
        # The .get() method includes a safe fallback just in case an invalid sem_id is passed.
        intro_text = intro_messages.get(sem_id, f"Entering Semester {sem_id}...\n\nPrepare for your exams.")

        def animation(index):
            if not intro_label.winfo_exists():
                return

            if index < len(intro_text):
                # Type the next character
                intro_label.config(text=intro_label.cget("text") + intro_text[index])
                # Speed of the typing (30ms per character)
                self.master.after(30, lambda: animation(index + 1))
            else:
                # Once typing is completely finished, wait 1 second (1000ms), then load the battle
                self.master.after(1000, lambda: self.start_battle(sem_id))
        
        # Start the animation at character index 0
        animation(0)
                    
                    
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

        # INCREASED CANVAS SIZE: height from 250 to 400
        canvas = tk.Canvas(self.master,
                        width=900,
                        height=600,
                        bg="#000000",
                        highlightthickness=1,
                        highlightbackground="#ffffff")
        canvas.pack(pady=10)
        
        #CHOSEN PLAYER SPRITE
        chosenChara = self.characterSprite.get_character_text()

        #MODIFIED
        #==========
        #Enemy
        #==========
        #EnemyInformation
        enemy_pool = ENEMIES.get(sem_id, ENEMIES["default"])
        enemy_list = list(enemy_pool.items())
        enemy_name, enemy_art = enemy_list[b_state["monster_count"] - 1]
        
        #Sprite
        enemy_sprite = tk.Label(canvas, text= enemy1, fg="white", bg="black", font=("courier", 10), justify="left")
        enemy_spriteWindow = canvas.create_window(600, 40, window=enemy_sprite, anchor="nw")
        #HP Bar
        
        canvas.create_rectangle(46, 70, 357, 88, outline="#ffffff", width=1)
        enemy_bar = canvas.create_rectangle(48, 72, 355, 86, fill="#ffffff", outline="")
        enemy_name_tag = canvas.create_text(48, 65, text=enemy_name, fill="white", font=("courier", 12, "bold"), anchor="sw")

        #==========
        #Player
        #==========
        
        #Sprite
        player_sprite = tk.Label(canvas, text=chosenChara, fg="white", bg="black", font=("courier", 8), justify="left")
        player_spriteWindow = canvas.create_window(148, 600, window=player_sprite, anchor="sw")
        #HP Bar
        canvas.create_text(545, 445, text="Mary", fill="white", font=("courier", 12, "bold"), anchor="sw")
        canvas.create_rectangle(545, 452, 860, 472, outline="#ffffff", width=2)
        player_bar = canvas.create_rectangle(547, 454, 858, 470, fill="#ffffff", outline="")

        # --- SHAKE EFFECT ---
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
            
            canvas.coords(enemy_bar, 48, 72, 48 + (e_perc * 307), 86)
            
            p_perc = max(0, b_state["player_hp"] / player.hp)
            
            canvas.coords(player_bar, 547, 454, 547 + (p_perc * 311), 470)

        #MODIFIED
        def set_question():
            exam_num = b_state["monster_count"]
            
            # 1. Fetch semester data (fallback to default if semester isn't defined)
            sem_data = SEMESTER_QUESTIONS.get(sem_id, SEMESTER_QUESTIONS["default"])
            
            # 2. Fetch specific exam questions (fallback to default if exam isn't defined)
            exam_questions = sem_data.get(exam_num, SEMESTER_QUESTIONS["default"][exam_num])
            
            # 3. Filter out questions that have been asked 2 or more times
            valid_questions = [q for q in exam_questions if question_usage.get(q["q"], 0) < 2]
            
            # 4. Fallback: Reset usage if all questions are exhausted
            if not valid_questions:
                for q in exam_questions:
                    question_usage[q["q"]] = 0
                valid_questions = exam_questions

            # 5. Select random question and update tracking
            q_data = random.choice(valid_questions)
            question_usage[q_data["q"]] = question_usage.get(q_data["q"], 0) + 1

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
                shake(player_spriteWindow)  # Player shakes on hit
            else:
                dmg = player.get_damage(player.intelligence)
                b_state["enemy_hp"] = max(0, b_state["enemy_hp"] - dmg)
                shake(enemy_spriteWindow)  # Enemy shakes on hit
            update_bars()
            self.master.after(600, process_turn_end)

        #MODIFIED
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
                    # ADVANCE TO NEXT EXAM/MONSTER
                    b_state["monster_count"] += 1
                    b_state["enemy_hp"] = ENEMY_MAX_HP + (sem_id * 10)
                    
                    # Grab the updated pool, convert to list, and get the new name/art
                    current_pool = ENEMIES.get(sem_id, ENEMIES["default"])
                    enemy_list_updated = list(current_pool.items())
                    new_name, new_art = enemy_list_updated[b_state["monster_count"] - 1]

                    enemy_sprite.config(text=new_art)
                    canvas.itemconfig(enemy_name_tag, text=new_name)

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
                text="DROP CLASS",
                command=self.school_menu,
                bg="#333333",
                fg="#ffffff",
                font=("Courier New", 10, "bold"), width=20, relief="flat").pack(pady=5)
        
        battle_entry.bind("<Return>", check_ans)
          
        shake(enemy_spriteWindow, count=4)
        shake(player_spriteWindow, count=4)

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
                    





            

            
        
        
           


# # #INDEPENDENT TEST#
# # # --- Add this at the very bottom of gameplay.py ---

# if __name__ == "__main__":
#     # 1. Create the main Tkinter window
#     root = tk.Tk()
#     root.geometry("800x600")  # You can adjust the size
#     root.title("Gameplay Testing Mode")
#     root.configure(bg="black")
#     root.state("zoomed")

#     # 2. Create a "Mock" or dummy quiz instance.
#     # The Gameplay class requires this to get the character sprite label.
#     class MockQuizInstance:
#         def get_character_label(self):
#             # Return a simple placeholder label instead of the actual image
#             return tk.Label(root, text="[Character Sprite Placeholder]", fg="white", bg="#333333", width=30, height=10)
#     mock_quiz = MockQuizInstance()

#     # 3. Initialize the Gameplay session
#     test_session = Gameplay(master=root, active_quiz_instance=mock_quiz)

#     # 4. Choose where you want the test to start!
#     # Uncomment the one you want to test:
    
#     test_session.story1(0)         # Tests the typing animation and intro
#     # test_session.main_menu()     # Skips intro and goes straight to the Hub
#     # test_session.school_menu()   # Skips directly to the Year/Semester selection
#     # test_session.start_battle(1) # Skips directly to a battle (Semester 1)

#     # 5. Start the Tkinter loop
#     root.mainloop()