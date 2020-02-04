# Program that acts like a stop watch or timer

import time

# TODO: is there any way for Python to make a sound/notification to show up?

# Handles seconds
time_limit = int(input("Enter your seconds: "))

while time_limit != 0:
        print(time_limit)
        time_limit -= 1        
        time.sleep(1)

print("RING!")
