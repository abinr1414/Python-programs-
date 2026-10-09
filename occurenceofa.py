names=list(input('enter the names:').split())

count=0 
for name in names:
   count+=name.count('a')
print(names)

print('occurences of a',count)
