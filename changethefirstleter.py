str=input("enter the string:")
first=str[0]
changed_string=first
for i in str[1:]:
    if i == first:
        changed_string += '$'
    else:
        changed_string += i

print(changed_string)    
