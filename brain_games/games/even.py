import random


def get_question_and_answer():    
    number = random.randint(0, 100)
    question = number
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer