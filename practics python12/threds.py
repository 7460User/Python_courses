from threading import Thread
from time import sleep

class A(Thread):
    def run(self):
        for i in range(5):
            print("Sentric")
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Govind")
            sleep(2)

class C(Thread):
    def run(self):
        for i in range(2):
            print("Hello Good Morning")
            sleep(2)
s1 = A()
s2 = B()
s3 = C()

s1.start()
s2.start() 
s1.join()
s3.start()