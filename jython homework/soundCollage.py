# Nishant Srivastava
# 2/13/18
# The code below completes the task of homework number four which is to bring five sounds together and change them up so it's a collage.

import random

def copy (source, target, start): # Copy function.
  targetIndex = start
  for sourceIndex in range(0, getLength(source)):
    sourceValue = getSampleValueAt (source, sourceIndex)
    setSampleValueAt (target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1

def clip (source, start, end): # Clip function.
  target = makeEmptySound (end - start, 44100)
  targetIndex = 0
  for sourceIndex in range (start, end):
    sourceValue = getSampleValueAt (source, sourceIndex)
    setSampleValueAt (target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1
  return target

def sampleValueMax(sound): # Sets the sample high for both spectrums (high & low).
    for sample in getSamples(sound):
      value = getSampleValue(sample)
      if value >= 0:
        setSampleValue(sample, 2000) # I decided to modify this so the sample value wouldn't cause the audio to be too fuzzy.
      if value < 0:
        setSampleValue(sample, -2000) # I decided to modify this so the sample value wouldn't cause the audio to be too fuzzy.
        
def increaseVolume(sound): # Increases the volume of the sound.
  samples = getSamples(sound)
  for index in range(len(samples)):
    sample = samples[index]
    value = getSampleValue(sample)
    setSampleValue(sample, value * 5)

def increaseVolumeOverTime(sound): # Sets sample values of each value greater than or equal to zero (0) to a random value.
    for sample in getSamples(sound):
      newNumbertoMultiply = random.randint(30, 1000)
      value = getSampleValue(sample)
      if value >= 0:
        setSampleValue(sample, value * newNumbertoMultiply)

def soundCollage():
# load original sounds into memory (use your own filenames)
  s1 = makeSound (getMediaPath("GucciGang.wav")) # https://www.youtube.com/watch?v=4LfJnj66HVQ
  s2 = makeSound (getMediaPath("Enemies.wav")) # https://www.youtube.com/watch?v=x-tBCkDNd00&feature=youtu.be
 
  canvasLen = getLength(s2) + getLength(s2) + getLength(s2) + getLength(s2) + getLength(s2)
  canvas = makeEmptySound (canvasLen, 48000)
  
  #Insert original sounds, with silence after each
  copy (s1, canvas, 0)
  copy (s2, canvas, 207357 + getLength(s1))
   
  #Three alterations and insertions ...
  
  alterationNumber1 = makeSound (getMediaPath("GucciGang.wav")) # Fuzzy sounding version.
  sampleValueMax(alterationNumber1)   
  copy (alterationNumber1, canvas, getLength(s1) + getLength(s2) + (getLength(s1) + getLength(s2) * 3/10))
  
  alterationNumber2 = makeSound (getMediaPath("GucciGang.wav")) # Louder version of the sound.
  increaseVolume(alterationNumber2)
  copy (alterationNumber2, canvas, getLength(s1) + getLength(s2) + getLength(alterationNumber1) + (getLength(alterationNumber1) + getLength(s1) + getLength(s2) * 3/10))
 
  alterationNumber3 = makeSound (getMediaPath("Enemies.wav")) # Increase or decrease every sample by a different random amount until the sound is just barely recognizable  [you said this was fine].
  increaseVolumeOverTime(alterationNumber3)
  copy (alterationNumber3, canvas, getLength(s1) + getLength(s2) + getLength(alterationNumber1) + getLength(alterationNumber2) + (getLength(s1) + getLength(s2) + getLength(alterationNumber1) + getLength(alterationNumber2) * 3/10))
 
   x = str(getLength(alterationNumber3))
  xx = str(getLength(canvas)/48000)
  print("The sampling rate of this soundCollage is 48000 hz!  There are " + x  + " samples in the final sound.  The sound in total is " + xx + " seconds long!") # For some odd reason, the code lags here.
  showInformation("I hope you enjoy!")
  
  play(canvas)
