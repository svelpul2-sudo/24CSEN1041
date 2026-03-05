first_names=["Anil","Priya","Rahul","Sneha"]
last_names=("Kumar","Reddy","Sharma","Verma")

result=[f+" "+l for f,l in zip(first_names,last_names)]

print(result)
#output
['Anil Kumar', 'Priya Reddy', 'Rahul Sharma', 'Sneha Verma']
