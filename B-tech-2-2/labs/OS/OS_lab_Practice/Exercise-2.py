import threading 
BUFFER_SIZE = 5
NUM_ITEMS = 10

buffer = []
mutex = threading.Lock()
items_available = threading.Semaphore(0)
spaces_available = threading.Semaphore(BUFFER_SIZE)

def producer():
    for i in range(NUM_ITEMS):
        item = f"Item {i} from producer"
        spaces_available.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Producer produced {item}")
        mutex.release()
        items_available.release()

def consumer():
    for i in range(NUM_ITEMS):
        items_available.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumer consumed {item}")
        mutex.release()
        spaces_available.release()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Producer and consumer have finished.")
