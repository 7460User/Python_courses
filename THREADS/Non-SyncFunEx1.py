import threading,time
def multable(n):
    print("Name of the thread{},exeuting multable():".format(threading.current_thread().name))
    if(n<=0):
        print("{} is invalid input".format(n))
    else:
        print("-"*50)
        print("mul Table for {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t{}X{}={}".format(n,i,n*i))
            time.sleep(1)
            print("-"*30)
t1=threading.Thread(target=multable,args=(10,2,))  
t2=threading.Thread(target=multable,args=(18,))
t3=threading.Thread(target=multable,args=(5,))
t1.start()
t2.start()
t3.start()         