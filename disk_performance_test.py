import os
import time
import subprocess
import random

MNT_POINT = "/mnt"
FILE_SIZE_MB = 100
FILE_PATH = os.path.join(MNT_POINT, "testfile")

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def measure_sequential_read_write():
    print("Testing Sequential Read/Write Speed...")
    print("Sequential Write Speed:")
    print(run_command(f"dd if=/dev/zero of={FILE_PATH} bs=1M count={FILE_SIZE_MB} oflag=dsync"))

    print("Sequential Read Speed:")
    print(run_command(f"dd if={FILE_PATH} of=/dev/null bs=1M"))

def measure_latency():
    print("Testing Latency...")
    print("Write Latency:")
    print(run_command(f"ioping -c 10 -D {MNT_POINT}"))

    print("Read Latency:")
    print(run_command(f"ioping -c 10 -R {MNT_POINT}"))

def measure_iops():
    print("Testing IOPS...")
    print("Write IOPS:")
    print(run_command(f"fio --name=write_iops --ioengine=libaio --rw=randwrite --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting"))

    print("Read IOPS:")
    print(run_command(f"fio --name=read_iops --ioengine=libaio --rw=randread --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting"))

def measure_throughput():
    print("Testing Throughput...")
    print(run_command(f"iostat -dx 1 10"))

def check_fragmentation():import os
import time
import subprocess
import random

MNT_POINT = "/mnt"
FILE_SIZE_MB = 100
FILE_PATH = os.path.join(MNT_POINT, "testfile")

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def measure_sequential_read_write():
    print("Testing Sequential Read/Write Speed...")
    print("Sequential Write Speed:")
    print(run_command(f"dd if=/dev/zero of={FILE_PATH} bs=1M count={FILE_SIZE_MB} oflag=dsync"))

    print("Sequential Read Speed:")
    print(run_command(f"dd if={FILE_PATH} of=/dev/null bs=1M"))

def measure_latency():
    print("Testing Latency...")
    print("Write Latency:")
    print(run_command(f"ioping -c 10 -D {MNT_POINT}"))

    print("Read Latency:")
    print(run_command(f"ioping -c 10 -R {MNT_POINT}"))

def measure_iops():
    print("Testing IOPS...")
    print("Write IOPS:")
    print(run_command(f"fio --name=write_iops --ioengine=libaio --rw=randwrite --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting"))

    print("Read IOPS:")
    print(run_command(f"fio --name=read_iops --ioengine=libaio --rw=randread --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting"))

def measure_throughput():
    print("Testing Throughput...")
    print(run_command(f"iostat -dx 1 10"))

def check_fragmentation():
    print("Checking Fragmentation...")
    print(run_command(f"e4defrag -c {MNT_POINT}"))

def measure_workload_patterns():
    print("Testing Workload Patterns...")
    print(run_command(f"fio --name=workload_patterns --ioengine=libaio --rw=randrw --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting"))

def clean_up():
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

def main():
    measure_sequential_read_write()
    measure_latency()
    measure_iops()
    measure_throughput()
    check_fragmentation()
    measure_workload_patterns()
    clean_up()
    print("All tests completed.")

if __name__ == "__main__":
    main()
    print("Checking Fragmentation...")
    print(run_command(f"e4defrag -c {MNT_POINT}"))

def measure_workload_patterns():
    print("Testing Workload Patterns...")
    print(run_command(f"fio --name=workload_patterns --ioengine=libaio --rw=randrw --bs=4k --numjobs=1 --size=100M --runtime=10 --filename={FILE_PATH} --group_reporting"))

def clean_up():
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

def main():
    measure_sequential_read_write()
    measure_latency()
    measure_iops()
    measure_throughput()
    check_fragmentation()
    measure_workload_patterns()
    clean_up()
    print("All tests completed.")

if __name__ == "__main__":
    main()
