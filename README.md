# Memory-Partitioning-and-Process-Scheduling-in-Python
memory management with fixed partition technique in two single queue and multiple queue method.
**Overview**
This repository contains a Python implementation of memory partitioning and process scheduling. The code demonstrates two methods for allocating processes to memory partitions: single queue and multiple queue. By using threading and queues, the code efficiently manages process allocation and deallocation, aiming to optimize memory utilization and throughput.

**Features**
Dynamic Memory Partitioning: The memory is partitioned dynamically based on the given size.
Process Scheduling: Two methods of scheduling (single queue and multiple queue) are implemented.
Threading: Utilizes Python's threading module to handle process allocation and deallocation concurrently.
Performance Metrics: Calculates memory utilization and throughput for both scheduling methods.
Colorful Output: Uses the colorama library to enhance console output for better readability.
**Requirements**
Python 3.x
colorama library
You can install the colorama library using pip:

bash
pip install colorama
**Usage**
Clone the repository:
bash
git clone https://github.com/yourusername/memory-partitioning-scheduling.git
cd memory-partitioning-scheduling
**Run the script:**
bash
python scheduler.py
Follow the prompts:
Enter the total memory size.
Enter the number of processes.
Enter the memory size and duration time for each process.
Example:

arduino
Enter the total memory size: 16
Enter the number of processes: 3
Enter the memory size & duration time for process 1: 2 5
Enter the memory size & duration time for process 2: 4 3
Enter the memory size & duration time for process 3: 8 2
Code Explanation
Partition Class
python
Copy code
class Partition:
    def __init__(self, size):
        self.size = size
        self.is_free = True
        self.process = None

    def allocate(self, process):
        self.is_free = False
        self.process = process

    def free(self):
        self.is_free = True
        self.process = None

    def __repr__(self):
        return f"{self.size}"
Represents a memory partition.
Methods to allocate and free the partition.
Process Class
python
Copy code
class Process:
    def __init__(self, pid, size, duration):
        self.pid = pid
        self.size = size
        self.duration = duration
Represents a process with a process ID, size, and duration.
Creating Partitions
python
Copy code
def create_partitions(memory_size):
    partitions = []
    size = 1
    while memory_size > size:
        partitions.append(Partition(size))
        memory_size -= size
        size *= 2
    partitions.append(Partition(memory_size))
    return sorted(partitions, key=lambda partition: partition.size)
Dynamically creates memory partitions based on the given total memory size.
Freeing Partitions
python
Copy code
def free_partition(partition, duration):
    time.sleep(duration)
    partition.free()
Frees a partition after a certain duration.
Process Scheduling Methods
Single Queue
python
Copy code
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
Allocates processes to partitions using a single queue.
Multiple Queue
python
Copy code
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
Allocates processes to partitions using multiple queues, one for each partition.
Example Output
arduino
Copy code
-------Partitions size-------
[1, 2, 4, 8, 1]

-------Enter your processes informations-------
Enter the memory size & duration time for process 1: 2 5
Enter the memory size & duration time for process 2: 4 3
Enter the memory size & duration time for process 3: 8 2

-------Running in single queue method-------
Utilization: 70%
Throughput: 3 / 10

-------Running in multiple queue method-------
Utilization: 75%
Throughput: 3 / 8
Contribution
Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.
