# Assuming start and end are inclusive for Prime Search

a=int(input("Enter a positive start number: "))
b=int(input("Enter a positive end number: "))

for i in range(a,b+1):  # b+1 since last number is not included in range
    prime=True
    if i==1:
        continue  # 1 is neither prime, nor consonant, ignored
    elif i==2 or i==3:  # floor of sqrt(2) and sqrt(3) are 1. Edge case-handling.
        pass  # Both 2 and 3 are prime => passed means prime stays True
    else:
        # Divisibility needs to be checked only till the sqrt for prime
        # int acts like floor function
        # i%1 will always give 0, hence starting from 2 not 1. Edge case-handling done above.
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime=False
                break

    if prime:  # prime will be false iff the number is divisible by a number less than its sqrt
        print(i, end=" ")