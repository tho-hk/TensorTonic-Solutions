import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    dframe = pd.DataFrame(data)

    rows_before = dframe.shape[0]                       # int
    cleaned_data = dframe.drop_duplicates(keep="first") # pandas dataframe
                                                        # keep = "first" is default
    rows_after = cleaned_data.shape[0]                  # int

    # convert cleaned data into dict, then combine into a list
    return [rows_before, rows_after, cleaned_data.to_dict(orient="list")]