def ternarySearch(A):
    lo = 0
    hi = len(A)-1
    while hi-lo >= 3:
        mid1 = (2*lo+hi)//3
        mid2 = (lo+2*hi)//3

        if A[mid1] >= A[mid2]:
            lo = mid1
        elif A[mid1] < A[mid2]:
            hi = mid2

    return min(A[lo:hi+1])