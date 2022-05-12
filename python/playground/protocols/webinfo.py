import requests
network_services = {
    80:'http',443:'https'
}
class port():
    def __init__(self,host,port):
        self.vic = host
        self.proto = port
        self.service = self.protocol()
        
    def protocol(self):
        if self.proto in network_services:
            return network_services[self.proto]
        else:
            return 'empty value'

portt = port('localhost',80)
portt2 = port('localhost',443)

print(portt.service)