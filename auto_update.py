import os

def auto_update():
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("git pull")

if __name__ == "__main__":
    auto_update()