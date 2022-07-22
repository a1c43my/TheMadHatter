import requests

t = requests.get('http://localhost:81/react-php/api/index.php?tp=feed')
t2 = str(t.text)