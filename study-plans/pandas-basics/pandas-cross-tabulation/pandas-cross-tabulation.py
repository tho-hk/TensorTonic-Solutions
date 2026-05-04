import pandas as pd

def cross_tab(data, row_col, col_col):
    """
    Returns: nested dict {col_value: {row_value: frequency}}
    """
    dframe = pd.DataFrame(data)
    crossed = pd.crosstab(dframe[row_col], dframe[col_col]) # pass arguments to crosstab

    return crossed.to_dict() # answer required as dict