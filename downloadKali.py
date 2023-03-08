import requests
import os

def download_kali():
    url = "https://cdimage.kali.org/kali-2022.4/kali-linux-2022.4-installer-amd64.iso"
    filename = os.path.join(os.path.expanduser("~"), "Downloads", "kali.iso")

    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

    print("Downloaded Kali successfully!")
    return
