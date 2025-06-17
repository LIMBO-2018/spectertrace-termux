import requests
from colorama import Fore, Style

def search_cves(keyword):
    try:
        url = f"https://cve.circl.lu/api/search/{keyword}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception:
        return None

def print_cve_details(cve):
    print(Fore.GREEN + f"\n[+] CVE-{cve['id']}" + Style.RESET_ALL)
    print(Fore.CYAN + "  Published: " + Fore.YELLOW + cve.get('Published', 'N/A') + Style.RESET_ALL)
    print(Fore.CYAN + "  Modified: " + Fore.YELLOW + cve.get('Modified', 'N/A') + Style.RESET_ALL)
    print(Fore.CYAN + "  CVSS: " + Fore.YELLOW + str(cve.get('cvss', 'N/A')) + Style.RESET_ALL)
    print(Fore.CYAN + "  Summary: " + Fore.YELLOW + cve.get('summary', 'N/A') + Style.RESET_ALL)
    print(Fore.CYAN + "  References: " + Style.RESET_ALL)
    for ref in cve.get('references', []):
        print(Fore.YELLOW + f"    - {ref}" + Style.RESET_ALL)

def main():
    print(Fore.YELLOW + "\n[+] CVE Radar Module" + Style.RESET_ALL)
    keyword = input(Fore.CYAN + "[?] Enter product/software name or CVE ID: " + Style.RESET_ALL).strip()
    
    print(Fore.BLUE + "[*] Searching CVEs..." + Style.RESET_ALL)
    cves = search_cves(keyword)
    
    if cves:
        print(Fore.GREEN + f"\n[+] Found {len(cves)} CVEs:" + Style.RESET_ALL)
        for cve in cves:
            print_cve_details(cve)
    else:
        print(Fore.RED + "\n[-] No CVEs found" + Style.RESET_ALL)
    
    input(Fore.CYAN + "\n[?] Press Enter to return to main menu..." + Style.RESET_ALL)
