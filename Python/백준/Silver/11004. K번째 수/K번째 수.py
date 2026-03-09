N, K = map(int, input().split())
A = list(map(int, input().split()))

def get_pivot_idx(start, end):
    if start + 1 == end:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
        return end
    
    M = (start + end) // 2
    A[start], A[M] = A[M], A[start]
    
    pivot = A[start]
    
    i = start + 1
    j = end
    
    while i <= j:
        while i <= end and A[i] < pivot:
            i += 1
        
        while j >= start and A[j] > pivot:
            j -= 1
        
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    
    A[start] = A[j]
    A[j] = pivot
    return j

def sort(start, end):
    if start < end:
        pivot = get_pivot_idx(start, end)
        
        if pivot == K - 1:
            return
        elif pivot > K - 1:
            sort(start, pivot-1)
        else:
            sort(pivot+1, end)

sort(0, N-1)
print(A[K-1])