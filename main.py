# https://www.youtube.com/watch?v=rfscVS0vtbw
# command + / : footnote
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

secret_word = "HK"
guess = ""

# add comment :
# git add .
# git status
# git commit -m "second commit"
# git push -u origin main