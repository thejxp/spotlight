
from spotlight import *


def parseID(url, apps):
    ID = ""
    i = len(url)-1
    while(url[i] != "/"):
        ID = url[i] + ID
        i = i - 1
   
    text = apps.api.get_status(ID)
    return (text.text) 


machine = MachineSpotlight()
machine.manage_data()
machine.build_classifier()
application = Spotlight()
URL = raw_input("Enter the URL of the tweet you'd like to analyze: \n\n\n")
ID = parseID(URL, application)
a = machine.update_classifier(URL) # answer
machine.write_data("data.py", "Alisha")

print a
print ("\n\n\n\n\n")








