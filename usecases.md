# Usecases

## Table of Content
0. [README](README.md)
1. [Usecases](usecases.md)
    - [Numerical Integration](#numerical-integration)
    - [Linear Systems Solvers](#linear-systems-solvers)
    - [Matrix Decomposition](#matrix-decomposition)
    - [Polynomial Interpolation](#polynomial-interpolation)
    - [Polynomial Evaluation](#polynomial-evaluation)
    - [Polynomial Approximation](#polynomial-approximation)
    - [Root Finding](#root-finding)
    - [ODE Solvers](#ode-solvers)
    - [Nonlinear Regression](#nonlinear-regression)

---

## Numerical Integration

- [MidpointRule](methods.md#midpointrule)  
  Use for a simple and fast estimate of definite integrals, especially when the function is smooth and you want a quick, reasonably accurate result. Works best for functions without sharp changes over the interval.

- [Simpson](methods.md#simpson)  
  Use for higher accuracy on smooth functions, especially polynomials up to degree three. Requires an even number of subintervals.

- [SimpsonUniversal](methods.md#simpson_universal)  
  Use when you want adaptive Simpson integration without manually choosing the number of subintervals.

---

## Linear Systems Solvers

- [Gauss](methods.md#gauss)  
  Use for small to medium-sized, well-conditioned linear systems where you don’t expect zeros or very small numbers on the diagonal. It’s a direct method.

- [GaussPivot](methods.md#gaussspivot)  
  Use when your system might have zeros or very small values on the diagonal, or if you want better numerical stability.

- [GaussSeidel](methods.md#gausssiedel)  
  Use for large, sparse, or diagonally dominant systems. Often converges faster than Jacobi.

- [Jacobi](methods.md#jacobi)  
  Use for large, sparse, or diagonally dominant systems, especially if you want a simple, parallelizable iterative method.

---

## Matrix Decomposition

- [GaussLU](methods.md#gausslu)  
  Use when you want to perform LU decomposition using Gaussian elimination and return a new matrix containing both L and U factors, leaving the original matrix unchanged.

---

## Polynomial Interpolation

- [Lagrange](methods.md#lagrange)  
  Use for a straightforward, formula-based approach to interpolation. Good for small datasets.

- [NewtonInterpolation](methods.md#newtoninterpolation)  
  Use when you want efficient, incremental interpolation—especially if you may add new data points later.

- [Valdemort](methods.md#voldemort)  
  Experimental / alternative interpolation method.

---

## Polynomial Evaluation

- [Horner](methods.md#horner)  
  Use for fast and numerically stable evaluation of polynomials in standard (power) form.

- [NewtonEvaluation](methods.md#newtoneval)  
  Use for efficient evaluation of polynomials in Newton’s form.

---

## Polynomial Approximation

- [Least Squares Approximation (MNC)](methods.md#mnc)  
  Use when you want to fit a polynomial or linear model to noisy or overdetermined data using the least squares method.

- [Least Squares Approximation – simplified (MNCsmall)](methods.md#mncsmall)  
  Use for small datasets or simplified least squares demonstrations.

---

## Root Finding

- [Bisection](methods.md#bisekce)  
  Use when you need to find a root of a continuous function in a known interval where the function changes sign. Guarantees convergence.

- [NewtonRoot](methods.md#newtonroot)  
  Use when the function is differentiable and a good initial guess is available.

---

## ODE Solvers

- [Euler](methods.md#euler)  
  Use for numerically solving ordinary differential equations (ODEs) of the form  
  \( y' = f(x, y) \). Simple and fast, suitable for low-accuracy requirements.

---

## Nonlinear Regression

- [Nonlinear Regression](methods.md#nlinearni_regrese)  
  Use when fitting nonlinear models to experimental data for parameter estimation in physics, biology, or engineering.
