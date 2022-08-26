# https://www.youtube.com/watch?v=rfscVS0vtbw
# command + / : footnote

# add comment :
# git add .
# git status
# git commit -m "second commit"
# git push -u origin main
# git checkout -b freshman (for other brach)

# Strings
character_name = "Tom"
character_age = "54"
is_male = True
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

print("HK\nAcademy") # change the line
print("HK\"Academy") # include " in the sentence
print("HK\Academy") # include \

phrase = "HK Academy"
print(phrase + " is cool")
print(phrase.lower()) # change as lower
print(phrase.upper()) # change as upper
print(phrase.upper().isupper()) # change as upper and examine whether it is upper
print(len(phrase)) # length including space
print(phrase[0])  # count character from 0 (H)
print(phrase.index("K")) # find the location
print(phrase.index("Acad")) # find the location (0123 - starts)
print(phrase.replace("HK", "George")) # replace with other words

# numbers

print(-2.333) # negative, integer, decimal all fine
print(3 + 4.5) # calculation acceptable
print(3 * (4+5))
print(10 % 3) # give us remainder of 3 -> 1
print(10/3) # 3.333

my_num = 5
print(my_num)
print(str(my_num)) # change number as string
print(str(my_num) + " my favorite number")
# print(my_num + " my favorite number") # this will give an error

my_num = -5
print(abs(my_num)) # gives absolute number -> 5
print(pow(3, 2)) # power function 3^2 -> 9
print(max(4, 6)) # tell us which num is higher -> 6
print(min(4, 6)) # -> 4
print(round(3.2)) # round up or down -> 3

from math import * # math related functions

print(floor(3.7)) # chop off the remained -> 3
print(ceil(3.7)) # round number up -> 4
print(sqrt(36)) # -> 6

# Get input from users

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)
# result: Hello Mike! You are 30

# Calculator

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
#
# result = num1 + num2 # put the string together (10 + 2 -> 102)
# result = int(num1) + int(num2) # put the string as number (10 + 2 -> 12)
# result = float(num1) + float(num2) # accept decimal num as well

# print(result)

# color = input("Enter a color")
# pluoral_noun = input("Enter a plural noun")
# celebrity = input("Enter a celebrity: ")
#
# print("Roses are " + color)
# print(pluoral_noun + " are blue")
# print("I love " + celebrity)

# List []

friends = ["Kevin", "Karen", "Jim"] # make a list

print(friends)
print(friends[1]) #list starts from 0, 1-> Karen
print(friends[-2]) #last starts as -1, -2 -> Karen
print(friends[1:]) # return starts from 1
friends[1] = "Mike"
print(friends[1]) # return Mike
print(friends)

lucky_numbers = [4, 100, 8,15,16,23,42]
print(lucky_numbers[1]) #return 100
friends.extend(lucky_numbers) # combine two groups
print(friends)
friends.append("Cris") # append: add
print(friends)
friends.insert(1, "kelly") # insert : add specific position
print(friends)
friends.remove("Jim") # remove: remove specific
print(friends)
friends.clear() # clear : clear all
print(friends)

friends = ["Kevin", "Karen", "Jim"]
print(friends)
friends.pop() # pop: remove the last element -> return kevin, karen only
print(friends)

print(friends.index("Kevin")) # index: return the position: 0

friends = ["Kevin", "Karen", "Jim", "Jim", "Jim"]

print(friends.count("Jim")) # count: counting the ""
friends.sort() # sort: order as alphabetically
print(friends)
lucky_numbers.sort() # sort: order as increasing order
print(lucky_numbers)
lucky_numbers.reverse() # reverse: reverse the order
print(lucky_numbers)

friends2 = friends.copy() #copy: copy the group
print(friends2)


# Tuples ()

coordinates = (4, 5)
# coordinates[1] = 10 #not possible _ while list is possible
# Tuples is used because it does not be changed or mutated
print(coordinates[1])

coordinates = [(4, 5), (6,7), (80,34)]
print(coordinates[1])
coordinates.insert(1, (1,2))
print(coordinates)

# Functions

def sayhi():
    print("Hello User")

print("Top")
sayhi() # return Hello user
print("Bottom")

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)
say_hi("Mike", "35")
say_hi("Steve", "70")

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
say_hi("Mike", 35)
say_hi("Steve", 70)

# Return statement

def cube(num):
    return num*num*num # Return : to get answer back, it needs return & break
    print("code") # it is after return function: nothing will be printed

result = cube(4)
print(result) # 64

# If statement

is_male = False
is_tall = True

# or, if, else
if is_male or is_tall: # one of them is true
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# and, elif, elif not
if is_male and is_tall: # both should be true
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

# If statement & Comparisons, == >=, <=, !=

def max_num(num1, num2, num3):
    if num1 <= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5)) # return 5


# Building a better calculator

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

# Dictionaries

# Jan -> January
# Mar -> March
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr" : "April",
    1 : "December",
}

print(monthConversions["Mar"]) # print March
print(monthConversions.get("Luv", "Not a valid Key")) # print Not a valid key
print(monthConversions.get("Mar")) # print March
print(monthConversions.get("Luv")) # print None
print(monthConversions[1]) # print December

# While loop

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# Building a guessing game_using while loop, continuous ask
#
# secret_word = "HK"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False #bullian_keep playing
#
# while guess != secret_word and not(out_of_guesses): # false for word & false for (out_of_guesses)
#     if guess_count < guess_limit: # when guess_count is 3 -> out to else
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True #when it is true -> out from while loop
#
# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!") #true for (out_of_guess) -> print this
# else:
#     print("You win!")


# Loop

for letter in "HK Academy":
    print(letter) # print all each letter in the word

for index in range(3, 10):
    print(index) # print out every number in the range (3~9)

friends = ["Jim", "Karen", "Kevin"]
len(friends)
for index in range(len(friends)):
    print(friends[index]) # Jim, Karen, Kevin
    print(friends[2]) # Kevin x3

for friend in friends:
    print(friend) # Jim, Karen, Kevin

for index in range(5): # range 0,1,2,3,4 (first iteration x1, not first x4)
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

# Exponent function

print(2**3) # 2x2x2 = 8
print(2^3) # binary operator (11 - 10 = 01 -> 1)
print(3^6) # binary operator (111 - 11 = 100 -> 5)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num): # for loop (pow_num) repeat
        result = result * base_num # 1 x 3 -> 3 x 3
    return result

print(raise_to_power(3,2)) #9

# 2D lists & nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][1]) # give 2

for row in number_grid:
    for col in row: # 1,2,3, [1,2,3]
        print(col)
    print(row)

# Build a translator

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase: "))) # if I put On -> Gn, aeiou -> ggggg, AEIOU -> GGGGG

# Comments
'''
ewrewrewr
'''
# This program is cool
print("Comments are fun")

# Try Except

try:
    answer = 10 / 0 # put value not through input function
    number = int(input("Enter a number: "))
    print(number)
# except:
#     print("Invalid Input")
except ZeroDivisionError as err:
    print("Divided by zero")
except ValueError:
    print("invalid input")


# Reading files

employee_file = open("employee.txt", "r") # r means reading
# print(employee_file.readline()[1]) # read first line: Amy -> index[1] -> m
#
# print(employee_file.read()) # read after line

for employee in employee_file.readlines(): # read all
    print(employee)
employee_file.close() # once it is done, close the file

# Writing to files

employee_file = open("employees.txt", "w") # a means append, w: overwrite
employee_file.write("Toby - Human Resources")
employee_file.write("Toby2 - Human Resources")
employee_file.write("\nKelly - Customer Service") #put this in the new line
employee_file.close() # once it is done, close the file


employee_file = open("index.html","w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()

# Modules and Pip

# import useful_tools # ?? not available module - couldn't find
# print(useful_tools.roll_dice(10))

# Classes & Objects

from Student import Student # Make new module as student.py first

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.gpa)
print(student2.gpa)

# Building a multiple choice quiz

# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# from Question import Question
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct")
#
# run_test(questions)

# Object Functions

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False) # Check whether it is over 3.5

print(student2.on_honor_roll())

# Inheritance

from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()


