

I = 1

while I != 'q' :
    I = input('输入q退出,输入其他则继续：')
    if I == 'q':
        break
    

    X = int(input('第一个数：'))
    Y = input('运算符：')
    Z = int(input('第二个数：'))

    K = {'+':X+Z,
     '-':X-Z,
     '*':X*Z,
     '/':X/Z,
     '**':X**Z,
     '%':X%Z,
     }
    J = K.get(Y,'请输入+|-|*|/|**|%|')
    print(J)
