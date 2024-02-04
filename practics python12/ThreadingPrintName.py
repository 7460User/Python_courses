from threading import *
import time
s=Semaphore()
def wish(name):
    s.acquire()
    for i in range(5):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Dhoni',))
t2=Thread(target=wish,args=('Rohit',))
t3=Thread(target=wish,args=('Kohli',))
t4=Thread(target=wish,args=('Panday',))
t5=Thread(target=wish,args=('Sky',))
t6=Thread(target=wish,args=('Kishan',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()



