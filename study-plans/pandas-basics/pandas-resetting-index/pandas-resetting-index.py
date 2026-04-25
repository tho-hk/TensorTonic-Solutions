import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    dframe = pd.DataFrame(data)
    # this set input index_col as index column
    indexed_df = dframe.set_index(index_col)
    # reset_index(drop=False): moves the current index back into data columns
    # and restores the default integer row labels (0, 1, 2, ...)
    # drop=True would discard the index entirely instead of restoring it as a column
    reset_df = indexed_df.reset_index(drop=False)

    return [list(indexed_df.columns), list(reset_df.columns)]
    