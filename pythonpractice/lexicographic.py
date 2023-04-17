string = []
reverse =[]
x= int((input("Enter the no. of strings to be sorted : "))) 
for i in range(0,x):
    string.append(str(input()))
for i in range(0,string.__len__(),1):
    for j in range(0,string.__len__()-1,1):
        if(string[j]>string[j+1]):
            temp =string[j]
            string[j] =string[j+1] 
            string[j+1]=temp
print("Alphabetically sorted list is : ",string)

for start in range(string.__len__()-1,-1,-1):
    reverse.append(string[start])
print(reverse)
