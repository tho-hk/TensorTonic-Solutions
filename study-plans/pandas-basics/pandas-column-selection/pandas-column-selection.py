import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    data = pd.DataFrame(data)
    column = str(column)
    
    list_col = data[column]      # extract a column with index
                                 # but is still in dataframe form
    list_col = list_col.tolist() # turn the column DF into list

    return {
        "values": list_col,      # returns the requied list
        "length": len(list_col)  # count number of items and return
    }