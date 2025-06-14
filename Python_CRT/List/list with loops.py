Num_List=[10,20,30,40,50,60,70,80,90]
print(Num_List)
#using for loop
print("Accessing the List Elements using for loop without indexing:")
for i in Num_List:
    print(i)
print("Accessing the List Elements using for loop with indexing:")
# range(start,stop,stepsize),range(start,stop),range(stop  )
for i in range(len(Num_List)):
    print(Num_List[i])
#using while loop
print("Accessing the List Elements using while loop with indexing:")
i=0
while(i<len(Num_List)):
    print(Num_List[i])
    i+=1