#!/usr/bin/env python3
import pyAesCrypt
import io,os

bufferSize = 4096
password = '$guessm3'


def encryptData(msg):
	pbdata = str.encode(msg)
	fIn = io.BytesIO(pbdata)
	fCiph = io.BytesIO()
	pyAesCrypt.encryptStream(fIn, fCiph, password, bufferSize)

	dataToSend = fCiph.getvalue()
	return dataToSend


def decryptData(msg):
	
	fCiph = io.BytesIO()
	fDec = io.BytesIO()

	fCiph = io.BytesIO(msg)
	ctlen = len(fCiph.getvalue())
	fCiph.seek(0)

	pyAesCrypt.decryptStream(fCiph, fDec, password, bufferSize, ctlen)
	decrypted = str(fDec.getvalue().decode())
	return decrypted

def encryptFile(password, file):
	if len(file) < 1 or len(password) < 1 or not os.path.isfile(file): return '> Enter correct file/password.\n'
	newfile = file + '.aes'
	bufferSize = 64 * 1024
	try:
		pyAesCrypt.encryptFile(file, newfile, password, bufferSize)
		return '> Encrypted: ' + newfile + '\n'
	except:
		return '> Error while encrypting, try again.\n'

def decryptFile(password, file):
	if len(file) < 1 or len(password) < 1 or not os.path.isfile(file): return '> Enter correct file/password.\n'
	try:
		newfile = os.path.splitext(file)[0]
	except: newfile = 'decrypted.' + file
	bufferSize = 64 * 1024
	try:
		pyAesCrypt.decryptFile(file, newfile, password, bufferSize)
		return '> Decrypted: ' + newfile + '\n'
	except:
		return '> Error while decrypting, try again.\n'
