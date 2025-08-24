import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

arithmetic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    more_operations = True
    n1 = float(input("What is the first number?: "))

    while more_operations:
        for operation in arithmetic:
            print(operation)
        operation = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        output = arithmetic[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {output}\n")

        next_operation = input(f"Type 'y' to continue calculation with {output}, or type 'n' to start a new calculation: ").lower()
        if next_operation == "y":
            n1 = output
        else:
            more_operations = False
            print("\n" * 20)
            calculator()

calculator()