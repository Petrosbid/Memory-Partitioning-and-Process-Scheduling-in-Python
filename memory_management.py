import time
import threading
from queue import Queue
from colorama import Fore 

class Partition:
    def __init__(self, size): 
        self.size = size
        self.is_free = True
        self.process = None

    # Allocate a process to this partition
    def allocate(self, process):
        self.is_free = False
        self.process = process

    # Free this partition
    def free(self):
        self.is_free = True
        self.process = None

    def __repr__(self):
        return f"{self.size}"

class Process:
    def __init__(self, pid, size, duration):  
        self.pid = pid
        self.size = size
        self.duration = duration

# Function to create partitions based on the total memory size
def create_partitions(memory_size):
    partitions = []
    size = 1
    while memory_size > size:
        partitions.append(Partition(size))
        memory_size -= size
        size *= 2
    partitions.append(Partition(memory_size))
    return sorted(partitions, key=lambda partition: partition.size)

# Function to free a partition after a certain duration
def free_partition(partition, duration):
    time.sleep(duration)
    partition.free()

# Function to process a queue of processes for a given partition
def process_partition_queue(partition, queue):
    while not queue.empty():
        process = queue.get()
        partition.allocate(process)
        free_partition(partition, process.duration)

# Single queue scheduling method
def single_queue(partitions, processes):
    queue = processes[:]
    start_time = time.time()

    while queue:
        process = queue.pop(0)
        for partition in partitions:
            if process.size <= partition.size:
                while not partition.is_free:
                    time.sleep(1)
                partition.allocate(process)
                threading.Thread(target=free_partition, args=(partition, process.duration)).start()
                break

    while not all(partition.is_free for partition in partitions):
        time.sleep(0.5)

    end_time = time.time()
    total_time = int(end_time - start_time)
    throughput = f"{len(processes)} / {total_time}" if total_time > 0 else 0
    utilization = int((sum(p.size * p.duration for p in processes) / (memory_size * total_time))*100) if total_time > 0 else 0

    return utilization, throughput

# Multiple queue scheduling method
def multiple_queue(partitions, processes):
    queues = [Queue() for _ in partitions]

    for process in processes:
        for i, partition in enumerate(partitions):
            if process.size <= partition.size:
                queues[i].put(process)
                break

    start_time = time.time()
    threads = []
    for i, partition in enumerate(partitions):
        t = threading.Thread(target=process_partition_queue, args=(partition, queues[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    total_time = int(end_time - start_time)
    throughput = f"{len(processes)} / {total_time}" if total_time > 0 else 0
    utilization = (sum(p.size * p.duration for p in processes) / (memory_size * total_time)) * 100 if total_time > 0 else 0

    return utilization, throughput

# Main code to run the scheduling simulation
if __name__ == "__main__":
    memory_size = int(input(Fore.BLUE + "Enter the total memory size: "))
    num_processes = int(input("Enter the number of processes: "))

    print(Fore.YELLOW + "\n-------Partitions size-------")
    partitions = create_partitions(memory_size)
    print(Fore.GREEN + f"{partitions}")

    processes = []
    print(Fore.YELLOW + "\n-------Enter your processes informations-------")
    for i in range(num_processes):
        size, duration = map(int, input(Fore.BLUE + f"Enter the memory size & duration time for process {i+1}: ").split())
        processes.append(Process(i + 1, size, duration))

    print(Fore.YELLOW + "\n-------Running in single queue method-------")
    utilization_single, throughput_single = single_queue(partitions, processes)
    print(Fore.GREEN + f"Utilization: {utilization_single}%")
    print(f"Throughput: {throughput_single}")

    print(Fore.YELLOW + "\n-------Running in multiple queue method-------")
    utilization_multiple, throughput_multiple = multiple_queue(partitions, processes)
    print(Fore.GREEN + f"Utilization: {int(utilization_multiple)}%")
    print(f"Throughput: {throughput_multiple}")
