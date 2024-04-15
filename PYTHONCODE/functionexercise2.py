def sphereArea():
    
    radius=float(input("enter a value:"))

    while radius > 0:
        area = (4)*(3.14)*(radius*radius)
        print(area)
        radius=float(input("enter a value:"))

def sphereVolume():
    radius=float(input("enter a value:"))
    volume= (4/3)*(3.14)*(radius*radius*radius)
    print(volume)


sphereArea()
sphereVolume()