import requests
import socket
import whois
from colorama import Fore, Style
import time

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719")
        return response.json()
    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)
        return None

def get_whois(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)
        return None

def print_recon_data(data, title):
    print(Fore.GREEN + f"\n[+] {title}:" + Style.RESET_ALL)
    for key, value in data.items():
        print(Fore.CYAN + f"  {key}: " + Fore.YELLOW + f"{value}" + Style.RESET_ALL)

def main():
    print(Fore.YELLOW + "\n[+] Passive Reconnaissance Module" + Style.RESET_ALL)
    target = input(Fore.CYAN + "[?] Enter IP or domain: " + Style.RESET_ALL).strip()
    
    try:
        # Check if input is IP or domain
        try:
            socket.inet_aton(target)
            is_ip = True
        except socket.error:
            is_ip = False

        if is_ip:
            print(Fore.BLUE + "[*] Gathering IP information..." + Style.RESET_ALL)
            ip_info = get_ip_info(target)
            if ip_info:
                print_recon_data(ip_info, "IP Information")
        else:
            print(Fore.BLUE + "[*] Performing WHOIS lookup..." + Style.RESET_ALL)
            whois_info = get_whois(target)
            if whois_info:
                print_recon_data(whois_info, "WHOIS Information")

            print(Fore.BLUE + "\n[*] Resolving DNS..." + Style.RESET_ALL)
            try:
                ip = socket.gethostbyname(target)
                print(Fore.CYAN + "  IP Address: " + Fore.YELLOW + ip + Style.RESET_ALL)
                print(Fore.BLUE + "[*] Gathering IP information..." + Style.RESET_ALL)
                ip_info = get_ip_info(ip)
                if ip_info:
                    print_recon_data(ip_info, "IP Information")
            except Exception as e:
                print(Fore.RED + f"[!] DNS Resolution Error: {str(e)}" + Style.RESET_ALL)

    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Operation cancelled by user!" + Style.RESET_ALL)
        return
    except Exception as e:
        print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)

    input(Fore.CYAN + "\n[?] Press Enter to return to main menu..." + Style.RESET_ALL)
