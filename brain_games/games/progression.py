import random


def make_progression(start, step, length):
    return [start + index * step for index in range(length)]


def get_question_and_answer():     
    start = random.randint(0, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = make_progression(start, step, length)
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    question = ' '.join(str(element) for element in progression)
    return question, correct_answer