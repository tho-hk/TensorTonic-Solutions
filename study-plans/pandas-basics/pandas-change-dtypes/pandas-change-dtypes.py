import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    dframe = pd.DataFrame(data)
    before = {}
    after = {}
    for col, dtype in dframe.dtypes.items():
        before[col] = str(dtype)
    dframe[column] = dframe[column].astype(target_type)
        
    for col, dtype in dframe.dtypes.items():
        after[col] = str(dtype)

    return [before, after]