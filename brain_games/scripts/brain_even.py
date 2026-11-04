from brain_games.greet import greet
from brain_games.cli import welcome_user
from brain_games.is_even import is_even


def main():
    greet()
    name = welcome_user()
    if is_even():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        
if __name__ == "__main__":
    main()