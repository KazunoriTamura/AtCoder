S = str(input())
# print(S)

# print(d1)
# print(S[0,5])

# if S[0:5] == d1:
#     print('OK')
# else:
#     print('NO')

def check_and_erase_head(s):
    # print('-------')
    d1 = 'dream'
    d2 = 'dreamer'
    e1 = 'erase'
    e2 = 'eraser'
    f = 0
    l = len(s)
    # print(l)
    if l == 0:
        f = 2
    elif 0 < l <  5:
        f = 0
    elif l == 5:
        if s[0:5] == d1:
            f = 1
            s = s[5:]
        elif s[0:5] == e1:
            f = 1
            s = s[5:]
    elif l == 6:
        if s[0:5] == d1 and s[5]!='e':
            f = 1
            s = s[5:]
        elif s[0:5] == e1 and s[5]!='r':
            f = 1
            s = s[5:]
        elif s[0:6] == e2:
            f = 1
            s = s[6:]
            # print('6,e2')
    elif l == 7:
        if s[0:5] == d1 and s[5]!='e' and s[6]!='r':
            f = 1
            s = s[5:]
        elif s[0:7] == d2:
            f = 1
            s = s[7:]
        elif s[0:5] == e1 and s[5]!='r':
            f = 1
            s = s[5:]
        elif s[0:6] == e2:
            f = 1
            s = s[6:]
    elif l > 7:
        if s[0:5] == d1 and s[5:7]!='er' and s[7]!='a':
            f = 1
            s = s[5:]
            # print('8,d1')
        elif s[0:5] == d1 and s[5:8]=='era':
            f = 1
            s = s[5:]
        elif s[0:7] == d2 and s[7]!='a':
            f = 1
            s = s[7:]
        elif s[0:5] == e1 and s[5]!='r':
            f = 1
            s = s[5:]
        elif s[0:6] == e2:
            f = 1
            s = s[6:]
    
    # print(f,s)
    return f,s

flag = 1
while flag == 1:
    flag,S = check_and_erase_head(S)

if flag == 1 or flag == 2:
    print('YES')
else:
    print('NO')