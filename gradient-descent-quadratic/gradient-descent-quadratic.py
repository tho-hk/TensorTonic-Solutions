def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = float(x0)
    for i in range(steps): # run gradient descent "steps" number of times
        # obtain gradient
        # which is derivative of f(x) = ax^2 + bx + c:
        # f(x)' = 2ax + b
        gradient = 2 * a * x + b
        x = x - lr * gradient # x has been updated
                              # direction can be +ve or -ve  

    return float(x)