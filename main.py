#!/usr/bin/env python3
import os
import sys
import time
from colorama import Fore, Style, init
from modules import recon, leaknet, port_scanner, fingerprint, cve_radar, exploit_search, pdf_reporter, crypto_tools

# Initialize colorama
init()

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    print(Fore.RED + r"""
     _____                     _       _____             _      
    / ____|                   | |     |  __ \           | |     
   | (___  _ __   ___  ___ ___| |_ ___| |__) |___  _ __ | |_ ___
    \___ \| '_ \ / _ \/ __/ __| __/ _ \  _  // _ \| '_ \| __/ __|
    ____) | |_) |  __/\__ \__ \ ||  __/ | \ \ (_) | | | | |_\__ \
   |_____/| .__/ \___||___/___/\__\___|_|  \_\___/|_| |_|\__|___/
          | |                                                    
          |_|            Termux Edition v1.0
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "          Elite Cyber Reconnaissance Toolkit" + Style.RESET_ALL)
    print(Fore.CYAN + "          -----------------------------------" + Style.RESET_ALL)

def main_menu():
    while True:
        print_banner()
        print(Fore.GREEN + "\n[+] Main Menu:\n" + Style.RESET_ALL)
        print(Fore.CYAN + "  1. Passive Reconnaissance")
        print("  2. Breach Data Checker")
        print("  3. Port Scanner")
        print("  4. Technology Fingerprint")
        print("  5. CVE Radar")
        print("  6. Exploit Search")
        print("  7. Crypto Tools")
        print("  8. Generate PDF Report")
        print("  0. Exit\n" + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "[?] Select an option: " + Style.RESET_ALL)

        try:
            if choice == "1":
                recon.main()
            elif choice == "2":
                leaknet.main()
            elif choice == "3":
                port_scanner.main()
            elif choice == "4":
                fingerprint.main()
            elif choice == "5":
                cve_radar.main()
            elif choice == "6":
                exploit_search.main()
            elif choice == "7":
                crypto_tools.main()
            elif choice == "8":
                pdf_reporter.main()
            elif choice == "0":
                print(Fore.RED + "\n[!] Exiting SpecterTrace..." + Style.RESET_ALL)
                sys.exit(0)
            else:
                print(Fore.RED + "\n[!] Invalid choice!" + Style.RESET_ALL)
                time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Operation cancelled by user!" + Style.RESET_ALL)
            time.sleep(1)
        except Exception as e:
            print(Fore.RED + f"\n[!] Error: {str(e)}" + Style.RESET_ALL)
            time.sleep(2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Exiting SpecterTrace..." + Style.RESET_ALL)
        sys.exit(0)
