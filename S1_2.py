m1,m2,m3=map(int,input().split())

avg=(m1+m2+m3)/3

if avg>=90:
    grade="O"
elif avg>=80:
    grade="A+"
elif avg>=70:
    grade="A"
elif avg>=60:
    grade="B+"
elif avg>=50:
    grade="B"
elif avg>=45:
    grade="C"
elif avg>=40:
    grade="P"
else:
    grade="F"

print("Average is:",round(avg,2))
print("Grade is",grade)
#output
Average is: 85.0
Grade is A+
