import time, json

def write(seconds, minutes, hours):
    file = "logs.json"
    data = {}
    data["seconds"] = seconds
    data["minutes"] = minutes
    data["hours"] = hours
    with open(file, "w") as fp:
        json.dump(data, fp)

while True:
    time.sleep(1)

    with open("logs.json") as file:
        file_data = json.load(file)
        seconds = file_data['seconds']
        minutes = file_data['minutes']
        hours = file_data['hours']
    
    if seconds == 59:
        if minutes == 59:
            write(0, 0, hours+1)
        else:
            write(0, minutes+1, hours)
    else:
        write(seconds+1, minutes, hours)
