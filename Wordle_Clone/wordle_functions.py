import random
from termcolor import colored

# --------------------------- main game ----------------------------------

# This will start the game with and option to fill in a word
def play_game():
    game_attempts = 5
    i = 0
    correct_letters = []
    guessed_words = []

    print("------------------------------")
    print("Welcome to wordle")
    print("------------------------------")

    while i < game_attempts:

        print("------------------------------")
        pc_rd_wd = random.choice(random_words)
        guess_word = input("Please write a word: ").lower()

        guessed_words.append(guess_word)

        checked = word_check(pc_rd_wd, guess_word)
        correct_letters.append(checked)

        print("------------------------------")
        print()
        print("These the correct letters")
        for letter in correct_letters:
            print(letter)
        print()
        print("These are your words you have guessed")
        for letter in guessed_words:
            print(colored(letter,"red"))
        print()

        correct = correct_word(pc_rd_wd, guess_word)
        if correct:
            print("----------------------------------------------------")
            print("Congratulations you have won the game\nThe word is: " + str(guess_word))
            print("----------------------------------------------------")
            break
        i += 1


# ---------------------------------------------------------------------------------


# ------------------------------word checking -------------------------------------
# This will check the word in put and compare it to the word that has been generated
def word_check(computer_word, guess_word):
    letters = []
    for i in computer_word:
        for j in guess_word:
            if i == j:
                letters.append(i)
            else:
                letters.append(" ")

    letters_set_like = list(dict.fromkeys(letters))
    return letters_set_like


# -------------------------------------------------------------------------------------------------


# --------------------------------- Result Confirmation -------------------------------------------
# this will display the letters required

def correct_word(computer_word, guess_word):
    if computer_word == guess_word:
        return True


# --------------------------------------Play again ------------------------------------------------
# this will replay the game
def play_again():
    pass


# --------------------------------------------------------------------------------------------------


random_words = ["catch"]

play_game()
