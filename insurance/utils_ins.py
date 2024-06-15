
def emblem_base(df, value_col="exposure", choose="max"):
    # medium tested
    """
    For each column except for value_col, sum value_col grouped by the unique elements of each column.
    Then, depending on the choose parameter, create a dictionary with the key being that column name and the value being the element with the highest or lowest sum of value_col.

    Parameters
    ----------
    df : pd.DataFrame
        The input data frame.
    value_col : str, optional
        The name of the column that contains the values to be summed. The default is "exposure".
    choose : str, optional
        The option to select the element with the highest or lowest sum of value_col. The default is "max".

    Returns
    -------
    dictt : dict
        The output dictionary with the column names as keys and the selected elements as values.

    Examples
    --------
    >>> df = pd.DataFrame({'country': ['USA', 'USA', 'Canada', 'Canada', 'Mexico', 'Mexico'],
                           'gender': ['M', 'F', 'M', 'F', 'M', 'F'],
                           'exposure': [100, 200, 300, 400, 500, 600]})
    >>> emblem_base(df)
    {'country': 'Mexico', 'gender': 'F'}
    >>> emblem_base(df, choose='min')
    {'country': 'USA', 'gender': 'M'}
    """
    
    # create an empty dictionary to store the results
    dictt = {}
    
    # loop through each column except for value_col
    for col in df.columns:
        if col != value_col:
            # group by the column and sum the value_col
            grouped = df.groupby(col)[value_col].sum()
            # depending on the choose parameter, select the element with the highest or lowest sum
            if choose == "max":
                element = grouped.idxmax()
            elif choose == "min":
                element = grouped.idxmin()
            else:
                raise ValueError("Invalid choose parameter. It must be either 'max' or 'min'.")
            # add the column name and the element to the dictionary
            dictt[col] = element
    
    # return the dictionary
    return dictt