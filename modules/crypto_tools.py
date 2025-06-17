from cryptography.fernet import Fernet
import base64
import hashlib
from colorama import Fore, Style

def generate_key():
    return Fernet.generate_key().decode()

def encrypt_message(message, key):
    try:
        fernet = Fernet(key)
        encrypted = fernet.encrypt(message.encode())
        return encrypted.decode()
    except Exception as e:
        print(Fore.RED + f"[!] Encryption error: {str(e)}" + Style.RESET_ALL)
        return None

def decrypt_message(encrypted_message, key):
    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except Exception as e:
        print(Fore.RED + f"[!] Decryption error: {str(e)}" + Style.RESET_ALL)
        return None

def xor_encrypt(message, key):
    try:
        encrypted = []
        for i in range(len(message)):
            key_c = key[i % len(key)]
            encrypted.append(chr(ord(message[i]) ^ ord(key_c)))
        return base64.urlsafe_b64encode("".join(encrypted).encode()).decode()
    except Exception as e:
        print(Fore.RED + f"[!] XOR encryption error: {str(e)}" + Style.RESET_ALL)
        return None

def xor_decrypt(encrypted_message, key):
    try:
        encrypted_message = base64.urlsafe_b64decode(encrypted_message).decode()
        decrypted = []
        for i in range(len(encrypted_message)):
            key_c = key[i % len(key)]
            decrypted.append(chr(ord(encrypted_message[i]) ^ ord(key_c)))
        return "".join(decrypted)
    except Exception as e:
        print(Fore.RED + f"[!] XOR decryption error: {str(e)}" + Style.RESET_ALL)
        return None

def hash_message(message, algorithm='sha256'):
    try:
        if algorithm.lower() == 'sha256':
            return hashlib.sha256(message.encode()).hexdigest()
        elif algorithm.lower() == 'md5':
            return hashlib.md5(message.encode()).hexdigest()
        else:
            print(Fore.RED + "[!] Unsupported hash algorithm" + Style.RESET_ALL)
            return None
    except Exception as e:
        print(Fore.RED + f"[!] Hashing error: {str(e)}" + Style.RESET_ALL)
        return None

def crypto_menu():
    print(Fore.GREEN + "\n[+] Crypto Tools Menu:\n" + Style.RESET_ALL)
    print(Fore.CYAN + "  1. Generate AES Key")
    print("  2. Encrypt Message (AES)")
    print("  3. Decrypt Message (AES)")
    print("  4. XOR Encrypt")
    print("  5. XOR Decrypt")
    print("  6. Hash Message")
    print("  0. Back to Main Menu\n" + Style.RESET_ALL)
    return input(Fore.YELLOW + "[?] Select an option: " + Style.RESET_ALL)

def main():
    while True:
        print(Fore.YELLOW + "\n[+] Crypto Tools Module" + Style.RESET_ALL)
        choice = crypto_menu()
        
        try:
            if choice == "1":
                key = generate_key()
                print(Fore.GREEN + f"\n[+] Generated AES Key: {Fore.YELLOW}{key}{Style.RESET_ALL}")
            elif choice == "2":
                message = input(Fore.CYAN + "[?] Enter message to encrypt: " + Style.RESET_ALL)
                key = input(Fore.CYAN + "[?] Enter AES key: " + Style.RESET_ALL)
                encrypted = encrypt_message(message, key)
                if encrypted:
                    print(Fore.GREEN + f"\n[+] Encrypted message: {Fore.YELLOW}{encrypted}{Style.RESET_ALL}")
            elif choice == "3":
                message = input(Fore.CYAN + "[?] Enter message to decrypt: " + Style.RESET_ALL)
                key = input(Fore.CYAN + "[?] Enter AES key: " + Style.RESET_ALL)
                decrypted = decrypt_message(message, key)
                if decrypted:
                    print(Fore.GREEN + f"\n[+] Decrypted message: {Fore.YELLOW}{decrypted}{Style.RESET_ALL}")
            elif choice == "4":
                message = input(Fore.CYAN + "[?] Enter message to XOR encrypt: " + Style.RESET_ALL)
                key = input(Fore.CYAN + "[?] Enter XOR key: " + Style.RESET_ALL)
                encrypted = xor_encrypt(message, key)
                if encrypted:
                    print(Fore.GREEN + f"\n[+] XOR encrypted message: {Fore.YELLOW}{encrypted}{Style.RESET_ALL}")
            elif choice == "5":
                message = input(Fore.CYAN + "[?] Enter message to XOR decrypt: " + Style.RESET_ALL)
                key = input(Fore.CYAN + "[?] Enter XOR key: " + Style.RESET_ALL)
                decrypted = xor_decrypt(message, key)
                if decrypted:
                    print(Fore.GREEN + f"\n[+] XOR decrypted message: {Fore.YELLOW}{decrypted}{Style.RESET_ALL}")
            elif choice == "6":
                message = input(Fore.CYAN + "[?] Enter message to hash: " + Style.RESET_ALL)
                algorithm = input(Fore.CYAN + "[?] Enter algorithm (sha256/md5): " + Style.RESET_ALL).lower()
                hashed = hash_message(message, algorithm)
                if hashed:
                    print(Fore.GREEN + f"\n[+] {algorithm.upper()} hash: {Fore.YELLOW}{hashed}{Style.RESET_ALL}")
            elif choice == "0":
                return
            else:
                print(Fore.RED + "\n[!] Invalid choice!" + Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Operation cancelled by user!" + Style.RESET_ALL)
            return
        except Exception as e:
            print(Fore.RED + f"\n[!] Error: {str(e)}" + Style.RESET_ALL)
        
                        input(Fore.CYAN + "\n[?] Press Enter to continue..." + Style.RESET_ALL)
