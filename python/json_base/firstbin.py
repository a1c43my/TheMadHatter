import requests,os,time

headers = 'content-type: application/json'
data = '{"sk8fl0": "xxxx"}'
#response = requests.put('https://jsonbase.com/demo_bucket/xxx', headers=headers, params=data)
cmd = f"powershell -c curl -XPUT 'https://jsonbase.com/demo_bucket/xxxddd' -d {data}"
cmd2 = f"powershell -c curl 'https://jsonbase.com/demo_bucket/xxxddd'"
os.system(cmd)
time.sleep(1)
os.system(cmd2)
