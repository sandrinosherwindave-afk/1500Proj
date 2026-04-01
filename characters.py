import random
import tkinter as tk

damage_range = {
    "High": (15, 20),
    "Medium": (10, 12),
    "Low": (5, 10)
}
# Character class
class Character:
    def __init__(self, name, ctype, intelligence, luck, subjects):
        self.name = name
        self.ctype = ctype
        self.intelligence = intelligence
        self.luck = luck
        self.subjects = subjects

    def get_damage(self, level):
        low, high = damage_range[level]
        return random.randint(low, high)
    
    
# Characters
mary = Character("Mary", "Achiever", "High", 5, {})
john = Character("John", "Athletic", "Low", 6, {})
nick = Character("Nick", "Street Smart", "Medium", 10, {})

# Quiz data
questions = [
    ("What is 5 + 3?", "8"),
    ("What is the capital of France?", "paris"),
    ("What is 10 * 2?", "20")
]



