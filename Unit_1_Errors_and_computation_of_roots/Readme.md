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




