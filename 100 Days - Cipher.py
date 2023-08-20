alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message,value):

    new = ""
    for i in message:
        cipher = alphabet.index(i)
        position = cipher + value


        if position > len(alphabet):
            position = position - len(alphabet)
        
        new += alphabet[position]

    
    print(f"The encrypted message is {new}")

def decrypt(message,value):
    new = ""
    for i in message:
        cipher = alphabet.index(i)
        position = cipher - value


        if position > len(alphabet):
            position = position - len(alphabet)
        
        old += alphabet[position]

    
    print(f"The original message was {old}")

def caesar(way,message,value):
    new = ""
    for i in message:
        cipher = alphabet.index(i)
        if way == "encode":
            position = cipher + value
            if position > len(alphabet):
                position = position - len(alphabet)

        elif way == "decode":
            position = cipher - value
            if position > len(alphabet):
                position = position - len(alphabet)

        new += alphabet[position]

    print(new)

caesar(direction,text,shift)