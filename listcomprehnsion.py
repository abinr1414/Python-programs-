

list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
positive_list=[]
square=[]
for num in list:
    if num%2==0:
        positive_list.append(num)
print("positive_list",positive_list)

for num in list:
    squares=num*num
    square.append(squares)
print("square of n number is:",square)

word=input("enter a word:")
vowels=['a','e','i','o','u']
found=False
for i in word:
    if i in vowels:
     print(i,'is a vowel')
     found=True
if not found:
       print("there are no vowels in the",word)


ordinal_value=[]
for i in word:
    ordinal=ord(i)
    ordinal_value.append(ordinal)
print('ordinal value is',ordinal_value)