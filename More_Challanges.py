
product = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
new_product = input("Enter The Product: ")

if(new_product in product):
    print(product.get(new_product))
else:
    print("product not Found")


print('-----------------------------------')


List = list(range(1,100,5))

for x in List:
    if x%2 == 1:
        print(x)


print('-----------------------------------')


