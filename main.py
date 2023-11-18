# Simple Calculator


def calculator():
    print("This calculator can perform the following operations:")
    print("Addition, Subtraction, Multiplication, Division, Exponent")
    operations = ["add", "sub", "mul", "div", "exp"]

    value_1 = input("Enter first number\n")
    try:
        value_1 = int(value_1)
    except ValueError:
        print("Incorrect format of value 1. Please enter an integer value\n")
        exit()

    value_2 = input("Enter second number\n")
    try:
        value_2 = int(value_2)
    except ValueError:
        print("Incorrect format of value 2. Please enter an integer value\n")
        exit()

    print("Operations: add / sub / mul / div / exp ")
    operation = input("Enter operation you want to perform\n")
    if operation not in operations:
        print("Incorrect format of format of operation")
        exit()

    result = None
    match operation:
        case "add":
            result = value_1 + value_2
        case "sub":
            result = value_1 - value_2
        case "mul":
            result = value_1 * value_2
        case "div":
            result = value_1 / value_2
        case "exp":
            result = value_1 ** value_2

    print(f"The result is {result}\n")
    return


if __name__ == '__main__':
    begin = input("Enter S to start\n")
    if begin == "S" or begin == "s":
        calculator()
    else:
        print("exiting the calculator\n")


