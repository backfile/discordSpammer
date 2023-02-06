import requests
import time

print("Created By Frann#8446")

channels = []

token = input("Token: ")
message = input("Message to spam: ")
delay = int(input("Delay: "))
rta = int(input("How many channels? "))

if rta >= 1:
    cont = 0
    while rta > cont:
        channel = int(input("ID of channel: "))
        channels.append(channel)
        cont += 1
else:
    print("invalid number")
    
    
def sendMessages(token, channels, message, delay):
    data = {"content": message}
    header = {"authorization": token}
    while True:
        for channel in channels:
            url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel)
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
                print("success")
                time.sleep(4)
                if channel == channels[rta - 1]:
                    time.sleep(delay)
            else:
                print("Something went wrong")
                break

if __name__ == "__main__":
    sendMessages(token, channels, message, delay)
