# We take range(11) since x,y,z <=10

for x in range(11):
    for y in range(11):
        for z in range(11):
            if x+y+z==10:
                print(f"x={x}, y={y}, z={z}")