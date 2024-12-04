#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def check_vulnerabilities(url):
    try:
        # Codsi u diraya bogga
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Qalad: Bogga ma furmo. Status-ka: {response.status_code}")
            return
        
        # Soo saarista content-ka bogga
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"\nFalanqeyn ee bogga: {url}\n")

        # Baaritaanka Links aan HTTPS lahayn
        links = soup.find_all('a', href=True)
        print("Links aan HTTPS lahayn:")
        for link in links:
            if not link['href'].startswith('https://'):
                print(f"- {link['href']}")

        # Baaritaanka foomamka
        forms = soup.find_all('form')
        print(f"\nFoomamka la helay: {len(forms)}")
        for form in forms:
            action = form.get('action', 'Aan la cayimin')
            if not action.startswith('https://'):
                print(f"- Foom aan HTTPS lahayn: {action}")

    except requests.RequestException as e:
        print(f"Qalad: {e}")

def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        ip = data.get('ip', 'Lama helin')
        location = f"{data.get('city', 'Lama helin')}, {data.get('region', 'Lama helin')}, {data.get('country', 'Lama helin')}"
        loc_details = data.get('loc', 'Lama helin')
        
        print(f"\nIP Address: {ip}")
        print(f"Goobta: {location}")
        print(f"Faahfaahinta Goobta: {loc_details}")

    except requests.RequestException as e:
        print(f"Qalad: {e}")

if __name__ == "__main__":
    print("""
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔═BLACK1446█╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

     ▂▃▄▅▆▇▓▒░ Coded By CyberAK ░▒▓▇▆▅▄▃▂
   ]──────────────────────────────────────[

""")
    print("1. Baar URL Jilicsan (Insecure)")
    print("2. Hel IP iyo Xogta Goobta")
    print("Dooro mid (1 ama 2):")

    choice = input("> ")
    if choice == '1':
        url = input("Geli URL-ga bogga aad rabto in aad baaris ku sameyso: ")
        check_vulnerabilities(url)
    elif choice == '2':
        get_ip_info()
    else:
        print("Xulasho khaldan, fadlan isku day mar kale.")
