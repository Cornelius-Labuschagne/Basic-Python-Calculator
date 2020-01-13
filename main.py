import re

print("The magical Py Calculator.")
print("Created by Cornelius.\n")

print("For the use of basic mathematical calculations.\n")

previous = 0
run = True


def performMath():
    global run
    global previous

    if previous == 0:
        equation = input("Enter an equation or type 'quit' to exit: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print('Good bye hooman.')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
