
def quad():

  a = input()
  b = input()
  c = input()
  
  a = int(a)
  b = int(b)
  c = -(int(c) * 2)
  
  x1 = (-b + (((b ** 2) - 4 * a * c) ** .5)) / (2 * a)
  x2 = (-b - (((b ** 2) - 4 * a * c) ** .5)) / (2 * a)
  
  if (int(x1) == float(x1)):
    print(int(x1))
  elif (int(x2) == float(x2)):
    print(int(x2))
  else:
    print(0)
    



def somethingElse2():
  mainFrame1 = ["Username1", ' - ', 0]
  mainFrame1 = ['Username2 - ', 0]
  a = input("What is your name?") # WELCOME
  print(a+", welcome back to the mainframe.") # WELCOME
  print(" ")
  action = input("If you plan on adding points to a user, please type ADD.  If you plan on deducting points to a user, please type SUBSTRACT.  If you plan on making a new profile, please type NEWPROFILE") # DETERMINE WHAT THE USER IS GOING TO DO
  print(" ")
  
  if (str(action) == "ADD"): # IF USER DOES ADD DO...
    anotherAction = input("First please type the username of the user correctly.  USERNAME MUST BE EXACT")
    print(" ")
    
  if (str(anotherAction) == str(mainFrame1[0])): # CHECKS THE USERNAME IN ARRAY MAINFRAME1
      print("That user is located in " + mainFrame1)
      numberInput = input("How many points do you wish to add to that user?")
      mainFrame1[-1] = mainFrame1[-1] + numberInput
      print(mainFrame1[-1])
  


  
  
  
  
  
  
  
  
  
