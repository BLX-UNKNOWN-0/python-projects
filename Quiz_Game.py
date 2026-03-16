# BLX-UNKNOWN-0
# PROJECT 5 // SIMPLE QUIZ GAME


import random

QUESTIONS = [
    {"question": "Which keyword defines a function?",
     "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
    {"question": "What does len('hello') return?",
     "options": ["A) 4", "B) 5", "C) 6", "D) 0"], "answer": "B"},
    {"question": "Which is mutable?",
     "options": ["A) tuple", "B) string", "C) list", "D) int"], "answer": "C"},
    {"question": "What is 10 % 3?",
     "options": ["A) 3", "B) 2", "C) 0", "D) 1"], "answer": "D"},
    {"question": "How to add item to list?",
     "options": ["A) add()", "B) push()", "C) insert()", "D) append()"], "answer": "D"},
]

def ask_question(number, q):
    print(f"\nQ{number}: {q['question']}")
    for option in q["options"]:
        print(f"  {option}")
    while True:
        ans = input("Answer (A/B/C/D): ").strip().upper()
        if ans in ["A", "B", "C", "D"]:
            break
        print("Invalid! Enter A, B, C or D.")
    if ans == q["answer"]:
        print(" Correct!")
        return True
    print(f"Wrong! Answer was {q['answer']}")
    return False

def save_score(score, total):
    with open("quiz_scores.txt", "a") as f:
        f.write(f"Score: {score}/{total}\n")
    print("Score saved to quiz_scores.txt")


print(" Python Quiz Game\n")
questions = random.sample(QUESTIONS, 3)
score = sum(ask_question(i+1, q) for i, q in enumerate(questions))
print(f"\nResult: {score}/{len(questions)}")
save_score(score, len(questions))


