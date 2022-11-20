from conversion import convertMp3ToWav #Function used for conversion of mp3 to wav
from keyGeneration import keyGeneration,keyAndCipherWriting #Function to get public and private keys
from TextGeneration import generateCipherText,generatePlanText
import numpy as np 
import matplotlib.pyplot as plt
getWavFile = convertMp3ToWav("sound.mp3")
KEY = keyGeneration()
with open(getWavFile,"rb") as f:
    x = f.read().hex()
#generate Encrypted text
cipherText = generateCipherText(x,KEY)
print("Completed Encrypting ..... ")
keyAndCipherWriting(cipherText=cipherText,KEY=KEY)
decrypt = generatePlanText(cipher=cipherText,KEY=KEY)
with open("dec_hill.wav", "wb") as f:
	f.write(bytes().fromhex(decrypt))
print("Completed Decryption")
print("--------------------------------------------")
#code for AES implementation
# row,col = np_data.shape
# str_data = np_data.tostring()
# print(np.fromstring(str_data,dtype=np.int64).reshape(row,col))