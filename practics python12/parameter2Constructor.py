class Parameter:
    def __init__(para,a,b):
        print("i am from parameterized constructor:")
        para.a=a
        para.b=b
        print("value of a:{}".format(para.a))
        print("value of b:{}".format(para.b))
p=Parameter(20,10)
p1=Parameter(40,4)

        