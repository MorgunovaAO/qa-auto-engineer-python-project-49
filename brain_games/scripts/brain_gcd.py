from brain_games.cli import welcome_user
from brain_games.engine import run_game
from brain_games.games.gcd import get_question_and_answer


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    
    description = "Find the greatest common divisor of given numbers."
    if run_game(description, get_question_and_answer):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        
if __name__ == "__main__":
    main()