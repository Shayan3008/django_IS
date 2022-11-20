from kellanb_cryptography import aes

def generateCipherText(x,KEY):
    cipherText = ""
    cipherText = aes.encrypt_aes(x,KEY)
    return cipherText

def generatePlanText(cipher,KEY):
    return aes.decrypt_aes(cipher,KEY)