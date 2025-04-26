from scapy.all import *
import random
import time
import threading

def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_port():
    return random.randint(1024, 65535)

def send_syn_packet(target_ip, target_port):
    ip = IP(dst=target_ip)
    syn = TCP(dport=target_port, flags="S", seq=random.randint(1000, 9000))
    packet = ip/syn
    send(packet, verbose=False)

def load_test():
    target_ip = generate_random_ip()
    target_port = generate_random_port()
    print(f"بدأ الاختبار: إرسال حزم إلى {target_ip} على المنفذ {target_port}")
    
    for i in range(100):
        send_syn_packet(target_ip, target_port)
        time.sleep(0.1)
    
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
