""" ---Print Functions--- """

def say_goodbye():
    # Asks user for their name, then prints a goodbye message.
    name = input("What is your name?: ")
    print("Goodbye", name)

# say_goodbye()

def area_of_a_circle(r):
    # Calculates and prints the area of a circle for a given radius r.
    A = 3.14 * r ** 2
    print(A)


""" ---Return Functions--- """

def subtract(a, b):
    # Subtracts b from a
    return a - b


def multiply(c, d):
    # Multiples two numbers
    return c * d


def divide(e, f):
    # Divides one number by another
    return e / f


""" ---Conditionals--- """

def what_should_I_wear(list):
    # Returns a tuple of min and max values from a list of temperatures.
    return (min(list), max(list))

import random
temps = []
for i in range(10):
    temps.append(random.randint(50,100))


def is_weekend(n):
    # Returns whether or not it is the weekend depending on the (numerical) day of the week.
    if n == 6 or n == 7:
        return "It's the weekend!"
    elif n not in range(1,8): # If n is not in (1,8) (exclusive), returns ValueError.
        raise ValueError("Not a Valid Day of the Week: " \
        "The Week Starts on Monday = 1 and Ends on Sunday = 7")
    else:
        return "It's not the weekend."


def fuel_efficiancy_calculator(miles, gallons):
    # Takes miles and gallons of gas; returns mpg.
    return f"{miles / gallons} mpg"


def secret_code(num):
    # Takes an integer, returns a string with last digit moved to the front.
    last_digit = abs(num) % 10
    rest = abs(num) // 10
    if rest == 0:
        return str(num)
    elif num >= 0:
        value = str(last_digit) + str(rest)
    else:
        value = str("-") + str(last_digit) + str(rest)
    return value

""" --- Loops --- """

def power(x, y=int):
    # Calculates x raised to the power of y for integer values of y.
    result = 1
    if x == 0 and y <= 0:
        raise ValueError("Undefined")
    for i in range(abs(y)):
        if y > 0:
            result *= x
        elif y < 0:
            result /= x
    return result

def minimum_for_loop(list):
    # Calculates the minimum of a list of floats and/or integers using a for loop.
    minimum = list[0]
    for number in list:
        if minimum > number:
            minimum = number
        else:
            minimum = minimum
    return minimum

def maximum_for_loop(list):
    # Calculates the maximum of a list of floats and/or integers using a for loop.
    maximum = list[0]
    for number in list:
        if maximum < number:
            maximum = number
        else: maximum = maximum
    return maximum

def minimum_while_loop(list):
    # Calculates the minimum of a list of floats and/or integers using a while loop.
    minimum = list[0]
    index = 1
    while index <= len(list) - 1:
        if minimum > list[index]:
            minimum = list[index]
        index += 1
    return minimum

def maximum_while_loop(list):
    # Calculates the maximum of a list of floats and/or integers using a while loop.
    minimum = list[0]
    index = 1
    while index <= len(list) - 1:
        if minimum < list[index]:
            minimum = list[index]
        index += 1
    return minimum

def sum_of_digits(number):
    # Sums each digit of an integer.
    total = 0
    while number > 0:
        last_digit = number % 10
        total += last_digit
        number //= 10
    return total


x = 10
y = -3
result = power(x, y) # 10 raised to the power of -3

print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")