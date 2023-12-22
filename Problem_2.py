List =[]

for i in range(5):
    List.append(input(f"Enter name {i+1}:")) #Name input
    List[i]=List[i].split() #Nested List split at space
    List[i][0]=List[i][0].upper() #First name capitalised
    str=List[i][0]
    if len(List[i])>1:
        for j in range(len(List[i])-1):
            str=str+List[i][j+1].lower()
    List[i]=str[:-2]

List.sort()

for i in range(5):
    print(f"{i+1}. {List[i]}")