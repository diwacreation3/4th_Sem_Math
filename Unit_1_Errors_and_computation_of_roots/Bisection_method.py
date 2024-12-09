# Defining function
def f(x):
    return x**3 - 5*x - 9

# Implementing bisection method
def bisection(x0, x1, e):
    if f(x0) * f(x1) > 0.0:
        print("Given guess values do not bracket the root.")
        print("Try again with different guess values.")
        return None
    
    print("\n\n*** BISECTION METHOD IMPLEMENTATION ***")
    step = 1
    condition = True
    while condition:
        x2 = (x0 + x1) / 2
        print(f"Iteration-{step}, x2 = {x2:.6f}, f(x2) = {f(x2):.6f}")
        
        # Check if the root lies in the left or right half
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step += 1
        condition = abs(f(x2)) > e  # Check if the error tolerance is met

    print(f"\nRequired root is: {x2:.8f}")
    return x2

# Input section
x0 = float(input("First guess: "))
x1 = float(input("Second guess: "))
e = float(input("Tolerable error: "))

# Call bisection method
bisection(x0, x1, e)
