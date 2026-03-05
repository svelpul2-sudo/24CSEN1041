x,y=map(int,input().split())

for i in range(x,y+1):
    if i%3==0 and i%5==0:
        print("OHAH",end=" ")
    elif i%3==0:
        print("OH",end=" ")
    elif i%5==0:
        print("AH",end=" ")
    else:
        print(i,end=" ")
#output
1 2 OH 4 AH 7 8 OH 11 12 OHAH 14 
