# Nishant Srivastava
# Animation Homework - Idea #2
# 5/4/18

canvas = makePicture(getMediaPath("background.jpg")) # Background
fighter1 = makePicture(getMediaPath("fighter1.jpg")) # Fighter 1 [LEFT SIDE = Weird Creature]
fighter2 = makePicture(getMediaPath("fighter2.jpg")) # Fighter 2 [RIGHT SIDE = Spiderman]
rocketLauncher = makePicture(getMediaPath("rocketLauncher.jpg")) # Rocket Launcher
rocketMissle = makePicture(getMediaPath("missle.jpg")) # Missle
boomBoom = makePicture(getMediaPath("boomBoom.jpg")) # Boom boom!



def removeBlack(pic, background, xB, yB):
  blank = makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range(getWidth(pic)):
    for y in range(getHeight(pic)):
      px = getPixel(pic, x, y)
      if getRed(px) == 0 and getBlue(px) == 0 and getGreen(px) == 0:
        bPx = getPixel(background, x + xB, y + yB)
        bCol = makeColor(getRed(bPx), getGreen(bPx),getBlue(bPx))
        setColor(getPixel(blank, x, y),bCol)
      else:
        setColor(getPixel(blank,x,y),makeColor(getRed(px),getGreen(px),getBlue(px)))
  return(blank)



numm = 501
fighter11 = removeBlack(fighter1, canvas, 30, 100) # [LEFT SIDE]
fighter22 = removeBlack(fighter2, canvas, 270, 112) # [RIGHT SIDE]
fighter111 = removeBlack(fighter1, canvas, 30+((numm/10)+5), 100)
fighter222 = removeBlack(fighter2, canvas, 270-((numm/10)+5), 110)
boomBoom1 = removeBlack(boomBoom, canvas, 116, 87)

healthBar = makeColor(5, 255, 159)


def makeAnimation(directory):
  for num in range(1, 501):
    canvas = makePicture(getMediaPath("background.jpg")) # Background
    fighter1 = makePicture(getMediaPath("fighter1.jpg")) # Fighter 1 [LEFT SIDE = Weird Creature]
    fighter2 = makePicture(getMediaPath("fighter2.jpg")) # Fighter 2 [RIGHT SIDE = Spiderman]
    rocketLauncher = makePicture(getMediaPath("rocketLauncher.jpg")) # Rocket Launcher
    rocketMissle = makePicture(getMediaPath("missle.jpg")) # Missle
    boomBoom = makePicture(getMediaPath("boomBoom.jpg")) # Boom boom!  
    addRectFilled(canvas, -3, 10, 800, 25, healthBar)
    addRectFilled(canvas, 225, -2, 50, 50, black)
    if 0 < num < 61:
      copyInto(fighter11, canvas, 30, 100) 
      copyInto(fighter22, canvas, 270, 110)
    elif 60 < num < 131:              
      copyInto(fighter111, canvas, 30+((num/10)+10), 100) 
      copyInto(fighter222, canvas, 270-((num/10)+10), 110)                         
    elif 130 < num <= 201:
      copyInto(fighter111, canvas, 50, 100) 
      copyInto(fighter222, canvas, 230, 110) 
      copyInto(rocketLauncher, canvas, 295, 181)
      copyInto(rocketMissle, canvas, 185-((50/10)+50), 170)
    elif 200 < num < 250:
      copyInto(fighter111, canvas, 50, 100) 
      copyInto(fighter222, canvas, 230, 110) 
      copyInto(boomBoom1, canvas, 50, 87)
      addRectFilled(canvas, -3, 10, 800, 25, healthBar)
      addRectFilled(canvas, 0, 10, (0+(num/10)+180), 25, red)
      addRectFilled(canvas, 225, -2, 50, 50, black)    
    else:
      canvas = makePicture(getMediaPath("background.jpg")) # Background
      copyInto(fighter22, canvas, ((200+(num/10) + 10)), 100)                                                                                                                
      addRectFilled(canvas, -3, 10, 800, 25, healthBar)    
      addRectFilled(canvas, -3, 10, 230, 25, red)
      addRectFilled(canvas, 225, -2, 50, 50, black)                                                                                                                                                                                                                                                                                                                                                                                                                            
      stringg = "Spiderman won!"
      stylee = makeStyle(sansSerif, bold, 20)
      addTextWithStyle(canvas, 30, (num + 80), stringg, stylee, orange)                                                                                                                                                                                                                                                                                                                                                                                                                   
    framenum = str(num)
    if num < 10:
      writePictureTo(canvas, directory+"//frame00"+framenum+".jpg")
    elif num >= 10 and num<100:
      writePictureTo(canvas, directory+"//frame0"+framenum+".jpg")
    if num >= 100:
      writePictureTo(canvas, directory+"//frame"+framenum+".jpg")
      
  
  movie = makeMovieFromInitialFile (directory+"\\frame00.jpg");
  return movie
  
  
  
  
  