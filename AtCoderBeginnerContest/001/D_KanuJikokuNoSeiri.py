N = int(input())
S = []
S = [input() for i in range(N)]

def marume(se_list):
    s_last = int(se_list[3])
    if 0 <= s_last < 5:
        se_list[3] = '0'
    elif 5 <= s_last < 10:
        se_list[3] =  '5'
    e_last = int(se_list[8])
    e_last_2 = int(se_list[7])
    e_last_3 = int(se_list[6])
    if e_last == 0:
        se_list[8] = '0'
    elif 0 < e_last <= 5:
        se_list[8] = '5'
    elif 5 < e_last < 10:
        if e_last_2 == 5:
            se_list[8] = '0'
            se_list[7] = '0'
            if e_last_3 == 9:
                se_list[6] = '0'
                se_list[5] = str( int(se_list[5]) + 1 )
            elif e_last_3 != 9:
                se_list[6] = str( int(se_list[6]) + 1 )
        elif e_last_2 != 5:
            se_list[8] = '0'
            se_list[7] = str( int(se_list[7]) + 1 )         
    return se_list

for i in range(N):
    se = S[i]
    se_list = [ i for i in list(se) ]
    se_list = marume(se_list)
    se_new = ''.join(se_list)
    S[i] = se_new

S.sort()
N = len(S)

count = 0
for i in range(N-1):
    e = int(S[i][5:9])
    s = int(S[i+1][0:4])
    if s <= e:
        if e <= int(S[i+1][5:9]):
            S[i+1] = S[i][0:4] + '-' + S[i+1][5:9]
            S[i] = ''
            count += 1
        elif e > int(S[i+1][5:9]):
            S[i+1] = S[i][0:9]
            S[i] = ''
            count += 1

while count > 0:
    S.remove('')
    count -= 1

S = list(set(S))
S.sort()
N = len(S)

for i in range(N-1):
    print(S[i])
print(S[N-1])