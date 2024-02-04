from threading import Thread 
from time import sleep
class Hello(Thread):
    def run(self):
            for i in range(5):
                print("Hello Mr.Govind")
                sleep(1)


class Goodmorning(Thread):
    def run(self):
        for i in range(5):
            print("Good Morning")
            sleep(1)


t1=Hello()
t2=Goodmorning()
print("-"*30)
t1.start()
sleep(0.5)
t2.start()

t1.join()
t2.join()
print("byy.....")