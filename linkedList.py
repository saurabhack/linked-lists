class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class linkedList:
    def __init__(self):
        self.header=None
    def push(self,data):
        self.New_node=node(data,self.header)
        self.header=self.New_node
    def display(self):
        i=self.header
        while(i!=None):
            print(i.data,end=" ")
            i=i.next
    def add_at(self,index,data):
        if index==0:
            self.push(data)
            return
        i=self.header
        counter=0
        while(i):
            if counter==index-1:
                L_node=node(data,i.next)
                i.next=L_node
                break
            i=i.next
            counter=counter+1
    def insert_end(self,data):
        if self.header==None:
            self.head=node(data,None)
            return
        i=self.header
        while(i.next):
            i=i.next

        i.next=node(data,None)

    def delete(self,index):
        if self.header==None:
            self.header=self.header.next
            return
        i=self.header
        counter=0
        while(i):
            if counter==index-1:
                i.next=i.next.next
                break
            counter=counter+1
            i=i.next
if __name__=="__main__":
    d=linkedList()
    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)
    d.add_at(3,4)
    d.add_at(2, 4)
    d.add_at(6, 4)
    d.insert_end(1)
    d.display()
    d.delete(4)
    d.delete(1)
    d.delete(2)
    print("")
    d.display()





