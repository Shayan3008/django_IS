from kellanb_cryptography import key
import os
def keyGeneration():
    if os.path.isfile("chats/audio/Generated_Key.txt"):
        with open("chats/audio/Generated_Key.txt","r") as f:
            return f.read()
    return key.gen_random_key()

def keyAndCipherWriting(cipherText,KEY):
    if os.path.isfile("chats/audio/Generated_Key") == False:
        with open("chats/audio/Generated_Key","w") as f:
            f.write(KEY)
    with open("chats/audio/audio.wav", "w") as f:
	    f.write(cipherText)