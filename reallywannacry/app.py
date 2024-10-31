from utils import processAudioFiles, isCrying, calculateTemperature
if __name__ == "__main__":
  sound = ["c1.wav"]
  a, b, c, d = processAudioFiles(sound)
  cry = isCrying(a, b, c, d)
  temp = calculateTemperature()
  print("Crying:", cry)
  print("Temperature:", temp)
  