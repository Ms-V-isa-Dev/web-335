#==============================================
#; Title:  Exercise 8.3
#; Author: Verlee Washington
#; Date:   20 June 2020
#; Modified by:
#; Description: Creating functions for
#               calculations and printing them.
#;=============================================

# program start
# input
firstNumber = input("Enter a number: ")
secondNumber = input("Enter a second number: ")

# addition calculation
def add(firstNumber, secondNumber):
    return firstNumber + secondNumber
result = float (firstNumber) + float (secondNumber)
print(result)

# subtraction calculation
def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber
result = float (firstNumber) - float (secondNumber)
print(result)

# division calculation
def divide(firstNumber, secondNumber):
    return firstNumber / secondNumber
result = float (firstNumber) / float (secondNumber)
print(result)
# program end
