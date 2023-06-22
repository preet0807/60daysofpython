arr={}
lst=[]
n=int(input("enter the size of your array"))
d=int(input("enter the number you would like to search"))
for i in range(0,n):
    m=int(input())
    lst.append(m)
for i in lst:
    if lst[i]==d:
        print(i)

