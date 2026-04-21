import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    dframe = pd.DataFrame(data)
    d_element = dframe.iloc[row,col] # exact position
    d_row = dframe.iloc[row,:]       # entire row
    d_col = dframe.iloc[:,col]       # entire col

    # iloc returns a series, need to use list() to convert to a list
    return [d_element, list(d_row), list(d_col)]