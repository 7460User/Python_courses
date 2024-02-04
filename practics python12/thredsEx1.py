from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for i in range(400):
            print("Hello ji")
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(500):
            print("Good morning ji")
            sleep(2)
class C(Thread):
    def run(self):
        for i in range(5):
            print("Hello Govind")
            sleep(3) 
t1 = A()
t2 = B()

t3 = C()



t1.start()

t2.start()

t3.start()

t3.join()


