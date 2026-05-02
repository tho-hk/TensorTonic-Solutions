import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    dframe = pd.DataFrame(data)

    grouped = dframe.groupby(group_col)

    # method 1: use agg() to pass in all aggregate functions
    results = grouped[value_col].agg(["sum", "mean", "count"])
    # this returns a dataframe. columns are agg() items
    # convert them to dict for answer
    answer = {col: results[col].to_dict() for col in results.columns}
    
    return answer
    
    '''
    method 2: populate each aggregate directly into the dict object
    
    return {
        "sum": grouped[value_col].sum().to_dict(),
        "mean": grouped[value_col].mean().to_dict(),
        "count": grouped[value_col].count().to_dict()
    }
    '''