#collisions are handled using Open Addressing

class MyHash:
    # -1 for empty slot and -2 for deleted slot
    def __init__(self,b):
        self.BUCKET = b
        self.table = [-1]*b #making each slot as empty in intialization
        self.size = 0
        
    def hash(self,x):
        return x % self.BUCKET
    
    def search(self,x):
        myhash = hash(x)
        t = self.table
        i = myhash
        while t[i] != -1: #cyclic rotation till we encounter an empty slot
            if t[i] == x:
                return True
            i = (i+1) % self.BUCKET  # moving linearly, after one roation it will become zero
            
            if i == myhash:
                return False
        return False
    
    def insert(self,x):
        
        if self.size == self.cap:
            return False
        
        if self.search(x) == True:
            return False
        
        i = self.hash(x)
        t = self.table
        
        while t[i] not in (-1 ,-2): #for linear probing
            i = (i + 1)%self.BUCKET
        
        t[i] = x 
        self.size = self.size + 1
        return True
    
    def search(self,x):
        myhash = hash(x)
        t = self.table
        i = myhash
        while t[i] != -1: #cyclic rotation till we encounter an empty slot
            if t[i] == x:
                t[i] = -2
                return True
            i = (i+1) % self.BUCKET  # moving linearly, after one roation it will become zero
            
            if i == myhash: #means we have reached the same slot i.e one time tranversing is done
                return False
        return False
