selling_price = 100


def student_discount(price):
    price = price - (price * 10) / 100
    return price
 
def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice
 
#applying both discounts simultaneously
 
print(additional_discount(student_discount(selling_price)))


print('--------------------------------')


Result = lambda x: x*(x+5)**2
print(Result(2))


print('--------------------------------')


def discount(price):
    price = price - (price*10) / 100
    return price

product = [10,20,25,30,50]

print(list(map(discount,product)))


print('--------------------------------')

















