# Server Monitor Setup Instructions

## Prerequisites
- Python 3 installed on your server (Ubuntu recommended)
- `pip` installed
- `requests` library installed (`pip install requests`)
- Git installed (if cloning from GitHub)

## Installation Steps

1. **Clone the repository** (if using GitHub):
   ```
   git clone <your-repo-url>
   cd Server
   ```

2. **Install required Python packages:**
   ```
   pip install requests
   ```

3. **Run the setup script with sudo:**
   ```
   sudo python3 setup.py
   ```
   - Enter your Discord webhook URL when prompted.
   - Enter the username that should have passwordless `apt update`/`upgrade` (usually your current user).

4. **What the setup script does:**
   - Saves your Discord webhook URL to `config.py`.
   - Adds passwordless sudo rules for system updates.
   - Adds a cron job to run `auto_update.py` daily.
   - Adds a cron job to run `ping.py` daily at 3 AM (optional).
   - Adds a startup job so `ping.py` runs automatically on reboot.
   - Starts `ping.py` in the background so it runs 24/7, pinging once per hour.

## How It Works

- `ping.py` runs continuously, pinging the specified host every hour and sending the result to your Discord channel.
- `auto_update.py` runs daily to update and upgrade your system packages.
- Both scripts use the webhook URL you provide during setup.

## Stopping the Monitor

- To stop `ping.py`, find its process and kill it:
  ```
  pkill -f ping.py
  ```
- To remove the startup job or cron jobs, edit your crontab:
  ```
  crontab -e
  ```

## Notes

- Make sure to run the setup script as root (`sudo`) to allow it to write to `/etc/sudoers.d/`.
- Only grant passwordless sudo for trusted users.
- You can change the host to ping by editing the `host` variable in `ping.py`.

---
```// filepath: c:\Users\Donal\OneDrive\Documents\Python Projects\Server\ReadMe.txt

# Server Monitor Setup Instructions

## Prerequisites
- Python 3 installed on your server (Ubuntu recommended)
- `pip` installed
- `requests` library installed (`pip install requests`)
- Git installed (if cloning from GitHub)

## Installation Steps

1. **Clone the repository** (if using GitHub):
   ```
   git clone <your-repo-url>
   cd Server
   ```

2. **Install required Python packages:**
   ```
   pip install requests
   ```

3. **Run the setup script with sudo:**
   ```
   sudo python3 setup.py
   ```
   - Enter your Discord webhook URL when prompted.
   - Enter the username that should have passwordless `apt update`/`upgrade` (usually your current user).

4. **What the setup script does:**
   - Saves your Discord webhook URL to `config.py`.
   - Adds passwordless sudo rules for system updates.
   - Adds a cron job to run `auto_update.py` daily.
   - Adds a cron job to run `ping.py` daily at 3 AM (optional).
   - Adds a startup job so `ping.py` runs automatically on reboot.
   - Starts `ping.py` in the background so it runs 24/7, pinging once per hour.

## How It Works

- `ping.py` runs continuously, pinging the specified host every hour and sending the result to your Discord channel.
- `auto_update.py` runs daily to update and upgrade your system packages.
- Both scripts use the webhook URL you provide during setup.

## Stopping the Monitor

- To stop `ping.py`, find its process and kill it:
  ```
  pkill -f ping.py
  ```
- To remove the startup job or cron jobs, edit your crontab:
  ```
  crontab -e
  ```

## Notes

- Make sure to run the setup script as root (`sudo`) to allow it to write to `/etc/sudoers.d/`.
- Only grant passwordless sudo for trusted users.
- You can change the host to ping by editing the `host` variable in `ping.py`.

---