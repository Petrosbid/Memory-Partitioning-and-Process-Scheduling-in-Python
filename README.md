# Memory-Partitioning-and-Process-Scheduling-in-Python
memory management with fixed partition technique in two single queue and multiple queue method.

## Overview

This repository contains a Python implementation of memory partitioning and process scheduling. The code demonstrates two methods for allocating processes to memory partitions: single queue and multiple queue. By using threading and queues, the code efficiently manages process allocation and deallocation, aiming to optimize memory utilization and throughput.

## Features

- **Dynamic Memory Partitioning**: The memory is partitioned dynamically based on the given size.
- **Process Scheduling**: Two methods of scheduling (single queue and multiple queue) are implemented.
- **Threading**: Utilizes Python's `threading` module to handle process allocation and deallocation concurrently.
- **Performance Metrics**: Calculates memory utilization and throughput for both scheduling methods.
- **Colorful Output**: Uses the `colorama` library to enhance console output for better readability.

## Requirements

- Python 3.x
- `colorama` library

You can install the `colorama` library using pip:
```bash
pip install colorama
```
## Usage
Clone the repository:

``` 
git clone https://github.com/yourusername/memory-partitioning-scheduling.git
cd memory-partitioning-scheduling
```

Follow the prompts:
Enter the total memory size.
Enter the number of processes.
Enter the memory size and duration time for each process.


## Example 
![Screenshot 2024-12-21 185723](https://github.com/user-attachments/assets/945f80c2-2ef3-49df-9ef3-994303d588c8)

### Contribution
Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
