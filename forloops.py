def recursive_function(number):
  number -= 1

  if number > 10:
    print(number)
    number = recursive_function(number)

def main():
  # Take user input in the form of '1 2 3 4 5'
  print("Enter some numbers, motherfucker.")
  numbers = input('>')

  # Split input into an array by spaces (' ')
  # '1 2 3 4 5' -> [1, 2, 3, 4, 5]
  numbers = numbers.split(" ")

  # Loop through the resulting array to add all of the numbers together
  total = 0

  for i in numbers:
    print(i)
    total += int(i)
 
  print(total)

def example():
  number = input("Enter a number: ")

  try:
    print(10 + int(number))

  except ZeroDivisionError:
    print("This will ONLY run if you divided by zero.")

  except ValueError:
    print("Why did you use a string, dumbass?")

  except:
    print(sys.exc_info()[0])
    print("Some other error I'm unaware of has occurred.")

  else:
    print("This runs ONLY if we succeeded.")

  finally:
    print("This will run regardless of whether or not the program succeeded.")

def generate_invitations():
  # Dear <name>,
  # Please come to my birthday party. I'm 4 years old, and I'm very cool.

  names = ['Noddy', 'Anna', 'Joe', 'Tramp', 'Jolly', 'Jumper', 'Piggy', 'Ivy', 'Jessica', 'Stephaniehaha']

  for name in names:
    print("Dear %s,\nPlease come to my birthday party. I'm 4 years old, and I'm very cool.\n\n" % (name))

#main()
#example()
generate_invitations()