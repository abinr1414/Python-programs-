list=list(map(int,input("enter the list of numbers that contain even numbers:").split()))
for num in list:
    if num%2==0:
        list.remove(num)
print("list after removal is:",list)