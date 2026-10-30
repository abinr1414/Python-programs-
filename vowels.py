
string=input("ENTER A STRING:")
vowels=['a','e','i','o','u']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
]
white_space=0
vowelss=0
consonantss=0

for i in string:
    if i in vowels:
       vowelss=vowelss+1
    if i in consonants:
        consonantss=consonantss+1
    if i == " ":
        white_space=white_space+1
        
print('vowels is',vowelss)
print("the consonents is ",consonantss)
print("white_space is ",white_space)

