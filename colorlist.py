list1=set(["red","black","blue","orange","indigo"])
list2=set(["green","blue","red"])
difference=[]
for color in list1:
    if color not in list2:
       difference.append(color)
print(difference)
       