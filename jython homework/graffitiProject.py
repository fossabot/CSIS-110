# Nishant Srivastava
# 1/8/18
# Graffiti Project

# Picture of Casey Neistat found @ https://goo.gl/485Wpu

import time  # Imported time to use for sleeping.
import random # Imported random for possible ways of manipulating the picture.



facePic = makePicture(getMediaPath("casey.jpg"))
trollPic = makePicture(getMediaPath("Screenshot at Jan 11 19-58-26.png"))


## START NEW FUNCTION BELOW ##
white2 = makeColor(208,173,154)
def teeth(facePic): # Turns the teeth orange
    orange = makeColor (255, 70, 0)
    for facex in range (149, 156):
        for facey in range (108, 113):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, white2) < 160.0):
                setColor (p, orange)
    for facex in range (155, 174):
        for facey in range (109, 113):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, white2) < 160.0):
                setColor (p, orange)

## END NEW FUNCTION ABOVE ##




## START NEW FUNCTION BELOW ##
white1 = makeColor(218,185,166)
def eyes(facePic): # Turns the eyes red
    for facex in range (144, 157):
        for facey in range (75, 82):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, white1) < 100.0):
                setColor (p, red)
    for facex in range (177, 187):
        for facey in range (79, 89):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, white1) < 100.0):
                setColor (p, red)
## END NEW FUNCTION ABOVE ##




## START NEW FUNCTION BELOW ##
def hair(facePic): # Turns the hair purple
    brown = makeColor(83,48,29)
    purple = makeColor(128,0,128)
    for facex in range (118, 212):
        for facey in range (12, 42):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brown) < 140.0):
                setColor (p, purple)
    for facex in range (118, 130): # left side of hair
        for facey in range (28, 79):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brown) < 140.0):
                setColor (p, purple)
    for facex in range (130, 149): # left side of hair (detailed)
        for facey in range (28, 74):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brown) < 75.0):
                setColor (p, purple)
    for facex in range (181, 209): # right side of hair
        for facey in range (34, 74):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brown) < 100.0):
                setColor (p, purple)
    for facex in range (201, 216): # right side of hair (detailed)
        for facey in range (45, 74):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brown) < 120.0):
                setColor (p, purple)
    brownMoreDEtailed = makeColor(106,73,56)
    for facex in range (201, 203): # right side of hair (more detail)
        for facey in range (69, 85):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brownMoreDEtailed) < 50.0):
                setColor (p, purple)
    for facex in range (149, 185): # center part side of hair (detail[omg enufffffff wid dis deteal!!!])
        for facey in range (37, 46):
            p = getPixel (facePic, facex, facey)
            color = getColor (p)
            if (distance (color, brown) < 2050.0):
                setColor (p, purple)
## END NEW FUNCTION ABOVE ##



## START NEW FUNCTION BELOW ##
def sqaureAroundText(facePic): # Makes a rectangle that's filled and adds text within it
  someColor = makeColor(59,178,115)
  addRectFilled(facePic, 0,390,1290,30, someColor)
  myStyle = makeStyle(sansSerif, plain, 9)
  addTextWithStyle(facePic, 0, 410, "Why did the coffee file a police report? Because it was mugged!", myStyle, white) # credit to https://goo.gl/TX3cjZ
## END NEW FUNCTION ABOVE ##


## START NEW FUNCTION BELOW ##
def flashingLights(facePic):
  light1 = makeColor(249,113,113) ## pinish color
  light2 = makeColor(178,238,230) ## mint color
  light3 = makeColor(87,212,255) ## light blue color
  light4 = makeColor(255,179,223) ## pink color
  light5 = makeColor(255,178,1) ## orange color
  canvas1 = makeEmptyPicture(500, 500, light1)
  copyInto(trollPic, canvas1, 30, 50)
  myStyle = makeStyle(sansSerif, plain, 20)
  addTextWithStyle(canvas1, 50, 410, "Flashing Lights", myStyle, white)
  show(canvas1)
  time.sleep(2)
  canvas2 = makeEmptyPicture(500, 500, light2)
  copyInto(trollPic, canvas2, 30, 50)
  myStyle = makeStyle(sansSerif, plain, 20)
  addTextWithStyle(canvas2, 50, 410, "Flashing Lights", myStyle, black)
  show(canvas2)
  time.sleep(2)
  canvas3 = makeEmptyPicture(500, 500, light3)
  copyInto(trollPic, canvas3, 30, 50)
  myStyle = makeStyle(sansSerif, plain, 20)
  addTextWithStyle(canvas3, 50, 410, "Flashing Lights", myStyle, white)
  show(canvas3)
  time.sleep(2)
  canvas4 = makeEmptyPicture(500, 500, light4)
  copyInto(trollPic, canvas4, 30, 50)
  myStyle = makeStyle(sansSerif, plain, 20)
  addTextWithStyle(canvas4, 50, 410, "Flashing Lights", myStyle, black)
  show(canvas4)
  time.sleep(2)
  canvas5 = makeEmptyPicture(500, 500, light5)
  copyInto(trollPic, canvas5, 30, 50)
  myStyle = makeStyle(sansSerif, plain, 20)
  addTextWithStyle(canvas5, 50, 410, "Flashing Lights", myStyle, red)
  show(canvas5)
  time.sleep(2)
  
## END NEW FUNCTION ABOVE



## START FINAL FUNCTION BELOW ##
def graffiti(): #conclusion.
    song = makeSound(getMediaPath("Flashing Lights (mp3cut.net).wav")) # By Kanye West
    play(song) # Plays the song
    showWarning("Here is what the original picture looks like.") # joke from https://goo.gl/TX3cjZ
    show(facePic)
    time.sleep(2)
    showInformation("Shown next is what the new picture looks like after all of the changes.")
    teeth(facePic)
    eyes(facePic)
    hair(facePic)
    sqaureAroundText(facePic)
    flashingLights(facePic)
    time.sleep(2)
    repaint (facePic)
    stopPlaying(song)
    ## END FINAL FUNCTION ABOVE ##
