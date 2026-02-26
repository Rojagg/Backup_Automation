import json
from netmiko import ConnectHandler
from datetime import datetime
import re

devicesFile = "../devices.json"


def connectDevice(device):
    connection = ConnectHandler(**device)
    connection.enable()
    output = connection.send_command("show running")
    connection.disconnect()
    return output

def parseDevices():
    with open(devicesFile, 'r') as f:
        devices=json.load(f)
    
    return devices
    
def saveConfiguration(devices):
    for device in devices:
        output = connectDevice(devices[device])
        filePath=f"{device}_"

#temp = parseDevices()
#saveConfiguration(temp)
def returnDate():
    date = str(datetime.now())
    dateFile = date.split()[0]
    dateFile = dateFile.replace('-', '_')
    hourFile = re.search(r"\d{1,2}:\d{1,2}", date).group()

    return dateFile + "_" + hourFile

print(returnDate())