# File: homework4.py

''' --- 3) Lists --- '''

''' --- 3.1: List Operations --- '''

favorite_foods = ['pad thai', 'fried chicken', 'BLT', 'avacado toast', 'fettuccine alfredo']

print(favorite_foods[1]) # Prints the second element of the list.
print(favorite_foods[-1]) # Prints the last element of the list.
favorite_foods.append('panner tikka masala') # Adds element to the end of the list.
favorite_foods.insert(0, 'apple') # Adds 'apple' to the 0th index (beginning of the list)
del favorite_foods[2] # Removes the third item from the list.
print(len(favorite_foods)) # Prints length (or number of elements) in the list.

for food in favorite_foods: # Iterates through each element in the list.
    print(food.upper()) # Changes each string to uppercase and prints.

new_list = favorite_foods[::5] 
# Slices leaving 'start' and 'stop' empty to correspond to first and last elements and strides using a 'step' of 5 to keep only the first and last elements.

if 'potato' in new_list:
    print("A Potato!") # Checks if str(potato) is in new_list. Prints a different message if True or False.
else:
    print("No Potato!")

''' --- 3.2) Splicing and Striding ---'''

numbers_list = []
for number in range(21): # Iterates through 0 - 20 (range 'stop' is exclusive)
    numbers_list.append(number) # Adds each number in range(21) to numbers_list

def get_first_15(numbers):
    # Takes a list of numbers and returns the first 15 elements
    return numbers[:16] # 16 bc slicing 'stop' is exclusive.

def get_every_5th(lst):
    # Takes the list from get_first_15() and returns a list with every 5th element.
    every_5th = get_first_15(lst)[::5]
    return every_5th

def reverse_and_stride(lst):
    # Takes the list from get_every_5th returns every 3rd element in reversed order.
    reverse = get_every_5th(lst)[::-1]
    return reverse[::3]

''' --- 3.3) Nested Lists ---'''

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2]) # Prints 3rd row of [numbers]. Note: numbers[2][0:3] would do the same, but the column slice is redundant since the entire row is being printed.
print(numbers[1][1]) # Prints the element in the second row, second column. 
numbers.append([10, 11, 12]) # Adds the list [10, 11, 12] to the end of [numbers].


def sum_nested(nested_list):
    # Takes a nested list, iterates through each row summing each number.
    total = 0
    for row in nested_list:
        total += sum(row)
    return total
# print(sum_nested(numbers))
'''
I encounted this error:

"TypeError 'int' object is not iterable" (detected at line 65, after calling the function at line 67)

I origionally wrote: 

        for num in row:
            total += sum(num)

The sum() function expects an iterable input, such as a list or a tuple, as it's first argument. However; the inner loop iterates through each number
in the current row. For example, on the first iteration, num is 1, so Python attempts to evaluate sum(1). Since an integer is not interable,
this raises a TypeError. 

I fixed it by eliminating the inner row and changing the line to total += sum(row), since row is a list, it is iterable, so sum(row) adds each number in the row
and the result is added to the variable total.
'''


''' --- 3.5) Create a 5 x 5 List --- '''

def create_5x5_list():
    five_by_five_list = [] # Initial empty list.
    # Creates a nested 5 x 5 list of numbers 1-25 (inclusive) using a nested for loop.
    count = 1
    for row in range(5): # creates 5 rows (lists)
        current_row = []
        for column in range(5): # appends the value of count, then adds 1 to count. Loops back to outer loop once multiple of 5 is reached.
            current_row.append(count)
            count += 1  
        five_by_five_list.append(current_row) # adds all 5 lists of numbers to five_by_five_list.
    return five_by_five_list
#five_by_five_list = create_5x5_list()
# print(create_5x5_list())

def replace_multiples_of_3(lst):
    # Takes a nested list and replaces any multiple of 3 with str(?).
    for row in lst:
        for i in range(len(row)):
            if row[i] == "?": # Checks if element has already been replaced, if so, skips that element.
                continue
            elif row[i] % 3 == 0: # Modulus to find multiples of 3. 
                row[i] = "?" 
    return lst

#print(replace_multiples_of_3(five_by_five_list))


"""
I encountered this error:
SyntaxError: expected ':' (detected at line 105)
I origionally wrote: for i in range(len(row))
I forgot the colon at the end of the for-loop line. I fixed it by adding ':' after the last parenthetical.
"""

def sum_numbers(lst):
    # Takes nested list, sums all values not equal to str(?).
    summation = 0
    for row in lst:
        for element in row:
            if element != '?':
                summation += element
                #print(summation)
            else:
                continue
    return summation

#print(sum_numbers(replace_multiples_of_3(five_by_five_list)))


''' --- 4 Dictionaries --- '''

''' ---- 4.1) Dictionary Operations ---'''

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages['Katie']) # Prints the value (30), corresponding to the key "Katie" in {ages}.

ages.update({"Mira": 100}) # Changes Mira's age (value) from 42 to 100.
#print(ages)

ages["Milana"] = 52 # Adds "Milana": 52 to {ages}.
#print(ages)

ages.pop("Mariam") # Removes both the key ("Marium") and corresponding value (42) from {ages}.
#print(ages)


for name, age in ages.items(): # Interates through and prints each name and age from {ages}
    print(f"{name} is {age} years old.")

'''
I encountered the error:
ValueError: too many values to unpack (expected 2) (detected at line 160)
I origionally wrote: for name, age in ages.key(), ages.values():
I forgot to use .items() rather than .keys() and .values(). Python attemted to assign both name and age to .keys() then to .values() raising
a ValueError since there are more than 2 keys / values in ages. I fixed this by changing to: in ages.items(): instead.
'''

print("---Above are all outputs from problems asking for a print statement---")

print("\n") # Creates line break in output.

initial_list = create_5x5_list()
modified_list = replace_multiples_of_3(initial_list)
sum_of_list = sum_numbers(modified_list)
print(f"The result of Nested For Loops (3.5) is the 5 x 5 generated list: \n{create_5x5_list()}, \n\n modified " \
      f"by replacing multiples of 3 with '?': \n{modified_list} \n\n and lastly the sum of all remaining numbers in the list is {sum_of_list}.")


