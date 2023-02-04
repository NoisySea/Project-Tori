while True:
   # options given to user
   print("Addition: 1")
   print("Subtraction: 2")
   print("Multiplication: 3")
   print("Division: 4")
   print("Quit: q")

   choice = input("What do you want to do?: ")

   if choice == "q":
      break   # quits calculator
   
   num1 = float(input("Input your first number: "))   # float to allow decimals
   num2 = float(input("Input your second number: "))

   if choice == "1":
      print(num1, "+", num2, "=", (num1+num2))
   elif choice == "2":
      print(num1, "-", num2, "=", (num1-num2))
   elif choice == "3":
      print(num1, "*", num2, "=", (num1*num2))
   elif choice == "4":
      if num2 == 0.0:   # cannot be 0 as it is defined in floats
        print("ERROR: Divided by Zero")   # numbers cannot be divided by 0
      else:
        print(num1, "/", num2, "=", (num1/num2))
   else:
      print("invalid choice")   # in case the input choice is not one of the options given
   print()   # space between answer and next calculation
   print()
   print()