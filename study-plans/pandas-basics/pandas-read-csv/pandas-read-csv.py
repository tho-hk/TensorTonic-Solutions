import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    dframe = pd.DataFrame(data) # pd.DataFrame already accepts dict as input
    # a data frame already has shape and column attributes
    # just make them lists
    shape = list(dframe.shape) # data.shape is a tuple, new we need a list
    columns = list(dframe.columns) # returns column headers of data frame in a list
    data_back = dframe.to_dict(orient='list')

    # return items arranged in dict as required
    return {
        "data": data_back,
        "shape": shape,
        "columns": columns        
    }