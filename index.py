import time

def print_integer_every_second():
    count = 0
    while True:
        print(count)
        count += 1
        time.sleep(1)

if __name__ == "__main__":
    print_integer_every_second()
