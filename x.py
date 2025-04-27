import requests
import threading
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://backend.kibomodz.online/"

def send_request():
    try:
        response = requests.get(url, verify=False)
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

num_requests = 1000

stress_test(num_requests)
