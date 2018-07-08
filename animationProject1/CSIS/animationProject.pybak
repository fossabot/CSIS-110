# Nishant Srivastava
# Animation Homework
# 5/4/18

background = makePicture(getMediaPath("background.jpg")) # Maze picture
accessGranted = makePicture(getMediaPath("meme.jpg")) # Meme!



def makeAnimation(directory):
  for num in range(1, 231): # 230 frames
    canvas = makePicture(getMediaPath("background.jpg")) # Background
    accessGranted = makePicture(getMediaPath("meme.jpg")) # Meme!
    
    if num < 53:
      addArcFilled(canvas, 305, 6+num, 10, 10, 0, 360, red) 
    elif 54 < num < 92:
      addArcFilled(canvas, 305+num, 58, 10, 10, 0, 360, red) 
    if 91 < num < 140:
      addRectFilled(canvas, 0, 0, getWidth(canvas), getHeight(canvas), red)                                       
      stringg = "Enabling M4Z{_H4X$..."
      stylee = makeStyle(sansSerif, bold, 35)
      addTextWithStyle(canvas, 35, 50+(num), stringg, stylee, makeColor(67, 253, 2)) 
      copyInto(accessGranted, canvas, 40+num, 15)                                                                            
    if 139 < num < 192:
      addArcFilled(canvas, 396-(num*2), 58+num, 10, 10, 0, 360, red)                                                                                                                      
    if 191 < num < 231:
      addArcFilled(canvas, 16, (248+(num/10))+10, 10, 10, 0, 360, red) 
    
                                                                                                                                                                                                                                                                                                                                                                                                          
    framenum = str(num)
    if num < 10:
      writePictureTo(canvas, directory+"//frame00"+framenum+".jpg")
    elif num >= 10 and num<100:
      writePictureTo(canvas, directory+"//frame0"+framenum+".jpg")
    if num >= 100:
      writePictureTo(canvas, directory+"//frame"+framenum+".jpg")
      
  
  movie = makeMovieFromInitialFile (directory+"\\frame00.jpg");
  return movie