from analyzer import processAudioFiles, isCrying
if __name__ == '__main__':
  
  sounds = ["cry.wav"]
  a,b,c,d = processAudioFiles(sounds)

  result = isCrying(a,b,c,d)
  print(result)