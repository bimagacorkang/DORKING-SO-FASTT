#thanks for qxyura404
#remake by bimatzy999

from googlesearch import search
from colorama import Fore, Style, init
import time
import sys

init(autoreset=True)

def banner():
    print(Fore.CYAN + r"""
██████╗ ██╗███╗   ███╗ █████╗ ████████╗███████╗██╗   ██╗999
██╔══██╗██║████╗ ████║██╔══██╗╚══██╔══╝╚══███╔╝╚██╗ ██╔╝
██████╔╝██║██╔████╔██║███████║   ██║     ███╔╝  ╚████╔╝ 
██╔══██╗██║██║╚██╔╝██║██╔══██║   ██║    ███╔╝    ╚██╔╝  
██████╔╝██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗   ██║   
╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   
""")
    print(Fore.YELLOW + "="*60)
    print(Fore.GREEN + "Find Dorking So Fastt🥵 | v1.9")
    print(Fore.GREEN + "Create  by BimaTzy999")
    print(Fore.GREEN + "Thanks for Qxyura404")
    print(Fore.YELLOW + "="*60 + Style.RESET_ALL)

def animasi_loading():
    chars = "/—\\|" 
    for _ in range(5):
        for char in chars:
            sys.stdout.write(Fore.YELLOW + '\r' + '[+] Memuat ' + char)
            sys.stdout.flush()
            time.sleep(0.1)

def main():
    banner()
    
    # Input dork dari pengguna
    dork = input(Fore.MAGENTA + "\n[?] Masukkan dork Anda (contoh: inurl:/admin/login site:co.id): " + Style.RESET_ALL)
    max_hasil = int(input(Fore.MAGENTA + "[?] Masukkan jumlah maksimal hasil (default 30): " + Style.RESET_ALL) or 30)
    delay = float(input(Fore.MAGENTA + "[?] Masukkan jeda antara permintaan (detik, min 2): " + Style.RESET_ALL) or 2)
    
    if delay < 2:
        print(Fore.RED + "[!] Jeda terlalu singkat, diatur ke minimum 2 detik" + Style.RESET_ALL)
        delay = 2
    
    print(Fore.BLUE + "\n[+] Memulai pencarian dengan dork: " + Fore.YELLOW + dork)
    print(Fore.BLUE + "[+] Jumlah maksimal hasil: " + Fore.YELLOW + str(max_hasil))
    print(Fore.BLUE + "[+] Jeda: " + Fore.YELLOW + str(delay) + "s")
    
    animasi_loading()
    print("\n" + Fore.RED + "[!] Pemindaian sedang berlangsung..." + Style.RESET_ALL)
    
    try:
        waktu_mulai = time.time()
        counter = 1
        
        print(Fore.WHITE + "-"*80)
        for result in search(dork, num_results=max_hasil, sleep_interval=delay):
            print(Fore.GREEN + f"[{counter}] " + Fore.CYAN + result)
            counter += 1
        print(Fore.WHITE + "-"*80)
        
        waktu_selesai = time.time() - waktu_mulai
        print(Fore.YELLOW + f"\n[+] Pemindaian selesai dalam {waktu_selesai:.2f} detik")
        print(Fore.YELLOW + f"[+] Total hasil ditemukan: {counter-1}")
        print(Fore.CYAN + "\n[+] Ikuti untuk tools lainnya!" + Style.RESET_ALL)
        
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}")
    finally:
        print(Fore.YELLOW + "\n[+] Sesi berakhir" + Style.RESET_ALL)
        print(Fore.YELLOW + "\n[+] Jangan Lupa Follow ig:BIOMI.VILLAIN" + Style. RESET_ALL) 

if __name__ == "__main__":
    main()