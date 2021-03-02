# Enter your code here. Read input from STDIN. Print output to STDOUT



N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

def weighted_mean(X,W,N):
    
    sum_value = 0
    temp = 0
    
    for i in range(N):
        sum_value += X[i]*W[i]
        temp += W[i]
    
    answer = round(sum_value/temp, 1)
    
    return answer

print(weighted_mean(X,W,N))
