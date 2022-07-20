#!/usr/bin/env python3
import pyAesCrypt,io,time

password = 'randomp4wnage'

def encryptData(buff):
	pbdata = str.encode(buff)
	fIn = io.BytesIO(pbdata)
	fCiph = io.BytesIO()
	pyAesCrypt.encryptStream(fIn, fCiph, password, 4096)
	dataToSend = fCiph.getvalue()
	return dataToSend

t = encryptData('doesntmatterthedata')
y = str(t).replace('CREATED_BY\\pyAesCrypt 6.','').replace('AES','').replace('b','').replace('\'','').replace('\\x00','')
yt = len(y)
st = 0
def fuxer():
    while True:
        print('fuzzinf with {} bytes'.format(len(y[0:st])))
        time.sleep(1)
        st+=5
fuxer()
print('programmed crahsed at {} bytes'.format(st))