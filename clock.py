import os
class Clock():
    def __init__(self,size=3):
        self.size=size
        self.lst=[None for i in range(size)]
        self.lstR=[-1 for i in range(size)]
        self.num_sub=0
        self.ptr=0
    def next(self):
        self.ptr=self.ptr+1 if self.ptr<self.size-1 else 0
    def show(self):
        for i in range(self.size):
            # if self.lst[i] is None:
            #     break
            print((self.lst[i],self.lstR[i]),"<--"if self.ptr==i else "")
        print()
    def Action(self,page):
        if page in self.lst:#does not move if page exists
            self.lstR[self.lst.index(page)]=1
            self.show()
            return True 
        while(True):               
            if self.lstR[self.ptr]<=0:   #substitution
                self.lst[self.ptr]=page
                self.lstR[self.ptr]=1
                self.next()
                self.num_sub+=1
                self.show()
                return True
            else: 
                self.lstR[self.ptr]=0   
                self.next()                 

if __name__=="__main__":
    os.system("cls")
    clock=Clock(int(input("enter size:")))
    #SEQ=[1,2,3,5,6,8,3,7,9,6,12,3,6,5,4,10,11]:
    #SEQ=[1,5,2,5,1,4,1,5,3]:
    SEQ=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    for x in SEQ:
        print(f"-->{x}")
        clock.Action(str(x))
    while(True):
        clock.Action(input("ENTER PAGE : "))
    
    