#!/bin/bash
echo -e "\033[1;32m[+] Setting up SpecterTrace-Termux...\033[0m"

# Update packages
pkg update -y && pkg upgrade -y

# Install essential dependencies
pkg install -y python git openssl libffi

# Install Python packages with fallbacks
pip install --upgrade pip wheel
pip install requests colorama scapy python-whois beautifulsoup4 mmh3 pycryptodome

# Install PDFKit alternatives if wkhtmltopdf fails
if ! command -v wkhtmltopdf &> /dev/null; then
    echo -e "\033[1;33m[!] Using HTML reports instead of PDF\033[0m"
    sed -i "s/import pdfkit//g" modules/pdf_reporter.py
    sed -i "s/pdfkit.from_string/open('report.html','w').write/g" modules/pdf_reporter.py
fi

# Create data directory
mkdir -p data

echo -e "\033[1;32m[+] Setup complete! Run: python main.py\033[0m"
