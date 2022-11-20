from kellanb_cryptography import key
import os
def keyGeneration():
    if os.path.isfile("Generated_Key.txt"):
        with open("Generated_Key.txt","r") as f:
            return f.read()
    return key.gen_random_key()

def keyAndCipherWriting(cipherText,KEY):
    if os.path.isfile("Generated_Key") == False:
        with open("Generated_Key","w") as f:
            f.write(KEY)
    with open("enc_hill.wav.crypt", "w") as f:
	    f.write(cipherText)
    