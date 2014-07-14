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