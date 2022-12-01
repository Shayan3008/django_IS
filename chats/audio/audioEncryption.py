# Function used for conversion of mp3 to wav
from chats.audio.conversion import convertMp3ToWav
# Function to get public and private keys
from chats.audio.keyGeneration import keyGeneration, keyAndCipherWriting
from chats.audio.TextGeneration import generateCipherText, generatePlanText
import os
import uuid


def audioEncrypt(KEY):
    with open("chats/audio/audio.wav", "rb") as f:
        x = f.read().hex()
    # generate Encrypted text
    cipherText = generateCipherText(x, KEY)
    with open("static/audio/"+str(uuid.uuid4())+".txt", "w") as f:
        f.write(cipherText)
    print("Completed Encrypting ..... ")
    keyAndCipherWriting(cipherText=cipherText, KEY=KEY)
    decrypt = generatePlanText(cipher=cipherText, KEY=KEY)
    store_path = "static/audio/"+str(uuid.uuid4())+".wav"
    with open(store_path, "wb") as f:
        f.write(bytes().fromhex(decrypt))
    print("Completed Decryption")
    print("--------------------------------------------")
    os.remove("chats/audio/audio.wav")
    return "/"+store_path
    # code for AES implementation
    # row,col = np_data.shape
    # str_data = np_data.tostring()
    # print(np.fromstring(str_data,dtype=np.int64).reshape(row,col))
