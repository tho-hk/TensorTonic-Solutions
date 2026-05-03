import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    dframe = pd.DataFrame(data)
    grouped = dframe.groupby(group_col)[value_col]

    return grouped.agg(funcs).to_dict()