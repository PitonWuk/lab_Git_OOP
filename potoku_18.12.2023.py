import threading

def print_cube(num):
    print("Cube: ", num * num * num)

def print_square(num):
    print("Square: ", num * num)

t1 = threading.Thread(target=print_cube, args=(10, ))
t2 = threading.Thread(target=print_square, args=(10, ))

t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")

#PRACTICE

import threading
import random

def calculare_midl(arr):
    midl = sum(arr) / len(arr)

data_size = 10000
data = [random.randint(0, 1000) for _ in range(data_size)]
num_threads = 4

chunk_size = len(data) // num_threads
chunks = [data[i: i + chunk_size] for i in range(0, len(data), chunk_size)]
results = []

threads = []
for chunk in chunks:
    thread = threading.Thread(target=lambda x: results.append(calculare_midl(x)), args=(chunk, ))

    threads.append(thread)
    thread.start()




