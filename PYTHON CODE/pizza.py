def pizz():
    r = float(input("Enter a value for n: "))
    Area = 3.14*(r*r)
    print(Area)
    return Area
def cost(Area):
    co = float(input("Enter the cost of pizza in $: "))
    price = co/Area
    print(price)
pizza_area = pizz()
cost(pizza_area)