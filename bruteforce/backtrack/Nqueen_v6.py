n = int(input())
L = [i for i in range(n)]
cnt = 0

def promising(subset,index,i):
    for j in range(index):
        if subset[j] == i or subset[j]+j == i+index or subset[j]-j == i-index:
            return False
    return True

def placequeen(subset,index):
    global cnt

    if index >= n:
        cnt += 1
        return

    for i in range(n):
        if promising(subset,index,i):
            placequeen(subset+[i], index+1)

placequeen([],0)
print(cnt)

#https://chanhuiseok.github.io/posts/baek-1/