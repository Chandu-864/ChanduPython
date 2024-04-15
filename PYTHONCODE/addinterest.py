def addinterest(amount,rate):
    newbalance = amount*(1+rate)
    return newbalance
def test():
    amount=1000
    rate=0.5
    amount=addinterest(amount,rate)
    print(amount)
test()