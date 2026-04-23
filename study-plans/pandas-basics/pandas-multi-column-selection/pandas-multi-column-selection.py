import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    dframe = pd.DataFrame(data)
    selected_col = dframe[columns] # this selection method preserves order of selected col)

    return selected_col.to_dict(orient="list") # using the to_dict turns dataframe to a dict of list