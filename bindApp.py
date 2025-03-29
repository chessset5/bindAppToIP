import os
import subprocess

import psutil

APP_FOLDER: str = [r"C:\Program Files (x86)\Epic Games"]

# Get network interface details
interfaces = psutil.net_if_addrs()

adapter: str = "Wi-Fi ax"
if adapter in interfaces:
    # check if Wi-Fi is available
    addresses = interfaces[adapter]

    address: str = ""
    for addr in addresses:
        if addr.family.name == psutil.AF_LINK:
            address = addr.address
            break

    if address:
        exes: list[str] = list()
        for app in APP_FOLDER:
            for root, dirs, files in os.walk(APP_FOLDER):
                for f in files:
                    if f.endswith(r".exe"):
                        exes.append(os.path.join(root, f))
            for e in exes:
                # subprocess.run(["ForceBindIP64.exe", "-i", address, e])
                subprocess.run(["ForceBindIP64.exe", address, e])
