# ------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question = 1

    for i in questions:
        print("\n------------------------------")
        print("Welcome to the Multiple Choice Game")
        print("------------------------------")
        print(i)
        for j in options[question - 1]:
            print(j)

        question += 1
        guess = input("What is your answer [A B C D]: ").upper()
        guesses.append(guess)
        correct_answer = questions.get(i)
        correct_guesses += check_answer(correct_answer, guess)

    display_score(guesses, correct_guesses)


# ------------------------------
def check_answer(answer, guess):
    if answer == guess:
        return 1
    else:
        return 0


# ------------------------------    
def display_score(guesses, correct_guesses):
    print("\n------------------------------")
    print("These are your RESULTS")
    print("------------------------------")
    print("These are your Guesses: " + ' '.join(map(str, guesses)))
    print("These are the Answers: " + ' '.join(map(str, questions.values())))
    score = correct_guesses / len(guesses) * 100
    print('This is Your score ' + str(int(score)) + "%")
    print("------------------------------")


# ------------------------------
def play_again():
    play = input("Do you want to play again (yes/no): ").lower()
    if play == "yes":
        return True
    else:
        print("Bye hope you want to play again!!!!")
        return False


questions = {

    "Who won the Rugby World Cup 2023": "B",
    "Who won the Football World Cup 2022": "C",
    "Who won the English Premier League in 2022": "A",
    "Who won the South African Premier Soccer League": "C"
}

options = [
    ["A.New Zealand", "B.South Africa", "C.Australia", "D.England"],
    ["A.England", "B.Italy", "C.Argentina", "D.France"],
    ["A.Man City", "B.Man Utd", "C.Liverpool", "D.Arsenal"],
    ["A.Cape Town FC", "B.Kaiser Chiefs", "C.Sundowns", "D.Pirates"]
]

new_game()

while play_again():
    new_game()
