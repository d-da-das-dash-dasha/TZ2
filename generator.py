import random

with open("test_10000.txt", "w") as file:
    for i in range(10000):
        file.write(str(random.uniform(-100, 100)) + ' ')

with open("test_100000.txt", "w") as file:
    for i in range(100000):
        file.write(str(random.uniform(-100, 100)) + ' ')

with open("test_1000000.txt", "w") as file:
    for i in range(1000000):
        file.write(str(random.uniform(-100, 100)) + ' ')

with open("test_10000000.txt", "w") as file:
    for i in range(10000000):
        file.write(str(random.uniform(-100, 100)) + ' ')

with open("test_100000000.txt", "w") as file:
    for i in range(100000000):
        file.write(str(random.uniform(-100, 100)) + ' ')