
remove = "This is line 3"
replace = "replaced"

def replaceit(file):
    inputfile = file
    try:
        with open(file,'r') as t2:
            print(f"file {file} is open\n")
            data = t2.read()
            data = data.replace(remove,replace)

        with open(file, 'w') as file:
            print(f"replacing data in file {inputfile}")
            file.write(data)
            
    except FileNotFoundError as l:
            print('file doesnt seem to exist, skipping on')
            pass

for x in range(1,4):
    try:
        replaceit(f"file{x}.txt")
    except Exception as l:
        print(l)