"""
Name: Abd Al-rahman Ahmed Mohammed Mahmoud
ID: 20211048
"""

import math

def poly_value(polynomial_terms, x):
    """
    Calculates the value of a polynomial P(x) at a specific point x.
    
    Args:
        polynomial_terms (list of tuples): Each tuple contains (coefficientficient, power).
        x (float): The value at which the polynomial is evaluated.
    
    Returns:
        float: Result of P(x).
    """
    return sum(float(coefficient) * (float(x) ** float(power)) for coefficient, power in polynomial_terms)

def differentiation(polynomial_terms, x):
    """
    Calculates the derivative P'(x) of a polynomial at a given point x.
    
    Args:
        polynomial_terms (list of tuples): Each tuple contains (coefficientficient, power).
        x (float): The value at which the derivative is evaluated.
    
    Returns:
        float: Result of P'(x).
    """
    return sum(float(coefficient) * float(power) * (float(x) ** (float(power) - 1))
               for coefficient, power in polynomial_terms if float(power) != 0)

def get_polynomial_terms():
    """
    Prompts the user to input the polynomial terms.
    
    Returns:
        list of tuples: Polynomial represented as a list of (coefficientficient, power).
    """
    try:
        num_terms = int(input("Enter the number of terms in the polynomial: "))
        if num_terms <= 0:
            raise ValueError("Number of terms must be positive.")
    except ValueError as e:
        print(f"[Error] {e}")
        return None

    print("\nEnter each term as coefficientficient and power:")
    terms = []
    for i in range(1, num_terms + 1):
        while True:
            try:
                coefficient = float(input(f"  coefficientficient for term {i}: "))
                power = float(input(f"  Power       for term {i}: "))
                terms.append((coefficient, power))
                break
            except ValueError:
                print("[Error] Please enter numeric values only.")
        print("-" * 10)
    return terms

def get_interval():
    """
    Prompts the user to input an interval [a, b].

    Returns:
        list: [start, end] as floats.
    """
    try:
        a = float(input("Enter the start of the interval: "))
        b = float(input("Enter the end of the interval: "))
        return [a, b]
    except ValueError:
        print("[Error] Please enter valid numeric bounds.")
        return None

def newton(polynomial_terms, interval):
    """
    Applies Newton method to approximate a root of the polynomial.

    Args:
        polynomial_terms (list of tuples): Polynomial definition.
        interval (list of float): [a, b] interval.
    """
    MAX_ITER = 20
    while True:
        try:
            TOL = int(input("\nEnter desired accuracy (e.g., enter 6 for 10^-6): "))
            if TOL <= 0:
                print("  [Error] Precision must be a positive integer.")
            else:
                break
        except ValueError:
            print("  [Warning] Please enter a valid integer.")

    TOL = 10 ** -TOL

    a, b = interval
    f_a, f_b = poly_value(polynomial_terms, a), poly_value(polynomial_terms, b)

    print(f"\nP({a:.3f}) = {f_a:.6f}")
    print(f"P({b:.3f}) = {f_b:.6f}")

    if f_a * f_b >= 0:
        print("\n[Warning] The function does not change sign on the interval.")
        print("Newton method may not converge.")
        return

    print("\n[Info] A sign change is detected. A root likely exists in the interval.")
    
    p = (a + b) / 2

    print("\nStarting Newton Iterations")
    print("-" * 40)
    print(f"Iteration 0: P = {p:.6f}")

    for i in range(1, MAX_ITER + 1):
        f_p = poly_value(polynomial_terms, p)
        f_prime_p = differentiation(polynomial_terms, p)

        if abs(f_prime_p) < 1e-10:
            print(f"\n[Stopped] Iteration {i}: Derivative is too small (≈ 0).")
            print(f"P'({p:.6f}) = {f_prime_p:.6f}")
            return

        p_next = p - (f_p / f_prime_p)

        print(f"Iteration {i}: P = {p_next:.6f} | f(P) = {f_p:.6f} | f'(P) = {f_prime_p:.6f}")

        if abs(p_next - p) <= TOL:
            print(f"\n=>after {i} iterations.")
            print(f"root: {p_next:.6f}")
            return

        p = p_next

def solve():
    """
    The main driver function to handle input, validate data, and run the root solver.
    """
    print("=" * 45)
    print("         Newton Root Finder")
    print("=" * 45)

    polynomial_terms = get_polynomial_terms()
    if polynomial_terms is None:
        return

    interval = get_interval()
    if interval is None:
        return

    newton(polynomial_terms, interval)

if __name__ == "__main__":
    solve()
