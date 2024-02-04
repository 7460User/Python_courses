import threading,time
class Table:
    def multable(self,n):
        print("Name of the thread{},exeuting multable():".format(threading.current_thread().name))  
        if(n<=0):
            print("{} is invalid input".format(n))
        else:
            print("mul table for {}".format(n))
            for i in range(1,11):
                print("\t{}X{}={}".format(n,i,n*i))
                time.sleep(1 )
                
t1=threading.Thread(target=Table().multable,args=(10,))
t2=threading.Thread(target=Table().multable,args=(5,))
t1.start()
t2.start()

