def getvalues():
    a,b=int(input("Enter First Value:")),int(input("Enter Secound Value:"))
    op=input("Enter Arithmetic operator: ")
    return a,b ,op
def performaop():
    a,b,op=getvalues()
    if(op=="+"):
        return("{}+{}={}".format(str(a),str(b),str(a+b)))

    if(op=="-"):
        return("{}-{}={}".format(str(a),str(b),str(a-b)))

    if(op=="*"):
        return("{}*{}={}".format(str(a),str(b),str(a*b))) 

    if(op=="/"):
        return("{}/{}={}".format(str(a),str(b),str(a/b)))

    if(op=="//"):
        return("{}//{}={}".format(str(a),str(b),str(a//b)))

    if(op=="%"):
        return("{}%{}={}".format(str(a),str(b),str(a%b)))

    if(op=="*"):
        return("{}*{}={}".format(str(a),str(b),str(a*b)))

    if(op=="*"):
        return("{}**{}={}".format(str(a),str(b),str(a**b)))  

    if(op not in ["+","-","*","**","/","//","%",]):
        return "{} Not an Aop Operator".format(op)

#main progran

res=performaop()
print(res)