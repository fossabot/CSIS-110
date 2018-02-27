def test():
  g = input("Grade out of 100?")
  print "Alright bud, so you're telling me that a student got a " , g,"%?"
  if g == 100:
    print "A+"
  elif g >= 90:
    print "A"
  elif 80 <= g <= 89:
    print "B"
  elif 70 <= g <= 79:
    print "C"
  elif 65 <= g <= 69:
    print "D"
  else:
    print "F - might as well drop out or ="
    
    
    
def elevatorStuff():
  button = int(raw_input("What button is pressed ->"))
  card = raw_input("Do you have a club card  (Y or N) ->")
  print("Alright, give me a second...")
  
  if button == 26:
    if card.upper() == "Y":
      print("Successfully transported you to the 26th floor.")
    else:
      return("Sorry, but you don't have access to that floor because you don't have the club card.")
  elif 1 <= button <= 12:
    print"Successfully transported you to floor number ", button,"."
  elif button == 14:
    print "Successfully transported you to floor number 13."
  elif button == 15:
    print "Successfully transported you to floor number 14."
  elif button == 16:
    print "Successfully transported you to floor number 15."
  elif button == 17:
    print "Successfully transported you to floor number 16."
  elif button == 18:
    print "Successfully transported you to floor number 17."
  elif button == 19:
    print "Successfully transported you to floor number 18."
  elif button == 20:
    print "Successfully transported you to floor number 19."
  elif button == 21:
    print "Successfully transported you to floor number 20."
  elif button == 20:
    print "Successfully transported you to floor number 21."
  elif button == 21:
    print "Successfully transported you to floor number 22."
  elif button == 22:
    print "Successfully transported you to floor number 23."
  elif button == 23:
    print "Successfully transported you to floor number 24."
  elif button == 24:
    print "Successfully transported you to floor number 25."
  else:
    return "Sorry buddy, but you inputed a number that could not be used on this elevator."
    
## OTHER IDEA

def elevatorStuff2():
  button = int(raw_input("What button is pressed ->"))
  card = raw_input("Do you have a club card  (Y or N) ->")
  print("Alright, give me a second...")
  
  if button == 26:
    if card.upper() == "Y":
      print("Successfully transported you to the 26th floor.")
    else:
      return("Sorry, but you don't have access to that floor because you don't have the club card.")
  elif 1 <= button <= 12:
    print"Successfully transported you to floor number ", button,"."
  elif button == 14:
    print "Successfully transported you to floor number 13."
  elif 14 < button < 26:
    print "Successfully transported you to floor number ", button,"."
  else:
    return "Sorry buddy, but you inputed a number that could not be used on this elevator."
 

def parts(string):
  for letter in string:
    print letter
    
def parts1(string):
  for chars in string:
    print chars*3
    
def justvowels(string):
  for letter in string:
    if letter in "aeiou":
      print letter,

def justvowels(string):
  for letter in string:
    if letter in "aeiouAEIOU":
      print letter,
      
def notvowels(string):
  x = 0
  count = 0
  for letter in string:
    if not (letter in "aeiouAEOIUs"):
     # print letter
      x = x + 1
      count+=1
  print("There are " + str(count)+ " constanants")
  
def countS(text):
  counter = 0
  for letter in text:
    if letter in "sS":
      counter+=1
  return counter
  
def vowels(string):
  result =""
  for char in string:
    if char in "aeiouAEIOU":
      result = result+char
  return result


def firstTwo(string):
  print string[0:2]
  
#def firstTwo(string):
 # num = len(string)
#  print string[0:2]+string[num-2:num]

def adventOfCode(puzzle):
  for p in puzzle:
    print p

def firstHalf(string):
  a = string.split(' ', 1)[0]
  print a
  
def reverse(string):
 gnirts = ""
 for i in range(len(string)-1,-1,-1):
   gnirts = gnirts + string[i]
 print(gnirts)
 
def lengthen(string):
    for letter in string:
      print letter,
