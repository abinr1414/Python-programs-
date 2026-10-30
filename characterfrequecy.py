string=input("ENTER A STRING:")


for i in string:
    count=0
    for j in string:
         if i==j:
          count=count+1
    print(i,"=",count)
    
        

