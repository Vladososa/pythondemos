# plus
def add(x, y):
    return x + y

# minus


def subtract(x, y):
    return x - y

# umnozhi


def multiply(x, y):
    return x * y

# deleniee


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # vzimam vhoda
    choice = input("Enter choice(1/2/3/4): ")

    # burza proverka kakvo sum vzel
    if choice in ('1', '2', '3', '4'):
        
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("ne pishi dumi bro!")

        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("kazah ti bez dumi")

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # iskam li pak da smqtam
        # chupi ako ne iskam
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
