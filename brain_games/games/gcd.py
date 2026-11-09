import random


def get_question_and_answer():    
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    while b != 0:
        a, b = b, a % b
    correct_answer = str(a)
    return question, correct_answer