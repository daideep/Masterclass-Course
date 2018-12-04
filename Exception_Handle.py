
##def divide(x,y):
## 
##   z = x/y
##   return z
##
##divide(10,0)

#print('111111111111111111111111')

def divide(x,y):
 try:
   z = x/y
   return z
 except:
    print('There is a divide by zero error')
    return 0

x = float(input('Enter a number :'))
y = float(input('Enter value by which you want to divide the number :'))    
    
print(divide(x,y))


print('111111111111111111111111')


