import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    dframe = pd.DataFrame(data)
    # df.head(n) / df.tail(n) mirrors Linux head/tail for positive n
    # negative n: head(-n) drops last n rows, tail(-n) drops first n rows
    df_head = dframe.head(n)
    df_tail = dframe.tail(n)
        
    return {
        "head": df_head.to_dict(orient="list"), # recall: to_dict returns column data as a dict
                                                # orient="list" gives 
        "tail": df_tail.to_dict(orient="list")
    }