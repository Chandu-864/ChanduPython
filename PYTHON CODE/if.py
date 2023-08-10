x=list(range(1,100))
even = 0
odd = 0
for y in x:
    if y%2==0:
        even = even + int(y)
    else:
        odd = odd + int(y)