
#s = input().strip()
s = "Hello WorlD"
count = 0
for i in s:
    if i.isupper():
        count = count + 1
print(count)

print('----------------------')

for a in range(5):
    print("I am Programmer")


print('----------------------')


def square():
  for x in range(1,10):
     print (x**2)
square()


print('------------------------')


square = lambda x : x**2
print(square(4))

result = lambda x,y,z : x+y+z
print(result(4,5,6))


print('------------------------')


def add(x,y):
    return x+y

def square(c):
    return c**2

result = square(add(2,3))
print(result)


print('------------------------')

def BMI(Height,Weight):

    BMI = (Weight)/(Height)**2

    return BMI

print(BMI(5.3,60))


print('------------------------')


Height = float(input("Enter Height Value: "))
Weight = float(input("Enter Weight Value: "))

def BMI(Height,Weight):

    BMI = (Weight)/pow(Height,2)

    return BMI

print (BMI(Height,Weight))
