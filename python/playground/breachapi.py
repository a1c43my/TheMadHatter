import sys, getopt,time
import requests
import yagmail,sys
# free api on raipdapi
sender_email = '<|youremail@gmail.com|>'
receiver_email = ''
#subject = "Breach Directory"
sender_password = ""
yag = yagmail.SMTP(user=sender_email, password=sender_password)
#
# free api on raipdapi
url = "https://breachdirectory.p.rapidapi.com/"
#
headers = {
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
    'x-rapidapi-key': "yourkeyhere"
    }
#
querystring = {"func":"","term":""}
email = ''
func = ''

def searchq(email_,func_):
    querystring["term"] = email_
    querystring["func"] = func_
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    r=open('yourfile.txt','a')
    r.write(f"Data entry for: {email_}")
    r.write(f"-------------------------\n\n")
    r.write(f"{response.json()}")
    r.write(f"-------------------------")
    r.write(f"-------------------------")
    r.close()
#
    contents = f"data for emali: {email_} \n --------------------- {response.json()}"
    subject = f"Breach Directory : {email_}"
    yag.send(receiver_email, subject, contents)
    print('email sent')


def main(argv):

    opts, args = getopt.getopt(argv,"he:f:",["eemail=","ffunc="])
    print('test1.py -e <email> -f <func>') 
    #sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test1.py -e <email> -f <func>')
    #sys.exit()
        elif opt in ("-e", "--eemail"):
            email = arg
        elif opt in ("-f", "--ffunc"):
            func = arg
    print('searching for email', email) 
    print('function set to:  ', func)
    searchq(email,func)

#
if __name__ == "__main__":
   main(sys.argv[1:])