hours=int(input())

if hours<=8:
    salary=hours*200
else:
    salary=(8*200)+(hours-8)*300

tax=0
if salary>5000:
    tax=salary*0.05

net=salary-tax

print(salary,tax,net)
#output
| Hours | Salary | Tax | Net  |
| ----- | ------ | --- | ---- |
| 6     | 1200   | 0   | 1200 |
| 8     | 1600   | 0   | 1600 |
| 10    | 3400   | 0   | 3400 |
| 30    | 6640   | 332 | 6308 |
