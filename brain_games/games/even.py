import random


def get_question_and_answer():    
    num = random.randint(0, 1000)
    question = num
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return question, correct_answer