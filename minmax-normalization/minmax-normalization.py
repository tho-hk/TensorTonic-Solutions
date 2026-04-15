import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    
    '''
    why need keepdims = True?
    if keepdims = False, np.max and np.min would treat
                  all arrays as a single flat array
                  and return a single global min
                  which is "1" rather than [1,2]
    '''
    X_max = np.max(X, axis, keepdims=True)
    X_min = np.min(X, axis, keepdims=True)
    denominator = X_max - X_min
    # there is a chance that X_max = X_min
    # which would lead to division with zero
    
    # this returns the larger of eps =! zero, or X_max - X_min
    denominator = np.maximum(denominator, eps)

    # now complete the min-max normalization
    x_pi = (X - X_min) / denominator

    return x_pi
    
        