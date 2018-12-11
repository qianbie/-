#for循环实现1-100，所有数的总和
k = 0
for i1 in range(1,101):
    k += i1
print(k)

#计算100以内的3、5倍数的和

k = 0

for i2 in range(1,101):
    if i2%3 == 0:
        k += i2
    elif i2%5 == 0:
        k += i2
print(k)

#冰雹序列

BB = input ('输入你想要输入的数字')
BB = int (BB)
print(BB)
if BB == 1:
    print(BB)
else :
    while BB > 1:
        if BB %2 == 0:
            BB = int(BB/2)
            print(BB)
        else :
            BB = BB*3+1
            print(BB)

        
        
