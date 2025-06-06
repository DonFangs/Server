import os
import getpass
import subprocess

def write_config():
    webhook_url = input("Enter your Discord webhook URL: ").strip()
    with open("config.py", "w") as f:
        f.write(f'DISCORD_WEBHOOK_URL = "{webhook_url}"\n')
    print("Saved webhook URL to config.py.")

def add_passwordless_sudo():
    username = input("Enter the username to grant passwordless apt update/upgrade: ").strip()
    sudoers_line = f'{username} ALL=(ALL) NOPASSWD: /usr/bin/apt update, /usr/bin/apt upgrade\n'
    sudoers_file = f"/etc/sudoers.d/{username}_apt"
    try:
        with open(sudoers_file, "w") as f:
            f.write(sudoers_line)
        os.chmod(sudoers_file, 0o440)
        print(f"Added passwordless sudo rule for {username} in {sudoers_file}")
    except PermissionError:
        print("Permission denied. Please run this script with sudo to modify sudoers.")

def add_cron_job(script, time="0 2 * * *"):
    cron_line = f'{time} /usr/bin/python3 {os.path.abspath(script)}\n'
    stream = os.popen('crontab -l')
    existing = stream.read()
    if cron_line.strip() in existing:
        print(f"Cron job for {script} already exists.")
        return
    new_cron = existing + cron_line
    with os.popen('crontab -', 'w') as cron:
        cron.write(new_cron)
    print(f"Added cron job: {cron_line.strip()}")

def add_startup_job(script):
    cron_line = f'@reboot /usr/bin/python3 {os.path.abspath(script)}\n'
    stream = os.popen('crontab -l')
    existing = stream.read()
    if cron_line.strip() in existing:
        print(f"Startup job for {script} already exists.")
        return
    new_cron = existing + cron_line
    with os.popen('crontab -', 'w') as cron:
        cron.write(new_cron)
    print(f"Added startup job: {cron_line.strip()}")

def start_ping_background():
    script_path = os.path.abspath("ping.py")
    subprocess.Popen(["nohup", "python3", script_path, "&"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Started ping.py in the background.")

if __name__ == "__main__":
    write_config()
    add_passwordless_sudo()
    add_cron_job("auto_update.py")
    add_cron_job("ping.py", time="0 3 * * *")  # Optional: daily run
    add_startup_job("ping.py")  # Auto-start on reboot
    start_ping_background()     # Start now