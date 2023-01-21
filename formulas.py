

def fill_mode(df, column):
    ''' To call the mode of any string column
    df = DataFrame
    column 'Column_name
    '''
    col_mode = df[column].mode()[0]
    col_mode = df[column].fillna(col_mode)
    return col_mode



def concat_df(lst, df, column):
    """Concatenate dataframes that contains some words stored in a list

    make sure there are no NaN o null values

    words: List of words
    dataframe: dataframe where we want to look for the words
    column: Specific column, remember needs to be between '' 
    
    """
    
    import pandas as pd
    
    lst_df = []
    for i in lst:
        x = df[df[str(column)].str.contains(i, case=False, na=False)]
        lst_df.append(x)
        
    return pd.concat(lst_df)


    
