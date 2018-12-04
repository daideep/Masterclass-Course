

file = open('demo.txt','w')

r = file.write('hiiiii i m fine\n')

file.close()


file = open('demo.txt','r')

print(file.read())

file.close()


file = open('demo.txt','a')

file.write('second line')

file.close()
