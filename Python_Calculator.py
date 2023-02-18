logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

#Add
def add(n1,n2):
    return n1 + n2
#Subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Calculator
def calculator():
    num1 = float(input("what is the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_loop = True
    while continue_loop:
        operation_symbol = input("pick an operation: ")
        if operation_symbol not in operations:
            print("invalid symbol. Try again")
        else:
            num2 = float(input("What is the next number? "))
            calc_function = operations[operation_symbol]
            answer = calc_function(num1, num2)
            print(f'{num1} {operation_symbol} {num2} = {answer}')
            if input("Type 'yes' or 'no' to continue calculating and press enter: ") == 'yes':
                num1 = answer
            else:
                continue_loop = False
                calculator()

calculator()
