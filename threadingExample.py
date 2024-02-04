from threading import *
import time
s=Semaphore()
def Student(name):
    s.acquire()
    for i in range(100,0,-1):
        print("Good Evening:",end=' ')
        time.sleep(2)
        print(name)
        s.release()
t1 = Thread(target=Student, args=("Dhoni",))
t2 = Thread(target=Student, args=("RohitSharma",))
t3 = Thread(target=Student, args=("Virat",))
t4 = Thread(target=Student, args=("Surya",))
t1.start()
t2.start()
t3.start()
t4.start()        
