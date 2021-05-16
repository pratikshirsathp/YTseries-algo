def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    
    while m % n !=0:
        (m,n)= (n,m%n)
        #or just use recursion
        gcd(n,m%n)
    
    return n


print(gcd(14,63))    
