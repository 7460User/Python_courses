from time import strftime
import  tkinter

def clock():
    time1 = strftime("%H : %M : %S : %p")
    label.config(text=time1,font=("arial",130))
    label.after(1000,clock)
    print("Hello good morning:")
    
root = tkinter.Tk()
label = tkinter.Label(root)
label.pack()
clock()
root.mainloop()    