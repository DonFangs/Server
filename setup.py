import os
import getpass

def add_cron_job(script, time="0 2 * * *"):
    user = getpass.getuser()
    cron_line = f'{time} /usr/bin/python3 {os.path.abspath(script)}\n'
    # Read existing crontab
    stream = os.popen('crontab -l')
    existing = stream.read()
    if cron_line.strip() in existing:
        print(f"Cron job for {script} already exists.")
        return
    # Add new cron job
    new_cron = existing + cron_line
    with os.popen('crontab -', 'w') as cron:
        cron.write(new_cron)
    print(f"Added cron job: {cron_line.strip()}")

if __name__ == "__main__":
    add_cron_job("auto_update.py")
    add_cron_job("ping.py", time="0 3 * * *")  # Example: run ping.py at 3 AM