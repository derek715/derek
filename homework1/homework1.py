# File : homework1.py

# --- Variables & Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals.

b = 1.5
print(b)
print(type(b)) # b is a float, a number with a decimal.

c = 3j
print(c)
print(type(c)) # c is complex, a number with a real part and an imaginary part.

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of text.

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a mutable data structure, of integers: 1, 2, & 3.

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a data structure that maps value(s) to keys. 

g = (1 , 2)
print(g)
print(type(g)) # g is a tuple, an immutable data structure, of integers: 1 & 2.

h = ["apple", "bananana", "strawberry"]
print(h)
print(type(h)) # h is a list of strings

i = True
print(i)
print(type(i)) # i is a boolean or 'bool' for short, a if / or statement with values of True or False.

j = None
print(j)
print(type(j)) # j is a NoneType, an object containing no value.

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, containing a Boolean, string, and integer.

l = str(14)
print(l)
print(type(l)) # l is a string, using the 'str' function is synonymous to using quotations.

m = 1e4
print(m)
print(type(m)) # m is a float, with value 10000.0.

# 1) Nine different data types were found.
# 2) integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
# 3)    b & m : floats, 
#       d & l : strings,
#       e, h, & k : lists,
# 4) l is a string. It is not an integer because it is a string. str() is a function that returns
# a string of the parameter within the parentheses. 
# 5) A set is another datatype which is a collection of unique (aka non-repeated) objects.
n = {1, 1, "one", "two", "three"} # is equal to {1, "one", "two", "three"} or set(1, "one", "two", "three").
print(n)
print(type(n)) # see answer in 5) above.

# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9.
print (10 == 9) # False, 10 does NOT equal 9.
print(10 <= 9) # False, 10 is NOT less than or equal to nine.
print(bool("abc")) # True, the boolean of a string is true.
print(bool(123)) # True, the boolean of an integer is true.
print(bool(["apple", "chery", "banana"])) # True, the boolean of a non-empty list returns true.
print(bool(True)) # True, the Boolean True is True.
print(bool(False)) # False, the Boolean False is False.
print(bool(0)) # False, 0 returns False.
print(bool("")) # False, an empty string returns False.
print(bool(" ")) # True, the string is not empty (as it contains a space), therefore it returns True.
print(bool( () )) # False, an empty tuple returns False.
print(bool([])) # False, an empty list returns False.
print(bool( {} )) # False, an empty set returns False.
print(bool(True and False)) # False, True and False are opposing Booleans.
print(bool(True and True)) # True, both booleans are True, thus the boolean of True and True is True.
print(bool(False and False)) # False, False and False are equivalent and are False.
print(bool(True or False)) # True, one of the booleans is True, thus the conditional is True.
print(bool(True or True)) # True, both booleans are True, thus the conditional is true,
print(bool(False or False)) # False, both booleans are False, thus the condtional is False.
print(bool(not(False))) # True, the negation of False is True.
print(bool(not(True))) # False, the negation of True is False.

# 1) Expressions returning True are non-empty by comparison are true, whereas empty expressions return False.
# 2) bool(0) being False surprised me.
# 3) bool(10 != 5) is True because 1o does not equal 5.
# 4) bool(None) is False because the boolean of NoneType returns False.

# --- Opeartors ---

    # --- Arithmatic Operators ---
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0 , / performs division
print(5 % 2) # 1, % performs arithmatic modulus
print(3 ** 2) # 9, ** performs exponentiation
print(15 // 2) # 7, // performs floor division

    # --- Comparison Operators ---
print(5 == 2) # False, == checks equivalence
print(10 != 10) # False, != checks for non-equivalence
print(2 < 5) # True, < checks if left term is less than right term.
print(12 > 5) # True, > checks if left term is greater than right term.
print(5 <= 6) # True, <= checks if left term is less than or equal to right term.
print(1 >= 10) # False, >= checks if left term is greater than or equal to right term.

    # --- Assignments Operators ---
x = 5
print(x) # 5, x is equal to 5

x += 5
print(x) # 10, += adds then reassigns variable value

x -= 4
print(x) # 6, -= subtracts then reassigns variable value

x *= 3
print(x) # 18, *= multiplies then reassigns variable value

    # --- Logical Operators ---
# 1) 'and' is the logical conjuction operator, it returns true only if both conditions are True; otherwise False.
print(10 > 5 and 5 < 7) # True, both conditions are True.
print(5 > 10 and 5 < 7) # False, only second condition is True.
print(5 > 10 and 7 < 5) # False, both condtions are False.

# 2) 'or' is the logical disjuction operator, it returns True as long as at least 1 condition is True. False if no condition is False.
print(10 > 5 or 5 > 7) # True, first condition is True, second is False.
print(5 > 10 or 5 > 7) # False, neither condtion is True.

# 3) 'not' is the logical negation operator, it flips True <--> False.
print(not 5 > 10) # True, 5 > 10 is False, so not 5 > 10 is True.
print(not 10 > 5) # False, 10 > 5 is True, so not 10 > 5 is False.
print(not True) # (Extra) False, not True is False.

    # --- More Questions ---
# 1) / Performs division, whereas // performs division then rounds to the nearest integer (floor division)
# 2) % Returns the remainder of the quotient, whereas // returns the rounded quotient
# 3) Would use the % operator.
print(17 % 3) # 2, 17 // 3 = 15 with remainder 2.
# 4) Assignment operators set the value of a variable, depending on the operator, may perform a calculation then reassign the value.

# --- Strings ---
my_string = "hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h (element corresponding to index 0)

print(my_string[1]) # Prints: e (element corresponding to index 1)

print(my_string[2]) # Prints: l (element corresponding to index 2)

print(my_string[3]) # Prints: l (element corresponding to index 3)

print(my_string[4]) # Prints: o (element corresponding to index 4)

print(my_string[-1]) # Prints: o (element of last index (here index 4))

print(my_string[1:3]) # Prints: el (ordered elemets corresponding to index 1 & 3)

print(my_string[0:5:2]) # Prints: hlo (ordered elements correspondng to index 0, 5, & 2)

print(len(my_string)) # Prints: 5 (number of elements in my_string

print(my_string + "goodbye") #Prints: hellogoodbye (combines my_string & "goodbye")

print(my_string * 7) # Prints: hellohellohellohellohellohellohello (my_string repeated 7 times)

# 1) 
    # Slicing is the action of taking and combining certain elements of a string.
    # Slicing was done on manipulations 8 and 9.
# 2) 
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski
# 3)
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski
# 4) The latter prints an f-string, used in printing, which allows for variables to be called within curly brackets.

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# List. Use it to print the (non-hidden) contents of the working directory.
# Example: ls Desktop

# ls -a. 
# List all. Use it to print all contents of working directory (including hidden files)
# Example: ls -a Desktop

# mkdir
# Make directory. Use it to create a directory within the working directory.
# Example: mkdir Desktop_Images

# cat
# Catenate. Use it to print the contents of a file.
# Example: cat text.txt

# cd ..
# Change to Parent Directory. Use it to move up one directory.
# Example:
    # > pwd
    # users/derek/desktop/dektop_images
    # > cd ..
    # > pwd
    # > users/derek/dektop


# cd .
# Change to current directory. 
# Example:
    # > pwd
    # users/derek/desktop/desktop_images
    # > cd .
    # > pwd
    # users/derek/desktop/desktop_images.

# cd ~
# Change to Home Directory. Use it to move from working directory to Home directory.
# Example: 
    # > pwd
    # users/derek/desktop/desktop_images
    # > cd ~
    # > pwd
    # users/derek

# cp
# Copy. Duplicates (and can rename) one or more files or directories.
# cp ~/Desktop/textfile1.txt ~/Desktop/textfile2.txt

# mv
# Move. Moves a file or directory.
# Example: mv ~/Desktop/desktop_images/image.png ~/Downloads/desktop_images/image.png

# rm
# Remove. Permenantly deletes a file.
# Example: rm ~/Desktop/text.txt

# clear
# Clear Terminal. Resets the terminal interface.
# Example: clear

# grep
# Global Regular Expression Print. Searches for specfiic lines of text in a file.
# Example: grep "This file is a test" text.txt

# 1) 
    # exit
    # terminates the current terminal session. Use it to end and close the terminal window.
    # Example: exit

    # nano
    # Opens a Text Editor. Use it to edit or create files.
    # Example: nano ~/Desktop/text.txt

    # echo
    # prints in the terminal. Use it to print within the terminal.
    # echo "This is something I want to print."
# 2) ls prints files within the working directory whereas ls -a prints all files, including hidden files, in the working directory.
# 3) A hidden file is a file that is not shown within a directory unless explicitly listed.
# 4) 
    # cp -r: copy with flag -r (recursive), copies directories
    # mkdir -p /1/2/3: make directory with flag -p (parent), creates parent directories.
    # grep with the flag -c: count matches instead of printing said matches.