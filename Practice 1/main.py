# include
from random import randint
from timeit import default_timer as timer

def generate_random_key(size):
    key = ""

    for i in range(size):
        tmp = str(randint(0, 1))
        key += tmp

    key = key.lstrip('0')
    return key

def bruteforce(size, key):

    i = 0
    var_num = pow(2, size)
    key = '0b' + key

    start_time = timer()

    while i <= var_num:
        #print("Size : " + str(size))
        #print("cur : " + str(bin(i)))
        #print("key : " + str(key))
        if bin(i) == key:
            break
        i += 1

    finish_time = timer()

    print("{0} bit - {1} ms".format(size, (finish_time-start_time)*1000))

def main():
    # 1-st part of the task
    print("\nPart 1. Number of keys.")
    lengths = {}

    i: int = 8
    while i <= 4096:
        lengths[i] = pow(2, i)
        print('{0} - {1}'.format(i, lengths[i]))
        i *= 2

    # 2-nd part of the task
    print("\nPart 2. Random keys.")
    keys = {}   # dictionary

    i = 8
    while i <= 4096:
        keys[i] = generate_random_key(i)
        print('{0} - {1}'.format(i, keys[i]))
        i *= 2

    # 3-rd part of the task
    print("\nPart 3. Brute-force.")
    for size, key in keys.items():
        bruteforce(size, key)

if __name__ == "__main__":
    main()