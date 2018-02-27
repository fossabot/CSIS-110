# Nishant Srivastava
# 11/13/17
# Homework 2 - Collage Implementation
# The following code will help make a collage of a picture I took at a school at a minimum amount of four times.
import random # Imported random for possible ways of manipulating the picture.
import time  # Imported time to use for sleeping.

originalPicture = makePicture(getMediaPath("newpicture.png")) # gets the original picture
originalMusic = makeSound(getMediaPath("Remk-Haunting.wav")) # idk, but i just wanted to add music!

def sunSet(originalPicture): # I got this from page 95 from the Python book.  I added only one more part of it, not really a sunSet then?
  originalPicture = makePicture(getMediaPath("newpicture.png")) # gets the original picture
  for p in getPixels(originalPicture):
    theValue = getBlue(p)    
    setBlue(p, theValue*10)
    theValue2 = getGreen(p)
    setGreen(p, theValue2*35)
  return(originalPicture)

def scaryFuture(originalPicture): # Got this from an old lab.
  originalPicture = makePicture(getMediaPath("newpicture.png")) # gets the original picture
  for p in getPixels(originalPicture):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    theScaryScaryPartParty = makeColor(255-30, 255-green, 255-blue)
    setColor(p,theScaryScaryPartParty)
  return (originalPicture)
  
def imRunningOutOfIdeas(originalPicture): # I got this from page 126 from the Python book that we recieved in class.  I didn't change anything here, but I made up for it in the next function.
  originalPicture = makePicture(getMediaPath("newpicture.png")) # gets the original picture
  for p in getPixels(originalPicture):
    x = getX(p)
    y = getY(p)
    if y < getHeight(originalPicture)-1 and x < getWidth(originalPicture)-1:
      sum = getRed(p)+getGreen(p)+getBlue(p)
      haxxer = getPixel(originalPicture,x+1,y+1)
      sum2 = getRed(haxxer)+getGreen(haxxer)+getBlue(haxxer)
      difference = abs(sum2 - sum)
      newcolor = makeColor(difference,difference,difference)
      setColor(p,newcolor)
  return(originalPicture)

def lastFunction(originalPicture): # I got this from page 121 from the Python book that we recieved in class.  This is my last function (not because I ran out of ideas, because I'm lazy).
  originalPicture = makePicture(getMediaPath("newpicture.png")) # gets the original picture  
  for p in getPixels(originalPicture):
    red = getRed(p)
    blue = getBlue(p)
    green = getGreen(p)
    if(red > 5):
      red = red+31
      blue = blue-42
      green = green/23
      setRed(p,red)
      setBlue(p,blue)
      setGreen(p,green)
  return(originalPicture)

def mirrorHorizontal(originalPicture): # got from Python book
  mirrorPoint = int(getHeight(originalPicture)/2)
  for yOffset in range(0,mirrorPoint):
    for x in range(1,getWidth(originalPicture)):
      pbottom = getPixel(originalPicture,x,yOffset+mirrorPoint)
      ptop = getPixel(originalPicture,x,mirrorPoint-yOffset)
      setColor(pbottom,getColor(ptop))
  return(originalPicture)
  
def createCollage():
  originalMusic = makeSound(getMediaPath("Remk-Haunting.wav")) # idk, but i just wanted to add music!
  originalPicture = makePicture(getMediaPath("newpicture.png")) # gets the original picture
  play(originalMusic) # Plays the song, silly!
  showInformation("Please turn up your volume for the best experience EVER!!!!")
  showError("I'm storing your name so I can return a nice message at the end") # Just a quick notification message.
  instructorName = requestString("What is your name, sir/ma'am?") # Storing this as a variable to use later.
  time.sleep(2) # Quick nap!
  showInformation("I'll begin by showing you what the original picture looks like.") # Shows some information.
  show(originalPicture) # Shows the original picture.
  time.sleep(4) # Quick nap!
  showInformation("Okay, I'm now going to create the collage.  Sit tight. :)") # Displaying some information.
  theCanvas = makeEmptyPicture (980, 2*getHeight(originalPicture)) # Creating the canvas
  a = sunSet(originalPicture)# I set the variable a to one of the functions.
  b = lastFunction(originalPicture)# I set the variable b to one of the functions.
  c = imRunningOutOfIdeas(originalPicture)# I set the variable c to one of the functions.
  d = scaryFuture(originalPicture)# I set the variable d to one of the functions.  s.
  copyInto(originalPicture, theCanvas, 1, 0) # I'm inserting the original picture to the top left corner of the canva
  print("step 1 done") # Just for testing purposes.
  copyInto(a, theCanvas, getWidth(originalPicture), 0) # Placement of the picture.
  print("step 2 done") # Just for testing purposes.
  copyInto(b, theCanvas, getWidth(originalPicture)+190, 0) # Placement of the picture.
  print("step 3 done") # Just for testing purposes.
  copyInto(c, theCanvas, getWidth(originalPicture)+380, 0) # Placement of the picture.
  print("step 4 done") # Just for testing purposes.
  copyInto(d, theCanvas, getWidth(originalPicture)+580, 0) # Placement of the picture.
  print("step 5 done") # Just for testing purposes.
  mirrorHorizontal(theCanvas) # Mirroring.
  print("step 6 done") # Just for testing purposes.
  show(theCanvas) # Showing the canvas here.
  time.sleep(3) # Quick nap!
  print("Hey " + instructorName + ", thanks for checking out this homework.") # Conclusion!
  showError("The song is called Haunting created by Remk.") # Song credit.
  stopPlaying(originalMusic)
