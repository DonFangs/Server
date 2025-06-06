import os
import time
import requests
from config import DISCORD_WEBHOOK_URL  # Import from config.py

def send_discord_message(message):
    data = {"content": message}
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Failed to send Discord message: {e}")

def ping(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        send_discord_message(f":white_check_mark: {host} is online!")
        return "Ping successful!"
    else:
        send_discord_message(f":x: {host} is offline!")
        return "Ping failed!"

if __name__ == "__main__":
    host = "google.com"  # Change this to your desired host
    while True:
        print(ping(host))
        time.sleep(3600)  # Wait for 1 hour (3600 seconds)