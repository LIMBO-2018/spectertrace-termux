import socket
from colorama import Fore, Style
import time

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def get_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except Exception:
        return None

def main():
    print(Fore.YELLOW + "\n[+] Port Scanner Module" + Style.RESET_ALL)
    target = input(Fore.CYAN + "[?] Enter target IP: " + Style.RESET_ALL).strip()
    start_port = int(input(Fore.CYAN + "[?] Enter start port: " + Style.RESET_ALL))
    end_port = int(input(Fore.CYAN + "[?] Enter end port: " + Style.RESET_ALL))
    
    print(Fore.BLUE + f"\n[*] Scanning {target} (ports {start_port}-{end_port})..." + Style.RESET_ALL)
    
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            banner = get_banner(target, port)
            status = Fore.GREEN + f"[+] Port {port} is open" + Style.RESET_ALL
            if banner:
                status += f" - Banner: {Fore.YELLOW}{banner}{Style.RESET_ALL}"
            print(status)
            open_ports.append((port, banner))
        else:
            print(Fore.RED + f"[-] Port {port} is closed" + Style.RESET_ALL, end='\r')
    
    if open_ports:
        print(Fore.GREEN + "\n[+] Open ports summary:" + Style.RESET_ALL)
        for port, banner in open_ports:
            print(Fore.CYAN + f"  Port {port}: " + Fore.YELLOW + f"{banner if banner else 'No banner'}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n[-] No open ports found" + Style.RESET_ALL)
    
    input(Fore.CYAN + "\n[?] Press Enter to return to main menu..." + Style.RESET_ALL)
