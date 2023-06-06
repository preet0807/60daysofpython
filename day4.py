

l=[]
N = int(input())
for _ in range(N):
    
    # print(command)
    command, *values = input().split()

    if command=="insert":
         #unpacking 
        position=int(values[0])
        number=int(values[1])
        l.insert(position,number)
    elif command=="print":
        print(l)
    elif command=="remove":
        number=int (values[0])
        l.remove(number)
    elif command=="append":
        number=int(values[0])
        l.append(number)
    elif command=='sort':
        l.sort()
    elif command=='pop':
        l.pop()
    elif command=='reverse':
        l.reverse()
    



   
        
    
        
    
