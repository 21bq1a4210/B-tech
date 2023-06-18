# # # #Bounded-Buffer problem
# # # import threading 
# # # BUFFER_SIZE = 5
# # # NUM_ITEMS = 10
# # # 
# # # buffer = []
# # # mutex = threading.Lock()
# # # items_available = threading.Semaphore(0)
# # # spaces_available = threading.Semaphore(BUFFER_SIZE)
# # # 
# # # def producer():
# # #     for i in range(NUM_ITEMS):
# # #         item = f"Item {i} from producer"
# # #         spaces_available.acquire()
# # #         mutex.acquire()
# # #         buffer.append(item)
# # #         print(f"Producer produced {item}")
# # #         mutex.release()
# # #         items_available.release()
# # # 
# # # def consumer():
# # #     for i in range(NUM_ITEMS):
# # #         items_available.acquire()
# # #         mutex.acquire()
# # #         item = buffer.pop(0)
# # #         print(f"Consumer consumed {item}")
# # #         mutex.release()
# # #         spaces_available.release()
# # # 
# # # producer_thread = threading.Thread(target=producer)
# # # consumer_thread = threading.Thread(target=consumer)
# # # 
# # # producer_thread.start()
# # # consumer_thread.start()
# # # 
# # # producer_thread.join()
# # # consumer_thread.join()
# # # 
# # # print("Producer and consumer have finished.")
import threading as thread
import random

global x                #Shared Data
x = 0
lock = thread.Lock()    #Lock for synchronising access

def Reader():
    global x
    print('Reader is Reading!')
    lock.acquire()      #Acquire the lock before Reading (mutex approach)
    print('Shared Data:', x)
    lock.release()      #Release the lock after Reading
    print()

def Writer():
    global x
    print('\n Writer is Writing!')
    lock.acquire()      #Acquire the lock before Writing
    x += 1              #Write on the shared memory
    print('Writer is Releasing the lock!')
    lock.release()      #Release the lock after Writing
    print()

for i in range(0, 10):
    randomNumber = random.randint(0, 100)   #Generate a Random number between 0 to 100
    if(randomNumber > 50):
        Thread1 = thread.Thread(target = Reader)
        Thread1.start()
    else:
        Thread2 = thread.Thread(target = Writer)
        Thread2.start()

Thread1.join()
Thread2.join()

# ## DP using semaphores
# import threading
# import time
# 
# # Number of philosophers
# N = 5
# 
# # List of semaphores for chopsticks
# chopsticks = [threading.Semaphore(1) for _ in range(N)]
# 
# # List of philosophers
# philosophers = [f"Philosopher {i+1}" for i in range(N)]
# 
# def philosopher(id):
#     while True:
#         print(f"{philosophers[id]} is thinking.")
#         time.sleep(1)
# 
#         print(f"{philosophers[id]} is hungry.")
#         # Acquire the left chopstick
#         chopsticks[id].acquire()
# 
#         # Acquire the right chopstick (wrap around for the last philosopher)
#         chopsticks[(id + 1) % N].acquire()
# 
#         print(f"{philosophers[id]} is eating.")
#         time.sleep(2)
# 
#         # Release the chopsticks
#         chopsticks[id].release()
#         chopsticks[(id + 1) % N].release()
# 
#         print(f"{philosophers[id]} finished eating and released the chopsticks.")
# 
# # Create philosopher threads
# threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
# 
# # Start philosopher threads
# for thread in threads:
#     thread.start()
# 
# # Wait for all philosopher threads to finish
# for thread in threads:
#     thread.join()
# 