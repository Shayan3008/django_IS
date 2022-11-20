from pydub import AudioSegment
# AudioSegment.ffmpeg = r"C:\Users\DELL\Desktop\IS\ffmpeg"
import os

#function to convert mp3 to wav
def convertMp3ToWav(fileName):
    # files                                                                         
    src = fileName
    dst = "test.wav"
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    return dst
    # os.remove("test.wav")
