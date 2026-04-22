import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    dframe = pd.DataFrame(data)

    # Creates a boolean Series of True/False
    filter_crit = (dframe[column] > threshold)

    '''
    When you need multiple conditions:
    
    # AND condition — both must be True
    mask = (dframe["score"] > 80) & (dframe["age"] < 30)
    
    # OR condition — either must be True
    mask = (dframe["score"] > 80) | (dframe["age"] < 30)
    '''

    # Passes the boolean mask into dframe[] — pandas keeps only rows where the mask is True and drops the rest. 
    # This is called boolean indexing.
    filtered = dframe[filter_crit]

    count = len(filtered)

    return {
        "filtered_data": filtered.to_dict(orient='list'),
        "count": count
    }