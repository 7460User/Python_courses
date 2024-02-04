import threading
import time
class Call(threading.Thread):
    def run(self):
        for i in range(10):
            print(threading.current_thread().getName())
obj=Call(name='sending msg hello')
obj1=Call(name='rec msg byee')
obj.start()
obj1.start()