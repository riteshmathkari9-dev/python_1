class Utils():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return(self.a+self.b)
    
    def mul(self):
        return(self.a*self.b)
    
if __name__ == '__main__':
    addition=Utils(10,20).add()
    multipication=Utils(10,20).mul()
    print(addition,multipication)