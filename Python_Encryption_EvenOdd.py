plain_text = input("What is the text you would like to encrypt?: ")

odd_chr = plain_text[0::2]
even_chr = plain_text[1::2]

print (odd_chr + even_chr) #encrypted text

while True:
   password = input("To decrypt the message, enter the password: ")
   if password == "incorrect":
      print (plain_text)
      break
   else:
      print ("Password is incorrect, please try again")