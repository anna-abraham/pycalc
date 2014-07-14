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

main()