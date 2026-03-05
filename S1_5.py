emp=[[1,'lalith','12-12-2000',25000,'banking'],
     [2,'raju','02-05-2001',50000,'sales'],
     [3,'sita','15-08-1999',45000,'sales']]

print("Sales:")
for i in emp:
    if i[4]=="sales":
        print(i[1])

high=max(emp,key=lambda x:x[3])
print("Highest paid:",high[1])
#output
Sales:
raju
sita
Highest paid: raju
