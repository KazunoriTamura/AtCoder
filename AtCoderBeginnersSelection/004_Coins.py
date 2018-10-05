A = input()
B = input()
C = input()
X = input()
a = int(A)
b = int(B)
c = int(C)
x = int(X)

def check_balance(x,num,price):
    balance = num * price
    if x > balance:
        return 0
    else:
        return 1

def compute_about_B(x,b,c):
    count = 0
    if x == 0:
        count = 1
    else:
        b_max = x//100
        if b_max <= b:
            for i in range(b_max+1):
                x_new = x - 100*i
                count = count + check_balance(x_new,c,50)
        else:
            for i in range(b+1):
                x_new = x - 100*i
                count = count + check_balance(x_new,c,50)
    return count
    
def compute_about_A(x,a,b,c):
        answer = 0
        a_max = x//500 + 1
        if a_max <= a: 
            for i in range(a_max+1):
                x_new = x - 500*i
                answer = answer + compute_about_B(x_new,b,c)
        else:
            for i in range(a+1):
                x_new = x - 500*i
                answer = answer + compute_about_B(x_new,b,c)  
        return answer

answer = compute_about_A(x,a,b,c)
print(answer)