import threading,time 
def multable(n):
    L.acquire()
    print("Name of the thread {}, exeuting multable():".format(threading.current_thread().name))
    if(n<=0):
        print("{} is invalid input number".format(n))
    else:
        print("{} mul table".format(n))
        for i in range(1,11):
            print("\t{}X{}={}".format(n,i,n*i))
            time.sleep(1)
           
        L.acquire()
        print("byyyy")
L=threading.Lock()
t1=threading.Thread(target=multable,args=(3,))
t2=threading.Thread(target=multable,args=(7,))
t3=threading.Thread(target=multable,args=(-9,))
t1.start()
t2.start()
t3.start()       
t3.join()