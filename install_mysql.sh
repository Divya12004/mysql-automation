#!/bin/bash

set -e

echo "======================================"
echo "     MySQL Installation Script"
echo "======================================"

if [ "$EUID" -ne 0 ]; then
    echo "Please run this script using sudo."
    exit 1
fi

echo "[1/5] Updating packages..."
apt update -y

echo "[2/5] Installing MySQL..."
apt install mysql-server -y

echo "[3/5] Starting MySQL..."
systemctl start mysql

echo "[4/5] Enabling MySQL..."
systemctl enable mysql

echo "[5/5] Checking MySQL..."
mysql --version

if systemctl is-active --quiet mysql; then
    echo "======================================"
    echo " MySQL Installed Successfully!"
    echo "======================================"
else
    echo "MySQL installation failed."
    exit 1
fi
