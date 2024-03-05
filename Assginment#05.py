class BasicMathOperations:
    def greet_user(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        print("\nHello,",self.__first_name,self.__last_name)

    def add_numbers(self, num1, num2):
        return num1 + num2

    def perform_operation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero."
        else:
            return "Unsupported operation."

    def square_number(self, num):
        self.__num = num
        return self.__num ** 2

    def factorial(self, num):
        if num < 0:
            return "Invalid input. Number must be non-negative."
        factorial = 1
        if num == 0:
            factorial = 0
        for i in range(1, num + 1):
            factorial *= i
        return factorial

    def counting(self, start, end):
        for number in range(start, end + 1):
            print(number, end=" ")
        print()

    def calculate_hypotenuse(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2
        return (((self.__side1)**2)+((self.__side2)**2)) ** 0.5

    def area_of_rectangle(self, width, height):
        return width * height

    def power_of_number(self, base, exponent):
        return base ** exponent

    def type_of_argument(self, arg):
        return type(arg).__name__


def main():
    operations = BasicMathOperations()
    print("Welcome to Basic Math Operations!")

    while True:
        print("\nPlease choose an operation:")
        print("1. Greet User")
        print("2. Add Numbers")
        print("3. Perform Operation")
        print("4. Square Number")
        print("5. Factorial")
        print("6. Counting")
        print("7. Compute Hypotenuse")
        print("8. Area of Rectangle")
        print("9. Power of Number")
        print("10. Type of Argument")
        print("Enter 'exit' to quit.")

        choice = input("Your choice: ")

        if choice == 'exit':
            break

        if choice == '1':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            operations.greet_user(first_name, last_name)

        elif choice == '2':
            num1 = float(input("Enter num1: "))
            num2 = float(input("Enter num2:"))
            print("\nSum:", operations.add_numbers(num1,num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")
            print("\nResult:", operations.perform_operation(num1, num2, operator))

        elif choice == '4':
            num = float(input("Enter a number: "))
            print("\nSquare:", operations.square_number(num))

        elif choice == '5':
            num = int(input("Enter a number: "))
            print("\nFactorial:", operations.factorial(num))

        elif choice == '6':
            start = int(input("Enter start number: "))
            end = int(input("Enter end number: "))
            operations.counting(start, end)

        elif choice == '7':
            side1 = float(input("Enter side 1 length: "))
            side2 = float(input("Enter side 2 length: "))
            print("\nHypotenuse:", operations.calculate_hypotenuse(side1, side2))

        elif choice == '8':
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            print("\nArea of Rectangle:", operations.area_of_rectangle(width, height))

        elif choice == '9':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("\nPower of Number:", operations.power_of_number(base, exponent))

        elif choice == '10':
            arg = input("Enter an argument (will be evaluated as a string): ")
            print("\nType of Argument:", operations.type_of_argument(arg))

        else:
            print("\nInvalid choice. Please select a valid option.")

main()
