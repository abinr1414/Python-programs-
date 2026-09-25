string=input('enter a string:')
if len(string)<=1:
    print("string is too small")
else:
    new_string=string[-1]+string[1:-1]+string[0]
    print(new_string)