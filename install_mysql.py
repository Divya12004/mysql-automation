#!/usr/bin/env python3

import os
import sys
import subprocess
from dotenv import load_dotenv

# Load .env file

load_dotenv()



MYSQL_PACKAGE = os.getenv("MYSQL_PACKAGE", "mysql-server")
MYSQL_SERVICE = os.getenv("MYSQL_SERVICE", "mysql")


def run_command(command):
    print(f"\n$ {' '.join(command)}")
    subprocess.run(command, check=True)


def main():

    print("======================================")
    print("     MySQL Installation Script")
    print("======================================")

    # Check root permission
    if os.geteuid() != 0:
        print("Please run this script using sudo.")
        sys.exit(1)

    # Step 1
    print("\n[1/5] Updating packages...")
    run_command(["apt", "update", "-y"])

    # Step 2
    print("\n[2/5] Installing MySQL...")
    run_command(["apt", "install", MYSQL_PACKAGE, "-y"])

    # Step 3
    print("\n[3/5] Starting MySQL...")
    run_command(["systemctl", "start", MYSQL_SERVICE])

    # Step 4
    print("\n[4/5] Enabling MySQL...")
    run_command(["systemctl", "enable", MYSQL_SERVICE])

    # Step 5
    print("\n[5/5] Checking MySQL...")

    result = subprocess.run(
        ["mysql", "--version"],
        capture_output=True,
        text=True,
        check=True
    )

    print(result.stdout)

    # Check service
    status = subprocess.run(
        ["systemctl", "is-active", "--quiet", MYSQL_SERVICE]
    )

    if status.returncode == 0:
        print("======================================")
        print(" MySQL Installed Successfully!")
        print("======================================")
    else:
        print("MySQL installation failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
