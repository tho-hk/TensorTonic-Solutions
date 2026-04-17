import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    dframe = pd.DataFrame(data) #enforce data type

    rows = dframe.shape[0]
    cols = dframe.shape[1]

    columns = list(dframe.columns) # df.columns originally a pandas index object
    
    
    '''
    if implemented from scratch:
    
    columns = []
    for col in range(len(dframe.columns)):
        columns.append(dframe.columns[col])
    '''
    
    dtypes = {}
    for col in dframe.columns:           # this loops through the dtype objects
        dtype_obj = dframe.dtypes[col]   # each have "index: dtype", e.g. "age: int64"
                                         # here it looks up the dtype using index key e.g. "age"
        dtype_str = str(dtype_obj)       
        dtypes[col] = dtype_str
        # each key ("age", "name") would be assigned a value ("int64", "object")
    
    total_values = rows * cols

    return {
        "rows": rows,
        "cols": cols,
        "columns": columns,
        "dtypes": dtypes,
        "total_values": total_values
    }