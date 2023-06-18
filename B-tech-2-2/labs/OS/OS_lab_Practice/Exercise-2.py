# # #Bounded-Buffer problem
# # import threading 
# # BUFFER_SIZE = 5
# # NUM_ITEMS = 10
# # 
# # buffer = []
# # mutex = threading.Lock()
# # items_available = threading.Semaphore(0)
# # spaces_available = threading.Semaphore(BUFFER_SIZE)
# # 
# # def producer():
# #     for i in range(NUM_ITEMS):
# #         item = f"Item {i} from producer"
# #         spaces_available.acquire()
# #         mutex.acquire()
# #         buffer.append(item)
# #         print(f"Producer produced {item}")
# #         mutex.release()
# #         items_available.release()
# # 
# # def consumer():
# #     for i in range(NUM_ITEMS):
# #         items_available.acquire()
# #         mutex.acquire()
# #         item = buffer.pop(0)
# #         print(f"Consumer consumed {item}")
# #         mutex.release()
# #         spaces_available.release()
# # 
# # producer_thread = threading.Thread(target=producer)
# # consumer_thread = threading.Thread(target=consumer)
# # 
# # producer_thread.start()
# # consumer_thread.start()
# # 
# # producer_thread.join()
# # consumer_thread.join()
# # 
# # print("Producer and consumer have finished.")
# import threading
# 
# readers = 0
# writers = 0
# read_mutex = threading.Lock()
# write_mutex = threading.Lock()
# read_try = threading.Semaphore(1)
# resource = threading.Semaphore(1)
# 
# def reader():
#     global readers
#     read_try.acquire()
#     read_mutex.acquire()
#     readers += 1
#     if readers == 1:
#         resource.acquire()
#     read_mutex.release()
#     read_try.release()
# 
#     # Read from the shared resource
#     print("Reader is reading the resource")
# 
#     read_mutex.acquire()
#     readers -= 1
#     if readers == 0:
#         resource.release()
#     read_mutex.release()
# 
# def writer():
#     global writers
#     write_mutex.acquire()
#     writers += 1
#     if writers == 1:
#         read_try.acquire()
#     write_mutex.release()
# 
#     # Write to the shared resource
#     print("Writer is writing to the resource")
# 
#     write_mutex.acquire()
#     writers -= 1
#     if writers == 0:
#         read_try.release()
#     write_mutex.release()
# 
# # Create reader and writer threads
# reader_threads = [threading.Thread(target=reader) for _ in range(3)]
# writer_threads = [threading.Thread(target=writer) for _ in range(2)]
# 
# # Start the threads
# for t in reader_threads + writer_threads:
#     t.start()
# 
# # Wait for all threads to finish
# for t in reader_threads + writer_threads:
#     t.join()
# 
# print("All readers and writers have finished.")

## DP using semaphores
import threading
import time

# Number of philosophers
N = 5

# List of semaphores for chopsticks
chopsticks = [threading.Semaphore(1) for _ in range(N)]

# List of philosophers
philosophers = [f"Philosopher {i+1}" for i in range(N)]

def philosopher(id):
    while True:
        print(f"{philosophers[id]} is thinking.")
        time.sleep(1)

        print(f"{philosophers[id]} is hungry.")
        # Acquire the left chopstick
        chopsticks[id].acquire()

        # Acquire the right chopstick (wrap around for the last philosopher)
        chopsticks[(id + 1) % N].acquire()

        print(f"{philosophers[id]} is eating.")
        time.sleep(2)

        # Release the chopsticks
        chopsticks[id].release()
        chopsticks[(id + 1) % N].release()

        print(f"{philosophers[id]} finished eating and released the chopsticks.")

# Create philosopher threads
threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

# Start philosopher threads
for thread in threads:
    thread.start()

# Wait for all philosopher threads to finish
for thread in threads:
    thread.join()
