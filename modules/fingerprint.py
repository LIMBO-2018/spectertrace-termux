import requests
import mmh3
import base64
import hashlib
from bs4 import BeautifulSoup
from colorama import Fore, Style

def get_favicon_hash(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        favicon_link = soup.find("link", rel="icon") or soup.find("link", rel="shortcut icon")
        
        if favicon_link:
            favicon_url = favicon_link['href']
            if not favicon_url.startswith(('http://', 'https://')):
                favicon_url = url + favicon_url if favicon_url.startswith('/') else url + '/' + favicon_url
            
            favicon_response = requests.get(favicon_url)
            favicon_data = favicon_response.content
            favicon_base64 = base64.encodebytes(favicon_data)
            return mmh3.hash(favicon_base64)
    except Exception:
        return None

def get_headers(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        response = requests.get(url)
        return dict(response.headers)
    except Exception:
        return None

def detect_tech(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        tech_detected = []
        response = requests.get(url)
        
        # Check for common headers
        headers = response.headers
        if 'X-Powered-By' in headers:
            tech_detected.append(headers['X-Powered-By'])
        if 'Server' in headers:
            tech_detected.append(headers['Server'])
        
        # Check HTML for common patterns
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check meta tags
        meta_tags = soup.find_all('meta')
        for tag in meta_tags:
            if 'generator' in tag.attrs:
                tech_detected.append(tag['generator'])
        
        # Check scripts
        scripts = soup.find_all('script')
        for script in scripts:
            if 'src' in script.attrs:
                src = script['src']
                if 'jquery' in src.lower():
                    tech_detected.append('jQuery')
                elif 'react' in src.lower():
                    tech_detected.append('React')
                elif 'angular' in src.lower():
                    tech_detected.append('Angular')
        
        return list(set(tech_detected)) if tech_detected else None
    except Exception:
        return None

def main():
    print(Fore.YELLOW + "\n[+] Technology Fingerprint Module" + Style.RESET_ALL)
    url = input(Fore.CYAN + "[?] Enter website URL: " + Style.RESET_ALL).strip()
    
    print(Fore.BLUE + "\n[*] Fingerprinting target..." + Style.RESET_ALL)
    
    # Get favicon hash
    favicon_hash = get_favicon_hash(url)
    if favicon_hash:
        print(Fore.GREEN + f"[+] Favicon hash: {Fore.YELLOW}{favicon_hash}{Style.RESET_ALL}")
    else:
        print(Fore.RED + "[-] Could not retrieve favicon hash" + Style.RESET_ALL)
    
    # Get headers
    headers = get_headers(url)
    if headers:
        print(Fore.GREEN + "\n[+] HTTP Headers:" + Style.RESET_ALL)
        for key, value in headers.items():
            print(Fore.CYAN + f"  {key}: " + Fore.YELLOW + f"{value}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n[-] Could not retrieve headers" + Style.RESET_ALL)
    
    # Detect technologies
    tech = detect_tech(url)
    if tech:
        print(Fore.GREEN + "\n[+] Detected Technologies:" + Style.RESET_ALL)
        for t in tech:
            print(Fore.YELLOW + f"  - {t}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n[-] Could not detect technologies" + Style.RESET_ALL)
    
    input(Fore.CYAN + "\n[?] Press Enter to return to main menu..." + Style.RESET_ALL)
