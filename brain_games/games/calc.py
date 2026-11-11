import operator
import random

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    } 


def get_question_and_answer():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    op_symbol, op_func = random.choice(list(ops.items()))
    
    question = f"{num_1} {op_symbol} {num_2}"    
    correct_answer = str(op_func(num_1, num_2))
    return question, correct_answer              