from brain_games.games.gcd import DESCRIPTION, get_question_and_answer
from brain_games.engine import start_game

def main():
    start_game(DESCRIPTION, get_question_and_answer)
    
if __name__ == "__main__":
    main()