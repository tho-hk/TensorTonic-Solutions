import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    dframe = pd.DataFrame(data)

    # requirement 1: dict mapping column names to dtype strings
    d_dict = {}
    
    for col, dtype in dframe.dtypes.items():
        d_dict[col] = str(dtype)
        '''
        ### dframe.dtypes is a Series, and .items() converts it to a lazy iterator
        ### which yields (index, value) tuples — here (column_name, dtype_object)

        print(f"col: {col}, dtype object: {dtype}, as string: {str(dtype)}")
        print(f"type of dtype: {type(dtype)}")

        ### terminal output (with data = {"age":[25,30], "name":["Alice","Bob"]}):
        # col: age, dtype object: int64, as string: int64
        # type of dtype: <class 'numpy.dtype[int64]'>
        # col: name, dtype object: object, as string: object
        # type of dtype: <class 'numpy.dtype[object_]'>
        '''

    # requirement 2: dict mapping dtype strings to count of columns with that type
    freq_dict = {}
    for dtp, counts in dframe.dtypes.value_counts().items():
        '''
        ### if we add some lines to debug:
        
        print(type(dtp))
        print(str(dtp))
    
        ### output will be:
        # int64
        # <class 'numpy.dtypes.ObjectDType'>
        # object
        # {dtype('int64'): 1, dtype('O'): 1}
        
        '''
        freq_dict[str(dtp)] = int(counts)

    # requirement 3: int (column count)
    col_count = dframe.shape[1]

    return {
        "dtypes": d_dict,
        "type_counts": freq_dict,
        "num_columns": col_count
    }