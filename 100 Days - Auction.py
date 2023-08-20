
values = {}

def auction():
    """Store names and bids in a dictionary"""

    print("Welcome to the Auction")
    name = input("What is your name? ")
    bid = int(input("What is your bid? £"))

    values[name] = bid

    again = input("Is there anyone else? ")
    if again == "yes":
        auction()



auction()

max_bid = 0
for i in values:
    if values[i] > max_bid:
        max_bid = values[i]
        max_i = i
    
print(f"{max_i} is the winner with a bid of £{max_bid}")