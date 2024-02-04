for v in range(1,101):
    if v>1:
        for i in range(2,v):
            if (v % i) ==0:
                break
            else:
                print(v,"this is prime number:")
# else:
#     print(v,"Not a prime number:")

