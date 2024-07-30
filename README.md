
# Disk Performance Testing Script

This script performs a series of disk performance tests, including sequential read/write speeds, latency, IOPS (Input/Output Operations Per Second), throughput, fragmentation check, and workload patterns on a specified mount point. The results of these tests are printed to the console.

## Prerequisites

- Python 3.x
- `dd` utility
- `ioping` utility
- `fio` utility
- `iostat` utility
- `e4defrag` utility

Make sure the required utilities are installed on your system before running the script.

## How to Use

1. **Set the Mount Point:**

   The default mount point is set to `/mnt`. If you want to test a different mount point, update the `MNT_POINT` variable in the script.

2. **Set the File Size:**

   The default file size for the tests is set to 100 MB. If you want to use a different file size, update the `FILE_SIZE_MB` variable in the script.

3. **Run the Script:**

   Execute the script using the following command:
   ```sh
   python disk_performance_test.py
   ```

## Script Details

### Constants

- `MNT_POINT`: The mount point where the tests will be conducted.
- `FILE_SIZE_MB`: The size of the test file in megabytes.
- `FILE_PATH`: The path to the test file.

### Functions

1. **run_command(command):**
   - Executes a shell command and returns the output.
   - Parameters:
     - `command` (str): The command to execute.
   - Returns:
     - `str`: The output of the command.

2. **measure_sequential_read_write():**
   - Measures the sequential read/write speed using the `dd` utility.
   - Prints the results to the console.

3. **measure_latency():**
   - Measures the write and read latency using the `ioping` utility.
   - Prints the results to the console.

4. **measure_iops():**
   - Measures the write and read IOPS using the `fio` utility.
   - Prints the results to the console.

5. **measure_throughput():**
   - Measures the throughput using the `iostat` utility.
   - Prints the results to the console.

6. **check_fragmentation():**
   - Checks the fragmentation of the specified mount point using the `e4defrag` utility.
   - Prints the results to the console.

7. **measure_workload_patterns():**
   - Measures the performance under mixed workload patterns using the `fio` utility.
   - Prints the results to the console.

8. **clean_up():**
   - Removes the test file created during the tests.

9. **main():**
   - Executes all the performance tests and cleans up afterward.
   - Prints a completion message to the console.

### Execution

The script executes the following sequence of functions:
1. `measure_sequential_read_write()`
2. `measure_latency()`
3. `measure_iops()`
4. `measure_throughput()`
5. `check_fragmentation()`
6. `measure_workload_patterns()`
7. `clean_up()`

The results of each test are printed to the console. After all tests are completed, the script prints "All tests completed."

## Note

Ensure you have the necessary permissions to run the disk performance tests and to create/remove files in the specified mount point.


