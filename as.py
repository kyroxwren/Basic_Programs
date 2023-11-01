from termcolor import colored

print("This is the default text color in terminal")
print()
print(colored("This is a red text in terminal", "red"))
print()
print(colored("This is a green text in terminal", "green"))
print()
print(colored("This is a red text with a green background", "red", "on_green"))
print()

word_list = ['Hello', 'world']

for word in word_list:
    print(colored(word, "yellow"), end=' ')
print()