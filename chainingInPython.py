class Myhash:
    def __init__(self,b):
        self.BUCKET = b
        self.table = [ [] for x in range(b)]
        
    def insert(self,x):
            
        i = x % self.BUCKET
        self.table[i].append(x)
            
    def search(self,x):
        i = x % self.BUCKET
        return x in self.table[i]
        
    def remove(self, x):
        i = x % self.BUCKET
        inTable = self.search(x)
        if inTable:
            self.table[i].remove(x)
        else:
            print("Item Not in Hash")
                
myHash = Myhash(5)
myHash.insert(51)
myHash.insert(20)
myHash.insert(31)
myHash.insert(25)
myHash.remove(31)
myHash.remove(47)
print(myHash.table)