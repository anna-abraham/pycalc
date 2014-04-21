#!/usr/bin/env python3
import functions

# Take input
def get_input():
  inp = None
  numbers = []

  while(inp != ''):
    inp = input("Enter a number: ")

    try:
      if int(inp):
        numbers.append(int(inp))

    except Exception:
      if not inp == '':
        print("Enter a number you ass <3")

  return tuple(numbers)

  
# Do the calculation
def main():
  poll = None
  while(poll != "quit"):
    print("What would you like to do? (add, subtract, multiply, divide, quit)")  
    poll = input('>')

    if poll == "add":
      print("Your result is: %d\n\n" % (functions.add(*get_input())))

    elif poll == "divide":
      print("Your result is: %d\n\n" % (functions.divide(*get_input())))

    elif poll == "multiply":
      print("Your result is: %d\n\n" % (functions.multiply(*get_input())))

    elif poll == "subtract":
      print("Your result is: %d\n\n" % (functions.subtract(*get_input())))

    else:
      if not poll == "quit":
        print("Sorry, I didn't understand.")

main()