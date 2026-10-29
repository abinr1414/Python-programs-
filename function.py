def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        fact+1
    return(fact)


#main program

num=int(input("ENTER THE NUMBER TO FIND FACTORIAL:"))
fact=fact(num)
print("FACTORIAL IS:",fact)
