import os

def ping(host):
    response = os.system(f"ping -c 4 {host}")
    return "Ping successful!" if response == 0 else "Ping failed!"

if __name__ == "__main__":
    print(ping("google.com"))