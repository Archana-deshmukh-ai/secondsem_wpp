import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x - 9  

def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    
    iterations = []
    for _ in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        
        if abs(f(c)) < tol:
            break
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return np.array(iterations)

def find_initial_interval(f, lower=-10, upper=10, step=0.5):
    x_vals = np.arange(lower, upper, step)
    for i in range(len(x_vals) - 1):
        if f(x_vals[i]) * f(x_vals[i+1]) < 0:
            return x_vals[i], x_vals[i+1]
    raise ValueError("No valid interval found.")

def plot_root_finding(iterations):
    plt.plot(iterations, 'bo-', label='Midpoints')
    plt.axhline(iterations[-1], color='r', linestyle='--', label=f'Root ≈ {iterations[-1]:.5f}')
    plt.xlabel("Iteration")
    plt.ylabel("Midpoint Value")
    plt.title("Bisection Method Root Finding")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    a, b = find_initial_interval(f)
    iterations = bisection_method(f, a, b)
    print("Root approximations:", iterations)
    plot_root_finding(iterations)

if __name__ == "__main__":
    main()
