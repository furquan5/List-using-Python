import ctypes
class MeraList:
    def __init__(self):
        self.number=0
        self.capacity=1
        self.A=self.make_array(self.capacity)

    def __str__(self):
        result=''
        for i in range(self.number):
            result=result+str(self.A[i])+','

        return '[{}]'.format(result[:-1])



    def __getitem__(self,index):
        return self.A[index]

    def __len__(self):
        return self.number

    def delete(self,index):

        for i in range(index,self.number-1):
            self.A[i]=self.A[i-1]

        self.number-=1


    def insert(self,index,item):
        if self.number==self.capacity:
            self.resize(2*self.capacity)
            
        for i in range(self.number,index-1,-1):
            self.A[i]=self.A[i-1]

        self.A[index]=item
        self.number+=1
        
        

    def append(self,item):
        if self.number==self.capacity:
            self.resize(2*self.capacity)
        self.A[self.number]=item
        self.number+=1

    def resize(self,new_cap):
        B=self.make_array(new_cap)

        for i in range(self.number):
            B[i]=self.A[i]

        self.A=B
        self.capacity=new_cap

        
    def make_array(self,capacity):
        return(capacity*ctypes.py_object)()
        
     
       
