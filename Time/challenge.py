import time

print("Showing clock info for various implementations:")

print("time()\t\t\t",  time.get_clock_info("time"))
print("perf_counter()\t\t",time.get_clock_info("perf_counter"))
print("monotonic()\t\t ",time.get_clock_info("monotonic"))
print("process_time()\t\t",time.get_clock_info("process_time"))