from adder import add_numbers, substract_numbers, multiply_numbers, divide_numbers

def ask_numbers():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        return x,y
    except ValueError:
        print("Please enter valid numbers.")
        return ask_numbers() #retry

def log_result(operation, x, y, result):
    with open("history.txt", "a") as file:
        file.write(f"{x} {operation} {y} = {result}\n")

def main():
    print("Simple Calculator")
    print("Choose operation: +, -, *, /")

    op = input("Operator: ")

    x, y = ask_numbers()

    if op == "+":
        result = add_numbers(x, y)
    elif op == "-":
        result = substract_numbers(x, y)
    elif op == "*":
        result = multiply_numbers(x, y)
    elif op == "/":
        try:
            result = divide_numbers(x, y)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid operator.")
        return

    print(f"The result is {result}")
    log_result(op, x, y, result)
main()