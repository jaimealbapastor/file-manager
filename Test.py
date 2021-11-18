import sys
from time import sleep

for i in range(4):
    print(f"\rTime remaining: {i} Seconds", flush=True, end="")
    sleep(1)
