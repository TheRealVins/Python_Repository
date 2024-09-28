import sys
from time import sleep

words = "Welcome to CB#SA.NET.CO"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()