a = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0}
b = {'+':0.3, '0':0.0, '-': -0.3}

score = 0
grade = input()
if grade != 'F':
    print(a[grade[0]] + b[grade[1]])
else:
    print(0.0)