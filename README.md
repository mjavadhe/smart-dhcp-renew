# **Smart DHCP Renew Script**

## 🚀 Overview

This is a Python script that helps manage your DHCP lease renewal automatically. It monitors the lease obtained and lease expiry times from your system's DHCP settings and renews the IP address just before it expires, ensuring uninterrupted internet access. It even logs every action to a file for future reference!

The script is designed to handle dynamic IP address changes effectively, so you never need to worry about manually renewing your IP address when it’s time to reconnect.

## 🔧 Features

- **Automatic DHCP Renewal**: The script renews your IP address at the optimal time (before lease expiry).
- **Safety Margin**: It checks and renews the IP 5 minutes before the DHCP lease expires (T1).
- **Log File**: All actions are logged, including time of lease obtained, time of renewal, and new IP address assigned.
- **Cross-platform**: Works on Windows with Python installed.

## 🛠️ Requirements

- Python 3.x (Recommended Python 3.6+)
- Administrative privileges to run `ipconfig` commands.
- Windows OS (for now, tested on Windows 10/11).

## 📥 Installation

1. **Clone the repository or download the script**:
    ```bash
    git clone https://github.com/mjavadhe/smart-dhcp-renew.git
    cd smart-dhcp-renew
    ```

2. **Install necessary dependencies** (if any):
    You may need to install Python if you haven't already:
    - Download and install Python from [here](https://www.python.org/downloads/).

3. **Run the script**:
    Open your terminal/command prompt and execute the script using Python:
    ```bash
    python smart_dhcp_renew.py
    ```

    > **Note:** You may need administrative privileges to run the script due to the `ipconfig` command. Run your terminal as Administrator.

## 🔄 How it Works

1. **Checking DHCP Lease**: The script checks the `Lease Obtained` and `Lease Expiry` time from the system using the `ipconfig /all` command.
   
2. **Calculating Renewal Time**: The script calculates 50% of the lease time (T1), which is typically when the DHCP lease renewal occurs. It will then add a 5-minute safety margin before attempting to renew the IP.

3. **Renewing IP**: If the script detects that it's time for renewal, it automatically runs `ipconfig /renew` to request a new IP address.

4. **Logging**: Every action, including the time of renewal, IP address before and after, and when the next renewal will happen, is logged into a `.txt` log file.

## 📋 Log File Example

Here’s what the log file might look like after running the script:

[2025-04-20 17:11:17] 🚀 DHCP Smart Renew Script Started  
[2025-04-20 17:11:17] 📡 IP: 10.189.1.13  
[2025-04-20 17:11:17] 📅 Lease Obtained: 2025-04-20 16:26:59  
[2025-04-20 17:11:17] ⏳ Lease Expires : 2025-04-21 17:05:00  
[2025-04-20 17:11:17] 🔁 Next Renew at: 2025-04-21 17:00:00  
[2025-04-20 17:11:17] ⌛ Not time yet. Will check again in 60 seconds.  

## ⚙️ Configuration

- **Safety Margin**: By default, the script renews the IP 5 minutes before the lease expiry. This can be adjusted by changing the `SAFETY_MARGIN` in the script (e.g., `timedelta(minutes=5)`).

- **Log File**: Logs are written to `smart_dhcp_renew_log.txt` in the same directory. You can change the log file name or location if you want.

## 🤖 Automation

You can automate this script by setting it up to run in the background or use Windows Task Scheduler to run it periodically. Here’s how:

### Windows Task Scheduler Setup

1. Open **Task Scheduler**.
2. Click **Create Task**.
3. Set **Trigger** to run the script at your desired frequency (e.g., every 30 minutes).
4. Set **Action** to run the Python script (`python smart_dhcp_renew.py`).
5. Optionally, configure the task to run with **administrator privileges**.

## 🤝 Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request with bug fixes, improvements, or new features!

---

### 🙏 Acknowledgments

- **Python**: For providing an easy-to-use scripting environment for automation.
- **Windows OS**: For its built-in `ipconfig` tool to manage network settings.
- **GitHub**: For hosting and sharing this project with the community.

---

### 🔗 Links

- [GitHub Repository](https://github.com/mjavadhe/smart-dhcp-renew)
- [Python Official Website](https://www.python.org/)
- [My Website](https://mjavadhe.ir)
  
---

## 📝 Summary

The **Smart DHCP Renew Script** helps you manage DHCP lease renewals, ensuring that your IP address stays active without interruption. It automates the process of IP renewal, logging every action, and reducing the risk of losing your connection. Perfect for users who rely on a consistent IP address.
