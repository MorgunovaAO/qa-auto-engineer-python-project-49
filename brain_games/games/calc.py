import random
import operator


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    } 

def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    op_symbol, op_func = random.choice(list(ops.items()))
    
    question = f"{num1} {op_symbol} {num2}"    
    correct_answer = str(op_func(num1, num2))
    return question, correct_answer              