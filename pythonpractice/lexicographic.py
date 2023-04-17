string = []
reverse =[]
counter=int(0)
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

# for j in range(0,reverse.__len__()):
#     counter = 0
#     for i in range(0,reverse[j].__len__()) :
#         if(reverse[j][i].__contains__("a")):
#             counter =counter+1
#         elif (reverse[j][i].__contains__("e")):
#             counter =counter+1
#         elif (reverse[j][i].__contains__("i")):
#             counter =counter+1
#         elif (reverse[j][i].__contains__("o")):
#             counter =counter+1
#         elif (reverse[j][i].__contains__("u")):
#             counter =counter+1
        
    # print( "Number of vowels in ",reverse[j],"is",counter )
 
for i in range(0,reverse.__len__()):
    prCounter= counter
    for words in range(0,reverse[i].__len__()):
        
        if(reverse[i][words].__contains__("a")):
            counter =counter+1
        elif (reverse[i][words].__contains__("e")):
            counter =counter+1
        elif (reverse[i][words].__contains__("i")):
            counter =counter+1
        elif (reverse[i][words].__contains__("o")):

            counter =counter+1
        elif (reverse[i][words].__contains__("u")):
            counter =counter+1
        
    print( "Number of vowels in ",reverse[i],"is",counter-prCounter )
                 
