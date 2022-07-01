words = ("книга", "ручка", "карандаш", "фломастер")

import random

right_word = random.choice(words)
number_of_letters = "*" * len(right_word)
number_of_tries = 4
number_of_tries = number_of_tries - 1
wrong_tries = 0
letters_used = ""

print("Угадайте слово, у вас есть 10 попыток")

while wrong_tries < number_of_tries and number_of_letters != right_word:
    your_guess = input("введите букву: ")
    your_guess = your_guess.lower()
    print("слово выглядит так ", number_of_letters)

    while your_guess in letters_used:
        print("вы уже использовали эту букву ")
        your_guess = input("введите букву: ")
        your_guess = your_guess.lower()
    letters_used += your_guess
    
    if your_guess in right_word:
        print("вы угадали букву ")
        right_letter = ""
        for i in range(len(right_word)):
            if your_guess == right_word[i]:
                right_letter = right_letter + your_guess
            else:
                right_letter = right_letter + number_of_letters[i]
        right_letter = number_of_letters
    else:
        print("этой буквы нет в слове ")
        wrong_tries = wrong_tries + 1

if wrong_tries == number_of_tries:
    print(number_of_tries)
    print("вы проиграли - конец игры ")
else:
    print("победа ")
print("загаданное слово было ", right_word)