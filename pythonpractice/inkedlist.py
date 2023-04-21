# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# Start=None
# itr = None
# var=0
# while(var !=-2):
#     var = int(input("Enter your values : "))
#     x=Node(var)
#     if Start is None:
#         Start=x
#         itr=Start
#     else:
#         itr.next=x
#         itr=x

# print("Nodes are")
# while(hasattr(Start, 'val')):
    
#         print(Start.val,"=>", end="")
#         Start=Start.next
# else:print("End of list")




class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
Start=None
itr = None
var=0
traverse =None
while(var !=-2):
    var = int(input("Enter your values : "))
    x=Node(var)
    if Start is None:
        Start=x
        itr=Start
        traverse=Start

    else:
        itr.next=x
        itr=x

def printer(goddha):
    print("Nodes are")
    while(goddha!=None):
        print(goddha.val,"=>", end="")
        goddha=goddha.next

printer(traverse)
# else:print("End of list")
var = 0 # reset
condition =input("Want to add anything , y for yes , any key for no")
if(condition=='y'):
    while(var !=-2):
        var = int(input("Enter your values : "))
        x=Node(var)
        itr.next=x
        itr=x

printer(Start)

