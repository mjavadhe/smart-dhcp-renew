import subprocess
import time
from datetime import datetime, timedelta
import re

LOG_FILE = "smart_dhcp_renew_log.txt"
CHECK_INTERVAL_SECONDS = 60  # بررسی هر 1 دقیقه
SAFETY_MARGIN = timedelta(minutes=5)  # بازه اطمینانی ۵ دقیقه قبل از T1

def get_lease_info():
    result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, shell=True)
    output = result.stdout

    lease_obtained_match = re.search(r"Lease Obtained[.\s:]+(.+)", output)
    lease_expires_match = re.search(r"Lease Expires[.\s:]+(.+)", output)
    ip_match = re.search(r"IPv4 Address[.\s:]+([\d\.]+)", output)

    if lease_obtained_match and lease_expires_match and ip_match:
        lease_obtained_str = lease_obtained_match.group(1).strip()
        lease_expires_str = lease_expires_match.group(1).strip()
        ip_address = ip_match.group(1).strip()

        lease_obtained = datetime.strptime(lease_obtained_str, "%A, %B %d, %Y %I:%M:%S %p")
        lease_expires = datetime.strptime(lease_expires_str, "%A, %B %d, %Y %I:%M:%S %p")
        return lease_obtained, lease_expires, ip_address
    else:
        return None, None, None

def renew_ip():
    subprocess.run(["ipconfig", "/renew"], capture_output=True, text=True, shell=True)

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {msg}\n")
    print(f"[{now}] {msg}")

def main():
    log("🚀 DHCP Smart Renew Script Started")
    while True:
        lease_obtained, lease_expires, ip = get_lease_info()
        now = datetime.now()

        if lease_obtained and lease_expires:
            lease_duration = lease_expires - lease_obtained
            renew_time = lease_obtained + lease_duration * 0.5  # T1 = 50% of lease

            log(f"📡 IP: {ip}")
            log(f"📅 Lease Obtained: {lease_obtained}")
            log(f"⏳ Lease Expires : {lease_expires}")
            log(f"🔁 Next Renew at: {renew_time}")

            # Renew early with safety margin
            if now >= (renew_time - SAFETY_MARGIN):
                log("⚠️ Time to RENEW! Renewing IP...")
                renew_ip()
                time.sleep(5)  # صبر کنیم DHCP اطلاعات جدید بده
                lease_obtained, lease_expires, ip = get_lease_info()
                log("✅ Renew Done.")
                log(f"📅 New Lease Obtained: {lease_obtained}")
                log(f"⏳ New Lease Expires : {lease_expires}")
                log(f"📡 New IP: {ip}")
            else:
                log(f"⌛ Not time yet. Will check again in {CHECK_INTERVAL_SECONDS} seconds.")

        else:
            log("❌ Couldn't fetch lease info.")

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
