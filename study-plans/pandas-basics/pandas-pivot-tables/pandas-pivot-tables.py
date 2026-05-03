import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    dframe = pd.DataFrame(data)
    pt = dframe.pivot_table(   # pass in the arguments
        values = values,
        index = index,
        columns = columns,
        aggfunc = aggfunc
    )

    pt = pt.fillna(0)          # fill missing data with 0 globally
    return pt.to_dict()        # answer requires dict