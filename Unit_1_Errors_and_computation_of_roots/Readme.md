# Errors and Computation of Roots

1. C++ Source code: Regula Falsi method
C++ implementation for false position method 

```c++

#include <iostream>
#include<iomanip>
#include <math.h>

/* 
define equation to be solved.
Change this equation to solve 
*/

#define f(x) cos(x) - x * exp(x)

using namespace std;

int main(){
    // Declaring required variable 
    float x, x0, x1, f0, f1, f, e;
    int step = 1;


    /*
    Setting precision and writing floating point values in fixed notation 
    */
   cout << setprecision(6) << fixed;

   // inputs 
   cout << "Enter first guess : ";
   cin >> x0;
   cout << "Enter second guess : ";
   cin >> x1;
   cout << "Enter tolerable error : ";
   cin >> e;

   // Calculating functional value 
   f0 = f(x0);
   f1 = f(x1);

   // Checking whether given gusses brackets the roor or not 
   if (f0 * f1 > 0.0)
   {
    cout << "Incorrest Initial gusses " << endl ;
    
   }

   // Implementing False position method 
   cout << endl<<  "***************************" << endl;
   cout << "False position Method" << endl;
   cout << "********************************" << endl;

   do
   {
    // Applying false Position Method 
    // x is next approxinated root using false position method 

    x = x0 - (x0-x1) * f0 / (f0-f1);
    f = f(x);

    cout << "Iteration-" << step << ":\t x = " << setw(10) << x  << " and f(x) = " << setw(10) << f(x) << endl;

    if(f0 * f < 0)
    {
        x1 = x;
        f1 = f;
    }
    else{
        x0 = x;
        f0 = f;
    }

    step = step + 1;
   } while(fabs(f) > e);
   cout << endl << "Root is: " << x << endl;


}
```
# Newton rapson Method

```py
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

```



