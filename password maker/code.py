import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890"
def passwordEncryption():
  length = input("How many characters long do you want your password to be?")
  length = int(length)
  generatedPassword = ""
  for x in range(0, length):
    generatedPassword += random.choice(chars)
  print("Your generated password is shown below...")
  return(generatedPassword)
