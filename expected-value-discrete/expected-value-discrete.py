import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    
    if not np.allclose(np.sum(p), 1.0, atol=1e-06):
        # np.allclose returns a boolean that compares 2 arrays element-wise
        # numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
        # a,b : input arrays
        
        # rtol: relative tolerance (precision)
        # atol: absolute tolerance (precision)
            # e.g. 1e-06 = 10 -6
            
        # equal_nan:
            #bool: whether NaN on both arrays can be considered as equal elements

        raise ValueError(f"Expected sum of probabilities to be 1, but got {np.sum(p)}")
                        # remember to add the f before the string
                        # otherwise it will become literal value
    
    sum_prod = np.dot(x, p)
    return sum_prod
