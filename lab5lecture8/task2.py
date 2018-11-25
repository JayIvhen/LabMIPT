"""
fibonacci numbers recursive
"""
fibo_hash = {}

def fibo(N):
    if N in fibo_hash.keys():
        return fibo_hash[N]
    if N == 1:
        fibo_hash.update([(N, 1)])
        return 1
    if N == 2:
        fibo_hash.update([(N, 1)])
        return 1
    res = fibo(N-1)+fibo(N-2)
    fibo_hash.update([(N, res)])
    return res

print(fibo(100))
