import prompt
import random


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')     
    for _ in range(3):
        num = random.randint(0, 1000)
        print(f'Question: {num}')
        
        answer = prompt.string("Your answer: ")
        correct = 'yes' if num % 2 == 0 else 'no'
        
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            return False

    return True