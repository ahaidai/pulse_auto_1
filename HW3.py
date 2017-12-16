#1
ustr1 = input()
print(
    '\n'
    #1.1
    ,ustr1[2:3]
    #1.2
    ,ustr1[len(ustr1)-2:len(ustr1)-3:-1]
    #1.3
    ,ustr1[0:5]
    #1.4
    ,ustr1[0:len(ustr1)-2]
    #1.5
    ,ustr1[0::2]
    #1.6
    ,ustr1[1::2]
    #1.7
    ,ustr1[::-1]
    #1.8
    ,ustr1[::-2]
    #1.9
    ,len(ustr1)
    #separator
    ,sep = '\n'
)



#2
ustr2 = input()

if len(ustr2) % 2 != 0:
    ustr2_1 = ustr2[:len(ustr2)//2+1]
    ustr2_2 = ustr2[len(ustr2)//2+1::1]
else:
    ustr2_1 = ustr2[:len(ustr2)//2]
    ustr2_2 = ustr2[len(ustr2)//2::1]

ustr2f = ustr2_2 + ustr2_1

print(ustr2f)



#3.1
i = 0
while i <= 10:
    print(i)
    i +=1

#3.2
i=20
while i >=1:
    print(i)
    i -= 1



#4.1
yrl = [1,2,3,4,5.55,6.77,-8,9.001]
while len(yrl)>0:
    print(yrl[0])
    yrl.remove(yrl[0])



#4.2
yrstr = 'Hello World!'
while len(yrstr)>0:
    print(yrstr[0])
    yrstr = yrstr[1:]



#4.3
yrlst = [1,2,3,4,5.55,-6.77,-8,9.001]
while len(yrlst)>0:
    yrlst.sort()
    print(yrlst[0])
    yrl.remove(yrlst[0])



#5
ustr3 = 'We are not what we should be!\nWe are not what we need to be.\nBut at least we are not what we used to be\n(Football Coach)'
#5.1
lstr = ustr3.split()
print(len(lstr))



#6.1
def is_year_leap(y):
    y = int(y)
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False

print(is_year_leap(2000))



#6.2
def is_this_triangle(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a+b > c and a+c > b and c+b > a and a > 0 and b > 0 and c > 0:
        return True
    else:
        return False

print(is_this_triangle(3,4,5))



#7
def is_this_triangle_and_what(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a+b > c and a+c > b and c+b > a and a > 0 and b > 0 and c > 0:
        if a == b != c or b == c != a or c == a != b:
            return 'Isosceles Triangle'
        elif a == b == c:
            return 'Equilateral Triangle'
        else:
            return 'Versatile Triangle'
    else:
        return 'Not a Triangle'

print(is_this_triangle_and_what(3,3,99))



#8
def lalasong(a = 3, b = 3, c = 0):
    lastr = 'la-' * b
    lastr = lastr[:len(lastr)-1] + ' \n'
    if c == 0:
        lastrl = lastr[:len(lastr) - 1] + '.'
    elif c == 1:
        lastrl = lastr[:len(lastr) - 1] + '!'
    lastrf = ''
    while a > 0:
        if a != 1:
            lastrf += lastr
        else:
            lastrf = lastrf + lastrl
        a -= 1
    return lastrf

print(lalasong(2,7,1))