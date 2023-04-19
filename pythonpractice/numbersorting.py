
c = 0
l = 0
z = 0
x = int(input("Enter the size of list=> "))
mylist=[]
for i in range(0,x,1):
    mylist.append(int(input()))
#print(mylist)
finalist=[]
for i in mylist:
    isPrime = True 
    for k in range(2,i):
        if(i%k==0):
            isPrime = False
            break
    if(isPrime) : finalist.append(i)
 
for m in finalist:
    l+= m
print("Sum of the prime numbers is:",l)
n = mylist.__len__()
key=n-1
for i in range(0,key,1):
    for j in range(0,key,1):
        if(mylist[j]<mylist[j+1]):
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
 

print("Decending list is :",mylist)

for i in range(0,mylist.__len__()):
        z=int(z)+mylist[i]
print("Average of numbers is :" ,z/mylist.__len__())

print("Largest number is :",mylist[0])

least = mylist.__len__()-1

print("Smallest number is :",mylist[least])
