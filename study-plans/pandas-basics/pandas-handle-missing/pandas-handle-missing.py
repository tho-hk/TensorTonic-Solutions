import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    dframe = pd.DataFrame(data)

    # .isna().sum() returns column na counts in a series
    # use .to_dict() to return in dict form
    na_count = dframe.isna().sum().to_dict()

    # .fillna() returns a dataframe
    # use to_dict() and specify list form to return answer
    cleaned_df = dframe.fillna(fill_value).to_dict(orient="list")

    return {
        "null_counts": na_count,
        "cleaned_data": cleaned_df
    }