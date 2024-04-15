def addinterest(amount,rate):
    for i in range(len(amount)):
        amount[i]=amount[i]*(1+rate)
def test():
    amount=[1000, 2200, 800, 360]
    rate=0.05
    addinterest(amount,rate)
    print(amount)
test()