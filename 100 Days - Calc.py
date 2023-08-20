def sub(x,y):
    return x - y

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

operations = {"+": add, "-": sub, "*": multiply, "/": divide}

def calculator():
    num1 = float(input("What's the first number: "))

    cont_flag = True

    while cont_flag:

        num2 = float(input("What's the second number: "))

        for i in operations:
            print(i)
        symbol = input("Pick an operation: ")
        answer = operations[symbol](num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        cont = input("Type 'y' to continue calculating with " + str(answer) + ", or type 'n' to exit: ")
        if cont == 'y':
            num1 = answer
        else:
            cont_flag = False
            print("-----------")
            calculator()
            
calculator()