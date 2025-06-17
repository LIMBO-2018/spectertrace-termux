import requests
import hashlib
from colorama import Fore, Style

def check_breach(email):
    try:
        # Hash the email using SHA-1 (required by HIBP API)
        sha1_hash = hashlib.sha1(email.encode('utf-8')).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        # Make request to HIBP API
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        
        if response.status_code == 200:
            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == suffix:
                    return int(count)
            return 0
        else:
            print(Fore.RED + f"[!] API Error: {response.status_code}" + Style.RESET_ALL)
            return None
    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)
        return None

def main():
    print(Fore.YELLOW + "\n[+] Breach Data Checker Module" + Style.RESET_ALL)
    email = input(Fore.CYAN + "[?] Enter email to check: " + Style.RESET_ALL).strip()
    
    print(Fore.BLUE + "[*] Checking breach databases..." + Style.RESET_ALL)
    breach_count = check_breach(email)
    
    if breach_count is not None:
        if breach_count > 0:
            print(Fore.RED + f"\n[!] Email found in {breach_count} breaches!" + Style.RESET_ALL)
            print(Fore.YELLOW + "[!] Recommendation: Change passwords immediately!" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "\n[+] No breaches found for this email." + Style.RESET_ALL)
    
    input(Fore.CYAN + "\n[?] Press Enter to return to main menu..." + Style.RESET_ALL)
