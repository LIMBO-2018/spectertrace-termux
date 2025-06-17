#!/bin/bash
echo -e "\033[1;32m[+] Setting up SpecterTrace-Termux...\033[0m"

# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install -y python git openssl

# Install Python packages
pip install --upgrade pip
pip install requests colorama scapy pdfkit python-whois beautifulsoup4 cryptography

# Clone and install wkhtmltopdf for PDF reports
if [ ! -f "/data/data/com.termux/files/usr/bin/wkhtmltopdf" ]; then
    echo -e "\033[1;33m[!] Installing wkhtmltopdf for PDF reports...\033[0m"
    wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_arm64.deb
    dpkg -x wkhtmltox_0.12.6-1.bionic_arm64.deb wkhtmltox
    mv wkhtmltox/usr/local/bin/* /data/data/com.termux/files/usr/bin/
    mv wkhtmltox/usr/local/include/* /data/data/com.termux/files/usr/include/
    rm -rf wkhtmltox*
fi

# Create data directory
mkdir -p data

echo -e "\033[1;32m[+] Setup complete! Run: python main.py\033[0m"
