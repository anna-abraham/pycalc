def recursive_function(number):
  number -= 1

  if number > 10:
    print(number)
    number = recursive_function(number)


def main():
  recursive_function(100)

main()