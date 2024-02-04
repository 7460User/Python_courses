import json

class A:
    def __init__(self):
        self.name=input("Enter Student Name:")
        self.age=input("Enter Student Age:")
        self.college=input("Enter Student College:")
    def show(self):
        print("="*40)
        return{
            "Name":self.name,
            "Age":self.age,
            "College":self.college,
        }
obj=A()
govind=obj.show()
json_data=json.dumps(govind,indent=4)
print(json_data)
        