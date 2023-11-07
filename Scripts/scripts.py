import sympy

def analyze_complexity(expression):
    n = sympy.Symbol('n')
    complexity = sympy.simplify(expression)

    if complexity.is_polynomial(n):
        degree = sympy.degree(complexity, n)
        if degree == 0:
            return "O(1)"
        elif degree == 1:
            return "O(n)"
        else:
            return f"O(n^{degree})"
    elif complexity.is_exponential(n):
        return "O(2^n)"
    elif complexity.is_logarithmic(n):
        return "O(log(n))"
    else:
        return "Complex or unknown complexity"

# Example usage:
expression = 2 * n**2 + 3 * n + 1
print(analyze_complexity(expression))
