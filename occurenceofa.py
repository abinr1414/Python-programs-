names=list(input('enter the names:').split())
found=False 
for name in names:
    if name.startswith("a"):
        print(name)
        found=True
if not found:
    print('names not found')
