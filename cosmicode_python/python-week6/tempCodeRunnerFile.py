import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"[Numbers Thread] {i}")
        time.sleep(1)

def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"[Letters Thread] {ch}")
        time.sleep(1)

def delay_task():
    print("[Delay Thread] Starting 3-second delay...")
    time.sleep(3)
    print("[Delay Thread] Finished delay!")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=delay_task)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads have completed.")
