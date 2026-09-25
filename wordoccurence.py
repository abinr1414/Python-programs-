words=list(input('enter the words:').split())
found=False
for i in set(words):#we use set for removing the duplicates 
    if words.count(i)>1:
        print(i ,'occurs',words.count(i),'times')
        found=True
if not found:
    print("Words are not repeating")