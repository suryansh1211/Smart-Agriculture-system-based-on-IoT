import time
import sys
import ibmiotf.application #To install pip install ibmiotf
import ibmiotf.device

#Device details
organization = "gmxmw0"
deviceType = "Motor"
deviceId = "motor123"
authMethod = "token"
authToken = "motor123"

#Callback function
def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data)        
    if cmd.data['command']=='motoron':
        print("MOTOR ON")
    elif cmd.data['command']=='motoroff':
        print("MOTOR OFF")
    if cmd.command == "setInterval":
        if 'interval' not in cmd.data:
            print("Error - command is missing required information: 'interval'")
        else:
            interval = cmd.data['interval']
    elif cmd.command == "print":
        if 'message' not in cmd.data:
            print("Error - command is missing required information: 'message'")
        else:
            output=cmd.data['message']
            print(output)

try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
    
except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()
    
#Connect the device and application from cloud
deviceCli.connect()

while True:
    
    deviceCli.commandCallback = myCommandCallback
    
#Disconnect the device and application from cloud
deviceCli.disconnect()
