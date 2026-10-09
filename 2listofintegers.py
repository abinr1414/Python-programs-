list1=[1,2,3,4,5,6,7,8]
list2=[9,2,3,4,5,5,6,7]
if len(list1) == len(list2):
    print("the list are of same length")
if sum(list1)==sum(list2):
    print("the lists sums to same value")
else:
    print('the list sums to different value',
          'sum of list1 is ',sum(list1),
          'sum of list2 is ',sum(list2))

for num in list1:
    if num  in list2:
       print(num,'is in list1 and list2')
