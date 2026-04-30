import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    
    dframe = pd.DataFrame(data)
    
    try:
        old_count = dframe[column].value_counts()[old_val]
    except KeyError:
        old_count = 0
        
    dframe[column] = dframe[column].replace(old_val, new_val)

    
    return {"data": dframe.to_dict(orient="list"),
            "count": old_count}