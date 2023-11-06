while True:
    word = input("Please provide me a palindrome word: ")

    word_to_list = list(word)
    word_to_list_reverse = list(word)
    word_to_list_reverse2 = word_to_list_reverse.reverse()

    if word_to_list == word_to_list_reverse:
        print("The word " + word + " is a palindrome")
    else:
        print("The word " + word + " is not a palindrome")

    play_again = input("Do you want to play again yes/no: ").lower()
    if play_again == "yes":
        continue
    else:
        print("Thank you for playing the game!!!!!1")
        break