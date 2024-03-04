import math

# Function to perform calculation based on user input
def calculate():
    # Prompt user to choose math operation
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulo
** for power
sin for sine
cos for cosine
tan for tangent
log for logarithm
sqrt for square root
pi for the value of pi
: ''')
    
    # Display the value of pi if chosen
    if operation == 'pi':
        print(math.pi)
        another_calculation()  # Ask if user wants another calculation
        
    # Prompt user to input numbers for binary operations
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Perform selected operation and display result
    if operation == '+':
        print('{} + {} = '.format(number1, number2), number1 + number2)
    elif operation == '-':
        print('{} - {} = '.format(number1, number2), number1 - number2)
    elif operation == '*':
        print('{} * {} = '.format(number1, number2), number1 * number2)
    elif operation == '/':
        print('{} / {} = '.format(number1, number2), number1 / number2)
    elif operation == '%':
        print('{} % {} = '.format(number1, number2), number1 % number2)
    elif operation == '**':
        print('{} ** {} = '.format(number1, number2), number1 ** number2)
    elif operation == 'sin':
        print('sin({}) = '.format(number1), math.sin(number1))
    elif operation == 'cos':
        print('cos({}) = '.format(number1), math.cos(number1))
    elif operation == 'tan':
        print('tan({}) = '.format(number1), math.tan(number1))
    elif operation == 'log':
        print('log({}) = '.format(number1), math.log(number1))
    elif operation == 'sqrt':
        print('sqrt({}) = '.format(number1), math.sqrt(number1))
    else:
        print('You have not typed a valid operator, please run the program again.')
    
    another_calculation()  # Ask if user wants another calculation

# Function to ask user if they want to perform another calculation
def another_calculation():
    again = input('''
Do you want to perform another calculation?
Please type Y for YES or N for NO.
: ''')
    
    # If user wants another calculation, call calculate() function again
    if again.lower() == 'y':
        calculate()
    # If user does not want another calculation, print farewell message
    elif again.lower() == 'n':
        print('Thank you for using the calculator. Goodbye!')
    # If invalid input, prompt user again
    else:
        again = input('''
Invalid input.
Do you want to perform another calculation?
Please type Y for YES or N for NO.
: ''')

calculate()  # Call calculate() function to start the program
