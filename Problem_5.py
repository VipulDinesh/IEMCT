List = [[],[]]
Dict={}

for i in range(5):
    List[0].append(input(f"Enter name {i+1}:")) #Name appended to first row of 2D array.
for i in range(5):
    List[1].append(int(input(f"Enter number {i+1}:"))) #Number appended to second row of 2D array.

List[0].sort()
List[1].sort()

for i in range(5):
    Dict[List[0][i]]=List[1][i] #2D array handling. i-th name assigned to i-th number.

print(Dict)