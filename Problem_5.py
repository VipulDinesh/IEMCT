List = [[],[]]
Dict={}

for i in range(5):
    List[0].append(input(f"Enter name {i+1}:"))
for i in range(5):
    List[1].append(int(input(f"Enter number {i+1}:")))

List[0].sort()
List[1].sort()

for i in range(5):
    Dict[List[0][i]]=List[1][i]

print(Dict)