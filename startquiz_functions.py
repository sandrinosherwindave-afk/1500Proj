from drawings import *
import tkinter as tk
from gameplay import Gameplay

questions = [
    ("What is 5 + 3?", "8"),
    ("What is the capital of France?", "paris"),
    ("What is 10 * 2?", "20")
]

class QuizFunctions:
    def __init__(self, master):
        self.master = master
        self.result = None  # Placeholder for the label/image
        self.score = 0
        self.q_index = 0
    
    # def transition_to_game(self):
    #     # 1. Hide the character label from the quiz screen
    #     if self.result is not None:
    #         self.result.pack_forget()
    #         self.result.place_forget()
            
    #     # 2. Clear all other widgets from the screen
    #     for widget in self.master.winfo_children():
    #         widget.destroy()
            
    #     # 3. Create the gameplay object, passing `self` (this exact quiz instance)
    #     game = Gameplay(self.master, self)
        
    #     # 4. Trigger the first story sequence
    #     game.story1(0)

    def get_character_label(self, parent=None):
            """
            Creates or updates the character label and returns the widget object.
            You can pass a 'parent' to put this label inside a specific frame or window.
            """
            # Use the passed parent, or default to self.master
            target_master = parent if parent else self.master

            # 1. If it doesn't exist yet, create the label with consistent styling
            if self.result is None:
                self.result = tk.Label(target_master, 
                                    text="", 
                                    bg="black", 
                                    fg="white", 
                                    font=("Courier New", 14), 
                                    justify=tk.LEFT)
            else:
                # If the label already exists but we want to move it to a new parent
                # we have to re-assign it or recreate it (Tkinter labels are tied to their masters)
                if self.result.master != target_master:
                    self.result.destroy()
                    self.result = tk.Label(target_master, 
                                        text="", 
                                        bg="black", 
                                        fg="white", 
                                        font=("Courier New", 14), 
                                        justify=tk.LEFT)
            
            # 2. Update the text to match the current character model
            if hasattr(self, 'current_model'):
                self.result.config(text=self.current_model) 
                
            # 3. Return the label object so it can be packed anywhere
            return self.result
    
    def get_character_text(self):
        """Returns just the raw string of the current model."""
        if hasattr(self, 'current_model'):
            return self.current_model 
        return ""
    
    def get_character_name(self):
        """Returns the name of the chosen character."""
        if hasattr(self, 'character_name'):
            return self.character_name
        return "" # Default fallback
    
    

    def next_question(self, entry, result_label, question_label,title, btn, root, start_btn, introquiz):
        user = entry.get().lower()
        entry.delete(0, tk.END)

        if user == questions[self.q_index][1]:
            self.score += 1
            result_label.config(text="Correct!")
        else:
            result_label.config(text="Wrong!")

        self.q_index += 1

        if self.q_index < len(questions):
            question_label.config(text=questions[self.q_index][0])
        else:
            self.show_result(question_label, title, entry, btn, root, result_label, start_btn, introquiz)

    def show_result(self, question_label, title, entry, btn, root, result_label, start_btn, introquiz):
            # Clear the screen
            question_label.pack_forget()
            introquiz.pack_forget()
            title.pack_forget()
            entry.pack_forget()
            btn.pack_forget()
                    
            # 1. Determine Model, Title, and Text based on Score
            if self.score == 3:
                self.current_model = mary_model
                self.character_name = "Mary"
                rank_text = "RANK: ACHIEVER"
                msg_text = f"Final Score: {self.score}/3\n You Got Mary"
                
            elif self.score == 1 or 2:
                self.current_model = nick_model
                rank_text = "RANK: STREET SMART"
                self.character_name = "Nick"
                msg_text = f"Final Score: {self.score}/3\n You Got Nick!"
                
            elif self.score == 0:
                self.current_model = john_model
                self.character_name = "John"
                rank_text = "RANK: ACHIEVER" 
                msg_text = f"Final Score: {self.score}/3\n You Got John" # Fixed copy-paste error here

            # 2. Setup and display the Title and Score
            self.model_title = tk.Label(root, 
                                        text=rank_text, 
                                        font=("Courier New", 20, "bold"), 
                                        fg="gold", 
                                        bg="black")
            self.model_title.pack(pady=3)
            
            result_label.config(text=msg_text, fg="white")
            start_btn.pack(side="top", pady=4)
            
            # 3. Get the character label and place/pack it anywhere!
            char_label = self.get_character_label()
            
            # Example 1: Packing it dynamically based on the score
            if self.score == 0:
                char_label.pack(pady=10)
            # Example 2: Placing it at specific coordinates
            elif self.score == 1:
                char_label.place(pady=10)
            elif self.score == 2:
                char_label.place(pady=10)
                        
            
        
        
        

        
         
        
        
        
        
    


        

        
        