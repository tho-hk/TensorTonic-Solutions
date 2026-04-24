import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    dframe = pd.DataFrame(data)
    # the index column is replaced by your desired column
    # it will be removed from dframe
    dframe = dframe.set_index(index_col)

    return {
        "index_values": list(dframe.index),
        "columns": list(dframe.columns),
        # notice, the index column has been removed, no need to slice
        # here if you slice with .iloc[:,1:]
        # it will drop 1 column of desired data
        "data": dframe.to_dict(orient="list") # dframe only contains data without index column
    }