import string

def caesar(text, shift, alphabets):   # input format of caesar encryption

   def shift_alphabet(alphabet):
      return alphabet[shift:] + alphabet[:shift]
   

   shifted_alphabets = tuple(map(shift_alphabet, alphabets))
   final_alphabet = ''.join(alphabets)
   final_shifted_alphabet = ''.join(shifted_alphabets)
   table = str.maketrans(final_alphabet, final_shifted_alphabet)
   return text.translate(table)


plain_text = input("Enter the text you want to encrypt: ")   # sentence to encrypt
print(caesar(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))   # no. of alphabets moved is determined here