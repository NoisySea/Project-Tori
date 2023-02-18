import random
while True:
   num = random.randrange (1,10)   # random number generated between 1 and 9
   guess = int(input("Enter any number: "))   # enter guess

   while num != guess:   # if guess is wrong, loop step
      if guess > num:
         print ("TOO HIGH! TRY AGAIN")
         guess = int(input("Enter any number: "))   # retry game
      elif guess < num:
          print ("TOO LOW! TRY AGAIN")
          guess = int(input("Enter any number: "))   # retry game
      else:
         break   # breaks "while" loop
   print ("YOU HAVE GOTTEN IT! CONGRATS!!!")
   
   while True:
      print ("Do you want to continue?")
      con = input("Continue?(y/n): ")   # enter if want to continue game
      if con != "n" and con != "y":
         print("Wrong input, try again")   # if wrong input is given
      else:
         break   # ensures the user gave an input of "y" or "n"
   
   if con == "n":
      print ("Goodbye")
      break   # stops game
   else:
      continue   # continues game