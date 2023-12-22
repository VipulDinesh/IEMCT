n=10
#i=1

for x in range(n):
    for y in range(n):
        for z in range(n):
            if x+y+z==n:
                print(f"x={x}, y={y}, z={z}")
                #print(f"{i}. x={x}, y={y}, z={z}")
                #i=i+1