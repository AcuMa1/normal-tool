import requests
import threading

url = "https://backend.kibomodz.online/api/users/login"

def send_request():
    try:
        response = requests.get(url)
        print(f"Request sent to {url} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def stress_test(num_requests):
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

num_requests = 9000

stress_test(num_requests)
