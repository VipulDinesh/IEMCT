List =[]

for i in range(5):
    List.append(input(f"Enter name {i+1}:"))
    List[i]=List[i].split()  # Nested List, split at space
    List[i][0]=List[i][0].upper()  # First word in name capitalised
    str=List[i][0]  # Adding uppercase first word by default
    if len(List[i])>1:  # If name has a space
        for j in range(len(List[i])-1):
            str=str+List[i][j+1].lower()  # Trailing words appended in lowercase
    List[i]=str[:-2]  # Last two characters removed

List.sort()

for i in range(5):
    print(f"{i+1}. {List[i]}")