class Poy:
    def draw1(self):
        print("Drawing circle")

class React(Poy):
    def draw2(self):
        print("Drawing React:")
        self.draw1
        
r=React()        
r.draw1()
        