import os
import subprocess
import time

MNT_POINT = "/mnt"
FILE_SIZE_MB = 100
FILE_PATH = os.path.join(MNT_POINT, "testfile")

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def progress_bar(iterable, total, desc=""):
    print(desc)
    for i, item in enumerate(iterable, 1):
        yield item
        print(f"\r[{i}/{total}] {'=' * (i * 20 // total):<20}", end='', flush=True)
        time.sleep(0.1)
    print()

def measure_sequential_read_write():
    print("Testing Sequential Read/Write Speed...")
    write_speed = run_command(f"dd if=/dev/zero of={FILE_PATH} bs=1M count={FILE_SIZE_MB} oflag=dsync")
    read_speed = run_command(f"dd if={FILE_PATH} of=/dev/null bs=1M")
    return {"Sequential Write Speed": write_speed, "Sequential Read Speed": read_speed}

def measure_latency():
    print("Testing Latency...")
    write_latency = run_command(f"ioping -c 10 -D {MNT_POINT}")
    read_latency = run_command(f"ioping -c 10 -R {MNT_POINT}")
    return {"Write Latency": write_latency, "Read Latency": read_latency}

def measure_iops():
    print("Testing IOPS...")
    write_iops = run_command(f"fio --name=write_iops --ioengine=libaio --rw=randwrite --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting")
    read_iops = run_command(f"fio --name=read_iops --ioengine=libaio --rw=randread --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting")
    return {"Write IOPS": write_iops, "Read IOPS": read_iops}

def measure_throughput():
    print("Testing Throughput...")
    throughput = run_command(f"iostat -dx 1 10")
    return {"Throughput": throughput}

def check_fragmentation():
    print("Checking Fragmentation...")
    fragmentation = run_command(f"e4defrag -c {MNT_POINT}")
    return {"Fragmentation": fragmentation}

def measure_workload_patterns():
    print("Testing Workload Patterns...")
    workload_patterns = run_command(f"fio --name=workload_patterns --ioengine=libaio --rw=randrw --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting")
    return {"Workload Patterns": workload_patterns}

def clean_up():
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

def main():
    results = {}
    test_functions = [
        measure_sequential_read_write,
        measure_latency,
        measure_iops,
        measure_throughput,
        check_fragmentation,
        measure_workload_patterns
    ]
    
    for test_func in progress_bar(test_functions, total=len(test_functions), desc="Running Tests"):
        results.update(test_func())
    
    clean_up()
    print("All tests completed.")
    
    # Display the results table
    print("\nTest Results:")
    print("{:<30} {}".format("Test", "Result"))
    print("="*60)
    for test, result in results.items():
        print("{:<30} {}".format(test, result))

if __name__ == "__main__":
    main()
