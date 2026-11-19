import prompt

ROUNDS_COUNT = 3


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def run_game(description, get_question_and_answer):
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")

        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            return False

    return True
        
def start_game(description, get_question_and_answer):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    
    if run_game(description, get_question_and_answer):
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")