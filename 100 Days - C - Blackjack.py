import random

deck = [11,1,2,3,4,5,6,7,8,9,10,10,10]

def calculator(cards):
    total = 0
    for i in cards:
        total += i
    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        position = cards.index(11)
        cards[position] = 1
    return total

def compare():
    
    if your_score == computer_score:
        print("Draw")
    elif your_score == 0:
        print("You win")
    elif computer_score == 0:
        print("You lose")
    elif your_score > 21:
        print("You lose")
    elif computer_score > 21:
        print("You win")
    elif your_score > computer_score:
        print("You win")
    else:
        print("You lose")

def deal_cards():
    card = random.choice(deck)
    return card

computer = []
you = []
game_over = False

for i in range(2):
    you.append(deal_cards())
    computer.append(deal_cards())

while not game_over:

    your_score = calculator(you)
    computer_score = calculator(computer)

    print(f"Your hand is {you} with a value of {your_score} ")

    if your_score == 0 or computer_score == 0 or your_score > 21:
        game_over = True
    else:
        decision = input("Do you want to hit or stick? ")
        if decision == 'hit':
            you.append(deal_cards())
        else:
            game_over = True

while computer_score != 0 and computer_score < 17:
    computer.append(deal_cards())
    computer_score = calculator(computer)
print(f"The computer has {computer} with a value of {computer_score}")
compare()


