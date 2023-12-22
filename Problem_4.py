#Assuming start and end are inclusive for Prime Search

a=int(input("Enter a positive start number: "))
b=int(input("Enter a positive end number: "))

for i in range(a,b+1):
    prime=True
    if i==1:
        continue
    elif i==2 or i==3: #Because GIF of sqrt of 2 or 3 is 1, but division range starts from 2
        pass
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=False
                break
    if prime:
        print(i, end=" ")