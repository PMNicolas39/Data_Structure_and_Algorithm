'''
    Muti threading (đa luồng) will boost the speed of command, do multitask
'''
import threading
import time

# example: calculate the square and cubic of list of numbers

arr = [2, 3, 8, 9]


def calc_square(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("square: ", i * i)


def calc_cubic(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("cubic: ", i * i * i)


# Start time
Start_time = time.time()

# Phân luồng cho tính toán cubic & square: multithreading
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cubic, args=(arr,))

# Start Threads
t1.start()
t2.start()

# End the thread Execution
t1.join()
t2.join()

#End time
End_time = time.time()
# Execution time
exe_time = End_time - Start_time

print(f"Done in: {exe_time:.2f}s")
