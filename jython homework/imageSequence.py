# Nishant Srivastava
# 10/11/17
# Image Sequence Homework
# The image I included was a picture I took in the morning on my walk to the bus stop.
import random # Importing `random` to use for possible ways of manipulating the picture.
import time #  Importing `time` to use for sleeping (basically waiting [x] seconds).
# Teacher will run, `setMediaPath()`

def sunSet(picture): # I got this from page 95 from the Python book that we recieved in class.  I added only one more part of it, not really a sunSet then? Humph.
  for p in getPixels(picture):
    theValue = getBlue(p)
    setBlue(p,theValue*.5)
    theValue2 = getGreen(p)
    setGreen(p,theValue2*.5)

def scaryFuture(picture): # Basically got this from a recent lab
  for p in getPixels(picture):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    theScaryScaryPart = makeColor(255-red, 255-green, 255-blue)
    setColor(p,theScaryScaryPart)
    
def imRunningOutOfIdeas(picture): # I got this from page 126 from the Python book that we recieved in class.  I didn't change anything here, but I made up for it in the next function.
  for p in getPixels(picture):
    x = getX(p)
    y = getY(p)
    if y < getHeight(picture)-1 and x < getWidth(picture)-1:
      sum = getRed(p)+getGreen(p)+getBlue(p)
      haxxer = getPixel(picture,x+1,y+1)
      sum2 = getRed(haxxer)+getGreen(haxxer)+getBlue(haxxer)
      difference = abs(sum2 - sum)
      newcolor = makeColor(difference,difference,difference)
      setColor(p,newcolor)

def lastFunction(picture): # I got this from page 121 from the Python book that we recieved in class.  This is my last function (not because I ran out of ideas, because I'm lazy).
  for p in getPixels(picture):
    red = getRed(p)
    blue = getBlue(p)
    if(red < 5):
      red = red*59
      blue = blue*12
      setRed(p,red)
      setBlue(p,blue)

def createSequence(): # I started the main function that'd run everything I want above. :)
  picture = makePicture(getMediaPath("itsABeautifulDay.JPG"))
  showError("Don't be alarmed!  The following prompt will only be storing your name for a later use in this assignment.") # I got this straight from JES functions then Input/Output
  name = requestString("What is your name, sir/ma'am?") # I'm going to store your name and use it later. :P
  time.sleep(1) # Waits one second before continuing to run the other functions.
  show(picture) # Shows the picture (original image)
  time.sleep(5) # Waits five seconds before continuing to run the other functions.
  
  sunSet(picture) # Runs the sunSet function.
  repaint(picture)# Repaints the picture.
  time.sleep(3) # Waits five seconds before continuing to run the other functions.
  
  scaryFuture(picture) # Runs the scaryFuture function.
  repaint(picture)# Repaints the picture.
  time.sleep(3) # Waits five seconds before continuing to run the other functions.
  
  imRunningOutOfIdeas(picture) # Runs the imRunningOutOfIdeas function
  repaint(picture)# Repaints the picture.
  time.sleep(3) # Waits five seconds before continuing to run the last function below!

  lastFunction(picture) # Runs the imRunningOutOfIdeas function
  repaint(picture)# Repaints the picture.
  time.sleep(3) # Waits five seconds before continuing to run the last function below!
      
  width = getWidth(picture) + 1 # Gets the width (ENTIRELY)
  height = getHeight(picture) + 1 # Gets the height (ENTIRELY)
  print("Hey there " + name + "!") # Print message
  print("This image's height is " + str(height) + " pixels tall.  The image's width is " + str(width) + " pixels wide.") # Print message
  something = width * height # Calculates the area/total amount of pixels
  print("There appears to be " + str(something) + " pixels in total within this image.")
  time.sleep(2) # Okay!  I've completed the homework, woohoo.
  showError("Thanks for checking out my assignment, have an awesome day, " + name +".") # Cya!
