#a = ['d', 'b', 'c', 'qwer']
#data = open('file.txt', 'a')
#data.writelines(a) # разделителей не будет
#data.write('\nLine123\n')
#data.close()

#path ='file.txt'
#data = open(path, 'r')
#for line in data:
#    print(line)
#data.close()
#exit()
#  Function

#import ser_1

#print(ser_1.f(1))

a = {1,2,3}
b = {1, 4, 5, 6}
c = a.difference(b)
k = b.difference(a)
print(c)
print(k)