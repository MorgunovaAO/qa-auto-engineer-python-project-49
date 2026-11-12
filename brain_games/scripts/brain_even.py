from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games.even import get_question_and_answer


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    if run_game(description, get_question_and_answer):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        

if __name__ == "__main__":
    main()