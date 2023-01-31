import requests
import time

print("Created By Frann#8446")


token = input("Token: ")
channel = int(input("ID of channel: "))
message = input("Message to spam: ")
delay = int(input("Delay: "))

def sendMessages(token, channel, message, delay):
    data = {"content": message}
    header = {"authorization": token}
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel)

    while True:
            r = requests.post(url, data=data, headers=header)
            print(r.status_code)
            if r.status_code == 200:
                time.sleep(delay)
            else:
                print("Something went wrong")
                break

if __name__ == "__main__":
    sendMessages(token, channel, message, delay)

