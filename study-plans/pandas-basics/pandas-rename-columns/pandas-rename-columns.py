import pandas as pd

def rename_columns(data, rename_map):
    """
    Returns: dict mapping renamed column names to value lists
    """
    dframe = pd.DataFrame(data)
    updated = dframe.rename(columns=rename_map) # columns should be a dict of
                                                # old_names : new_names

    return updated.to_dict(orient="list") # question requires dict of lists