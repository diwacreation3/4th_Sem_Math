# Defining the function
def f(x):
    return x**3 - 5*x - 9

# Defining the derivative of the function
def g(x):
    return 3*x**2 - 5

# Implementing Newton-Raphson method
def newtonRaphson(x0, e, N):
    print('\n\n*** Newton-Raphson Method Implementation ***')
    step = 1
    flag = 1
    condition = True
    
    while condition:
        if g(x0) == 0.0:
            print('Divide by Zero error.')
            break
        
        # Calculate the next approximation
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        
        x0 = x1
        step += 1
        
        # Break if maximum iterations are exceeded
        if step > N:
            flag = 0
            break
        
        # Update the condition for convergence
        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input section
x0 = input('Enter initial guess: ')
e = input('Enter tolerable error: ')
N = input('Enter maximum iterations: ')

# Convert inputs to appropriate types
x0 = float(x0)
e = float(e)
N = int(N)

# Start Newton-Raphson method
newtonRaphson(x0, e, N)
