def rabin_karp_matcher(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1, q)
    print("Hash Value:",h)
    p = 0
    t0 = 0
    spurious_hits = 0
    
    # Preprocessing
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t0 = (d * t0 + ord(T[i])) % q
    
    for s in range(n - m + 1):
        if p == t0:
            if P == T[s:s+m]:
                print("Pattern occurs with shift", s)
            else:
                spurious_hits += 1
        
        if s < n - m:
            t_next = (d * (t0 - ord(T[s]) * h) + ord(T[s + m])) % q
            t0 = t_next
    
    return spurious_hits

def count_spurious_hits(T, P, d, q):
    return rabin_karp_matcher(T, P, d, q)

# Taking user input
T = input("Enter the text: ")
P = input("Enter the pattern: ")
d = int(input("Enter the Radix value: ")) # number of characters in the input alphabet
q = int(input("Enter a Suitable prime no: "))

spurious_hits = count_spurious_hits(T, P, d, q)
print("Number of spurious hits:", spurious_hits)
