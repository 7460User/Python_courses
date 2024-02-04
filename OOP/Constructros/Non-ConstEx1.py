class Test:
    def noncon(self):
        self.eno=10
        self.name="govind"
        self.marks=33.4
#main program       
e=Test()
print("Content of e=",e.__dict__)
e.noncon()
print("Content of e ofter reading=",e.__dict__)        
