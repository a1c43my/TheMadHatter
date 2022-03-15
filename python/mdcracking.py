import hashlib


wordlist_location = str(input('Enter wordlist file location: '))
hash_input = '<paste hash>'
hash_inputs = [ 'paste','list','of','hashes' ] 

def single():
    with open(wordlist_location, 'r') as file:
        for line in file.readlines():
            hash_ob = hashlib.md5(line.strip().encode())
            hashed_pass = hash_ob.hexdigest()
            if hashed_pass == hash_input:
                print('Found cleartext password! ' + line.strip())
                exit(0)
def multimode():
    with open(wordlist_location, 'r') as file:
        for line in file.readlines():
            hash_ob = hashlib.md5(line.strip().encode())
            for hash_input_ in hash_inputs:
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input_:
                    print('Found cleartext password! ' + line.strip())
                    exit(0)