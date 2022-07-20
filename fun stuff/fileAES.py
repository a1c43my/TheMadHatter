import pyAesCrypt

buffSz = 128 * 1024
password = "password"
# encrypt
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", passw=password, bufferSize=buffSz)
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", passw=password, bufferSize=buffSz)