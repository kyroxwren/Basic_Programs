import random
import tkinter
from tkinter.constants import *


# This will start the game with and option to fill in a word
def play_game():
    # tk = tkinter.Tk()
    # frame = tkinter.Frame(tk, width=500, height=400, name="wordle")
    # frame.pack()
    # label = tkinter.Label(frame, text="Welcome to wordle")
    # label.pack()
    # button = tkinter.Button(frame, text="Exit", command=tk.destroy)
    # button.pack(side=BOTTOM)
    # tk.mainloop()
    game_attempts = 5
    i = 0
    guessed_words = []

    while i < game_attempts:

        print("------------------------------")
        print("Welcome to wordle")
        print("------------------------------")
        pc_rd_wd = random.choice(random_words)
        guess_word = input("Please write a word: ").lower()
        checked = word_check(guess_word, pc_rd_wd)
        guessed_words.append(checked)
        for letter in guessed_words:
            print(letter)
        correct_word(pc_rd_wd, guess_word)
        i += 1


# This will check the word in put and compare it to the word that has been generated
def word_check(computer_word, guess_word):

    letters =[]
    for i in computer_word:
        for j in guess_word:
            if i == j:
                letters.append(i)
            else:
                letters.append(" ")

    letters_set_like = list(dict.fromkeys(letters))
    return letters_set_like


# this will display the letters required

def correct_word(computer_word, guess_word):

    if computer_word == guess_word:
        print("Congratulations you have won the game\nThe word is: " + str(guess_word))

# this will replay the game


def play_again():
    pass


random_words = ["catch"]

play_game()
