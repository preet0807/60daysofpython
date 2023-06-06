# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
tupleval=()

    
elements= input().split()
tupleval=tuple(map(int,elements))
hashval=hash(tupleval)
print(hashval)