"""
HANDIN 1 (down payment)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

I first encountered a problem on how to determine whether the input was a float 
or integer as opposed to a string, since the input function always gives strings, 
and if you try to convert it to a float, any non-float will crash the program.
With my initial solution being the following

while True:
    interest_input = float(input("what is the monthly interest rate?(in %): "))
    if type(interest_input) == int or type(interest_input) == float:
        break
    print('please enter a number')

After consulting Stackexchange, I found a valid test using the try function.
https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python

Using simple math and a while loop I then calculated the remaining debt for 
each month, remembering to add an exception for cases, that would result in the 
loop never being broken.
"""



while True:
    loan_input = input("How large is the loan: ")
    try:
        loan=float(loan_input)
        break
    except ValueError:
        print('Please enter a number ')  

while True:
    interest_input = input("What is the monthly interest rate?(in %): ")
    try:
        interest=float(interest_input)
        break
    except ValueError:
        print('Please enter a number: ')
    
while True:
    pay_input = input("What is the monthly payment?: ")
    try:
        pay=float(pay_input)
        break
    except ValueError:
        print('Please enter a number: ')
    
print(' ')
if pay>interest*loan/100:
    print('The remaining debt each month will be:')
    while loan>interest:
        print(loan)
        loan+= loan*interest/100-pay        
else:
    print('Interest exceeds monthly payment, it will never be paid')
    







