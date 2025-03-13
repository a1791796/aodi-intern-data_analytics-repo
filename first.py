print("I am aodi xie from China!")
print

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

sumresult = num1 + num2
difference = num1-num2

product = num1*num2


if num2 != 0:
    quotient = num1/num2
else:
    quotient = "can't divide by zero"

print(f"num1 = {num1}, num2 = {num2}")
print(f"sum = {sumresult}")
print(f"difference = {difference}")
print(f"product = {product}")
print(f"quotient = {quotient}")

age = int(input("Enter your age in human years:"))
ageindog = age*7
print(f"Your age in dog years is {ageindog}")

food = str(input("Enter your favorite food:"))
print(f"Your favorite food is {food}.")

import random
number = random.randint(1,10)

attempt = 5

print("welcome to the number guessing game!")
print("I am thinking of a number between 1 and 10.")
print("You have 5 attempts to guess the number.")

while attempt >0:
    guess = int(input("Enter your guess:"))
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    attempt = attempt -1
    print(f"You have {attempt} attempts left.")
if attempt == 0:
    print(f"Sorry, you have used all your attempts. The number was {number}.")
print("Game over.")