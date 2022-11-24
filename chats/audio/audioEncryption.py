from chats.audio.conversion import convertMp3ToWav #Function used for conversion of mp3 to wav
from chats.audio.keyGeneration import keyGeneration,keyAndCipherWriting #Function to get public and private keys
from chats.audio.TextGeneration import generateCipherText,generatePlanText

import os

def audioEncrypt():
    KEY = keyGeneration()
    with open("./test.wav","rb") as f:
        x = f.read().hex()
    #generate Encrypted text
    cipherText = generateCipherText(x,KEY)
    print("Completed Encrypting ..... ")
    keyAndCipherWriting(cipherText=cipherText,KEY=KEY)
    decrypt = generatePlanText(cipher=cipherText,KEY=KEY)
    with open("final.wav", "wb") as f:
        f.write(bytes().fromhex(decrypt))
    print("Completed Decryption")
    print("--------------------------------------------")
    # os.remove("test.wav")
    #code for AES implementation
    # row,col = np_data.shape
    # str_data = np_data.tostring()
    # print(np.fromstring(str_data,dtype=np.int64).reshape(row,col))