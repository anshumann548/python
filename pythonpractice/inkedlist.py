class Node:
    def __init__(self,val):
        self.val=val 
        self.nextadr=None

x=0
var=0
Start = None
while(var!=-2):
    var = int(input("Enter values you want"))
    x = Node(var)
    if Start is None: 
        Start = x
    
    itr=Start
    
    while(itr.nextadr!=None):
        if (Start != x):
            itr=x

print("Your list is ")
while (Start!=None): print(Start.val,"->");Start=Start.nextadr