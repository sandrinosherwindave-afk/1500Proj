# Expanded Questions List
SEMESTER_QUESTIONS = {
    1: { # Semester 1: Basics & Syntax
        1: [ # Prelims (2 questions)
            {"q": "Which keyword is used to create a function in Python?", "a": "def"},
            {"q": "What is the correct file extension for Python files?", "a": ".py"}
        ],
        2: [ # Midterms (2 questions)
            {"q": "How do you insert COMMENTS in Python code?", "a": "#"},
            {"q": "What is the output of print(2**3)?", "a": "8"}
        ],
        3: [ # Finals (1 question)
            {"q": "Which function is used to get input from the user?", "a": "input"}
        ]
    },
    2: { # Semester 2: Data Types & Lists
        1: [ # Prelims
            {"q": "Which data type is used for True or False values?", "a": "boolean"},
            {"q": "What method adds an element to the end of a list?", "a": "append"}],
        2: [ # Midterms
            {"q": "How do you start a WHILE loop in Python?", "a": "while"},
            {"q": "What is the index of the first element in a list?", "a": "0"}],
        3: [ # Finals
            {"q": "Which command is used to exit a loop prematurely?", "a": "break"}]
    },
    3: { # Semester 3: Intermediate Logic
        1: [ # Prelims
            {"q": "What keyword is used to import a module?", "a": "import"},
            {"q": "Which operator is used for floor division?", "a": "//"}],
        2: [ # Midterms
            {"q": "What is a collection which is ordered and unchangeable?", "a": "tuple"},
            {"q": "What function returns the number of items in an object?", "a": "len"}],
        3: [ # Finals
            {"q": "How do you start an IF statement in Python?", "a": "if"}]
    },
    4: { # Semester 4: Advanced Basics
        1: [ # Prelims
            {"q": "Which keyword is used to handle exceptions?", "a": "try"},
            {"q": "What is the output of bool(0)?", "a": "false"}],
        2: [ # Midterms
            {"q": "What method removes whitespace from the start and end of a string?", "a": "strip"},
            {"q": "What is the keyword for a 'do nothing' statement?", "a": "pass"}],
        3: [ # Finals
            {"q": "Which symbol is used for the modulo operator?", "a": "%"}]
    },
    # Fallback for Semesters 5-8 using the final set to ensure no crashes
    "default": {
        1: [{"q": "Is Python case sensitive? (yes/no)", "a": "yes"}],
        2: [{"q": "Is Python an interpreted language? (yes/no)", "a": "yes"}],
        3: [{"q": "Can a list contain different data types? (yes/no)", "a": "yes"}]
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