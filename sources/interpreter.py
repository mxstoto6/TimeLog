import json, os, time

def printd():
    with open("logs.json") as file:
        file_data = json.load(file)
        seconds = str(file_data['seconds'])
        minutes = str(file_data['minutes'])
        hours = str(file_data['hours'])

    os.system('cls')

    print("Here is the total amount of time your PC has been running\nfrom the installation of this script:\n\n")
    print("    " + hours + "hours")
    print("    " + minutes + "minutes")
    print("    " + seconds + "seconds")

printd()

while True:
    printd()
    time.sleep(1)
