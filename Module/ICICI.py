bname="ICICI"
addr="HYD"
def simpleint():
    p=float(input("Enter Pricipale Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter role of interst:"))
    si=(p*t*r)/100
    totamt=p+si
    print("-"*50)
    print("principal Amount:{}".format(p))
    print("time:({})".format(t))
    print("rate interset:({})".format(r))
    print("simple instrest:({})".format(si))
    print("Total amount to pay:({})".format(totamt))
    print("-"*50)
simpleint()