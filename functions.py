# Addition function
def add(*numbers):
  if not len(numbers) > 1:
    return False

  total = 0

  for number in numbers:
    total += number

  return total

# Division function
def divide(*numbers):
  if not len(numbers) > 1:
    return False

  total = numbers[0]

  for number in numbers[1:]:
    total /= number

  return total

# Multiplication function
def multiply(*numbers):

  # Make sure we have more than one argument, return False otherwise.
  if not len(numbers) > 1:
    return False

  total = 1

  # Multiply all numbers passed by the total, one at a time.
  for number in numbers:
    total *= number

  # Return the total, end function.
  return total

# Subtraction function
def subtract(*numbers):
  if not len(numbers) > 1:
    return False

  total = numbers[0]

  for number in numbers[1:]:
    total -= number

  return total