import math

def calculate():
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
    
    if operation == 'pi':
        print(math.pi)
        another_calculation()
        
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
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
        
    another_calculation()

def another_calculation():
    again = input('''
Do you want to perform another calculation?
Please type Y for YES or N for NO.
: ''')
    
    if again.lower() == 'y':
        calculate()
    elif again.lower() == 'n':
        print('Thank you for using the calculator. Good bye!')
    else:
        again = input('''
Invalid input.
Do you want to perform another calculation?
Please type Y for YES or N for NO.
: ''')

calculate()
