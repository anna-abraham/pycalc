def example():
  number = input()

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

#main()
example()