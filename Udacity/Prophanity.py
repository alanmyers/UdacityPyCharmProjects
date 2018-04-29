import requests

file_loc = r"c:\tmp\Udacity\quotes.txt"

def read_text():
    quotes = open(file_loc)
    contents_of_file = quotes.read()
    quotes.close()

    #print(contents_of_file)
    #print ("boolean: ", bool(5 == 5))
    return(contents_of_file)

def check_profanity(text_to_check):
    myUrl = "http://www.wdylike.appspot.com/"
    results = requests.get(myUrl,
                           params={'q':text_to_check})
    print(results._content)
    retVal = results.text
    print("retVal: ", retVal)
    return(bool("true" in retVal))

    #print("Opening: [", myUrl, "]")
    #connection = urllib.request.urlopen(myUrl)
    #output = connection.read()
    #print(output)
    #connection.close()

some_txt = read_text()
if  (check_profanity(some_txt)):
    print("Profanity Found!")
else:
    print("this document is clean!")

