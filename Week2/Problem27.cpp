#include<cstdio>
#include<cmath>

using namespace std;

double TargetFunction (double x);
double FalsePosition(double rangeMin, double rangeMax, double TOL, int maxIter);

main()
{
    double rangeMin = 0.000001;
    double rangeMax = 1.0;
    double TOL = 0.0000000001;
    int maxIter = 100;

    printf("FalsePosition ");
    printf("[%f, %f]\n", rangeMin, rangeMax);
    double ans = FalsePosition(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");

    printf("Maximal interest rate = %.12f * 12 = %.12f\n", ans, ans * 12.0);
}

double TargetFunction (double x)
{
    return (1000.0 / x) * (1 - pow(1 + x, -360)) - 135000;
}

double FalsePosition(double rangeMin, double rangeMax, double TOL, int maxIter)
{
    int currentIter = 2;
    double p0 = rangeMin;
    double p1 = rangeMax;
    double p;
    double q0 = TargetFunction(p0);
    double q1 = TargetFunction(p1);
    double q;

    while(currentIter <= maxIter)
    {
        p = p1 - ((q1 * (p1 - p0)) / (q1 - q0));
        printf("p%d = %.12f Error = %.12f f(%.12f) = %.12f\n", currentIter, p, abs(p - p1), TargetFunction(p));

        if(abs(p - p1) < TOL)
        {
            printf("Success with %d iterations. f(%.12f) = %.12f\n", currentIter, p, TargetFunction(p));
            if(p < rangeMin || p > rangeMax)
            {
                printf("But p%d is not in range [%f, %f]\n", currentIter, rangeMin, rangeMax);
            }
            return p;
        }

        currentIter++;
        q = TargetFunction(p);

        if(q * q1 < 0)
        {
            p0 = p1;
            q0 = q1;
        }

        p1 = p;
        q1 = q;
    }
    printf("Fail");
    return -1;
}
