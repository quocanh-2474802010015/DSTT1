from sympy import Matrix, symbols, simplify

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def verify_fib_matrix(k):
    F = Matrix([[1, 1], [1, 0]])
    Fk = F**k
    
    fibs = fibonacci(k+1)
    F_expected = Matrix([
        [fibs[k+1], fibs[k]],
        [fibs[k],   fibs[k-1]]
    ])
    
    is_equal = simplify(Fk - F_expected) == Matrix([[0, 0], [0, 0]])
    
    print(f"F^{k} =\n{Fk}")
    print(f"Expected matrix from Fibonacci numbers:\n{F_expected}")
    print(f"✅ Is the formula correct for k = {k}? --> {is_equal}")

# Ví dụ kiểm tra với k = 5
verify_fib_matrix(5)
