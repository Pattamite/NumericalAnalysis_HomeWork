#include<cstdio>
#include<cmath>

using namespace std;

double TargetFunction (double x);
double TargetFunctionDerivative (double x);
void FalsePosition(double rangeMin, double rangeMax, double TOL, int maxIter);
void Secant(double rangeMin, double rangeMax, double TOL, int maxIter);
void Newton(double rangeMin, double rangeMax, double TOL, int maxIter);

main()
{
    double rangeMin = -1.0;
    double rangeMax = 0.0;
    double TOL = 0.000001;
    int maxIter = 100;

    printf("FalsePosition ");
    printf("[%f, %f]\n", rangeMin, rangeMax);
    FalsePosition(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");

    printf("Secant ");
    printf("[%f, %f]\n", rangeMin, rangeMax);
    Secant(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");

    printf("Newton ");
    printf("%f\n", (rangeMin + rangeMax) / 2.0);
    Newton(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");

    printf("------------------------------------------------------------------------\n\n");

    rangeMin = 0.0;
    rangeMax = 1.0;

    printf("FalsePosition ");
    printf("[%f, %f]\n", rangeMin, rangeMax);
    FalsePosition(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");

    printf("Secant ");
    printf("[%f, %f]\n", rangeMin, rangeMax);
    Secant(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");

    printf("Newton ");
    printf("%f\n", (rangeMin + rangeMax) / 2.0);
    Newton(rangeMin, rangeMax, TOL, maxIter);
    printf("\n");
}

double TargetFunction (double x)
{
    return (230.0 * pow(x, 4.0)) + (18.0 * pow(x, 3.0)) + (9.0 * pow(x, 2.0)) - (221.0 * x) - 9;
}

double TargetFunctionDerivative (double x)
{
    return (920.0 * pow(x, 3.0)) + (54.0 * pow(x, 2.0)) + (18.0 * x) - (221.0);
}

void FalsePosition(double rangeMin, double rangeMax, double TOL, int maxIter)
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
        printf("p%d = %.8f Error = %.8f\n", currentIter, p, abs(p - p1));

        if(abs(p - p1) < TOL)
        {
            printf("Success with %d iterations. f(%.8f) = %.8f\n", currentIter, p, TargetFunction(p));
            if(p < rangeMin || p > rangeMax)
            {
                printf("But p%d is not in range [%f, %f]\n", currentIter, rangeMin, rangeMax);
            }
            return;
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
}

void Secant(double rangeMin, double rangeMax, double TOL, int maxIter)
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
        printf("p%d = %.8f Error = %.8f\n", currentIter, p, abs(p - p1));

        if(abs(p - p1) < TOL)
        {
            printf("Success with %d iterations. f(%.8f) = %.8f\n", currentIter, p, TargetFunction(p));
            if(p < rangeMin || p > rangeMax)
            {
                printf("But p%d is not in range [%f, %f]\n", currentIter, rangeMin, rangeMax);
            }
            return;
        }

        currentIter++;
        q = TargetFunction(p);

        p0 = p1;
        q0 = q1;
        p1 = p;
        q1 = q;
    }
    printf("Fail");
}

void Newton(double rangeMin, double rangeMax, double TOL, int maxIter)
{
    int currentIter = 0;
    double p0 = (rangeMin + rangeMax) / 2.0;
    double p;

    while(currentIter <= maxIter)
    {
        if(TargetFunctionDerivative(p0) == 0)
        {
            printf("Fail");
            return;
        }

        p = p0 - (TargetFunction(p0) / TargetFunctionDerivative(p0));

        printf("p%d = %.8f Error = %.8f\n", currentIter, p, abs(p - p0));

        if(abs(p - p0) < TOL)
        {
            printf("Success with %d iterations. f(%.8f) = %.8f\n", currentIter, p, TargetFunction(p));
            if(p < rangeMin || p > rangeMax)
            {
                printf("But p%d is not in range [%f, %f]\n", currentIter, rangeMin, rangeMax);
            }
            return;
        }

        currentIter++;
        p0 = p;
    }
    printf("Fail");
}
