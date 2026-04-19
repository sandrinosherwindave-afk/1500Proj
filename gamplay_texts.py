# Expanded Questions List
SEMESTER_QUESTIONS = {
    1: { # Semester 1
        1: [ # Prelims
            {"q": "What is 2 + 2?", "a": "4"}, 
            {"q": "What color is the sky?", "a": "blue"}
        ],
        2: [ # Midterms
            {"q": "Capital of France?", "a": "paris"},
            {"q": "What is 5 + 5?", "a": "10"}
        ],
        3: [ # Finals
            {"q": "How many legs does a dog have?", "a": "4"},
            {"q": "Opposite of cold?", "a": "hot"}
        ]
    },
    2: { # Semester 2
        1: [
            {"q": "12 x 12?", "a": "144"}, 
            {"q": "Who wrote Romeo and Juliet?", "a": "shakespeare"}],
        2: [
            {"q": "Capital of Japan?", "a": "tokyo"}, 
            {"q": "What is 15 * 3?", "a": "45"}],
        3: [
            {"q": "How many continents are there?", "a": "7"}, 
            {"q": "What is 10 * 10?", "a": "100"}]
    },
    3: { # Semester 3
        1: [
            {"q": "Square root of 256?", "a": "16"}, 
            {"q": "Red Planet?", "a": "mars"}],
        2: [
            {"q": "Largest mammal?", "a": "blue whale"}, 
            {"q": "Author of 1984?", "a": "george orwell"}],
        3: [
            {"q": "Symbol for Gold?", "a": "au"}, 
            {"q": "Water boils at what temp (C)?", "a": "100"}]
    },
    "default": { # Fallback for Semesters 4-8 to prevent crashes
        1: [
            {"q": "Generic Prelim Question? (ans: yes)", "a": "yes"}],
        2: [
            {"q": "Generic Midterm Question? (ans: yes)", "a": "yes"}],
        3: [
            {"q": "Generic Boss Question? (ans: yes)", "a": "yes"}]
    }
}

        
# 1. Create a dictionary mapping each semester ID (1-8) to a unique message
intro_messages = {
    1: "Year 1, Semester 1.\n\nWelcome to the academy. Let's start with the basics.",
    2: "Year 1, Semester 2.\n\nThe training wheels are coming off. Stay sharp.",
    3: "Year 2, Semester 1.\n\nA new year. The curriculum grows darker.",
    4: "Year 2, Semester 2.\n\nMidterms approach. Don't lose your focus.",
    5: "Year 3, Semester 1.\n\nUpperclassman status achieved. Expectations are high.",
    6: "Year 3, Semester 2.\n\nThe pressure is mounting. Survive this.",
    7: "Year 4, Semester 1.\n\nThe final stretch begins. Master your craft.",
    8: "Year 4, Semester 2.\n\nThe Final Exams. Leave nothing behind."
}