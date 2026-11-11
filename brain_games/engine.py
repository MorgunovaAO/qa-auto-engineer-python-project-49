import prompt

ROUNDS_COUNT = 3


def run_game(description, get_question_and_answer):
    """
    description: строка-описание игры (выводится в начале)

    get_question_and_answer: функция, которая возвращает пару
    (question, correct_answer)
    """
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