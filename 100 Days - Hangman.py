#!/usr/bin/env python

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
length = len(chosen_word)

answers = []
i = 0
for i in range(length):
    answers.append("_")

count = 5
while '_' in answers:

    print(answers)
    guess = input("Choose a letter: ").lower()

    for char in range(length):

        if chosen_word[char] == guess:
            answers[char] = guess

    if guess not in chosen_word:
        count -= 1
        print(f"Wrong, you have {count} guesses left.")
    print(answers)

    if count == 0:
        print("you failed")
        break

if "_" not in answers:
    print("You win")