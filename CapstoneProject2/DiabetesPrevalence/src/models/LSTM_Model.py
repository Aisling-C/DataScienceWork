from pandas import concat
import numpy as np

def series_to_supervised(df, dep_var, n_in, concat):
    """
    Adapted from: https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
    Accessed 7/26/2021

    Prepare diabetes_county dataframe for LSTM Model
    With user-specified sequence length

    Arguments:
    dep_var: Name of the dependent variable
    df: Sequence of observations as a list or NumPy array.
    n_in: Number of lag observations as input (X).
    dropnan: Boolean whether or not to drop rows with NaN values.

    Returns:
    Pandas dfFrame of series framed for supervised learning.
    Captures all independent variables for time periods t -> t-n_in,
    Captures dependent variables for time periods t-1 -> t-(n_in+1),
    """
    scf_col = df.pop('state_county_fips')
    n_vars = df.shape[1]
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [(df.iloc[:, j].name + '(t-%d)' % (i)) for j in range(n_vars)]
    # current sequence
    for i in range(df.shape[1]):
        cols.append(df.iloc[:, i])
    names.extend(list(df.columns))
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    agg.dropna(inplace=True)
    # Drop current year's diabetes value
    agg.drop(columns=dep_var, inplace=True)
    # Add the preceeding diabetes value to the last year
    first_y = df.shift((n_in + 1))[dep_var]
    agg = concat([first_y, agg], axis=1)
    agg.rename(columns={'diabetes_%': 'diabetes_%(t-{})'.format((n_in + 1))}, inplace=True)
    # Return state county fips column to df
    agg = concat([agg, scf_col], axis=1)
    return agg

def test_train_split(df, df_copy, n, years, np):
    Y = df_copy[df_copy.years_since_2006 > years[(n + 1)]][['diabetes_%', 'state_county_fips', 'years_since_2006']]
    X = df

    # Ensure that the y values correspond to the X values
    s1 = X.merge(Y, left_on=['state_county_fips', 'years_since_2006'],
                 right_on=['state_county_fips', 'years_since_2006'], how='inner')
    s2 = X.merge(Y, left_on=['state_county_fips', 'years_since_2006'],
                 right_on=['state_county_fips', 'years_since_2006'], how='left')
    s3 = X.merge(Y, left_on=['state_county_fips', 'years_since_2006'],
                 right_on=['state_county_fips', 'years_since_2006'], how='right')

    if s1.shape != s2.shape:
        print(s1.shape, s2.shape, s3.shape)
        raise ValueError("X & Y Don't Match")
    if s1.shape != s3.shape:
        print(s1.shape, s2.shape, s3.shape)
        raise ValueError("X & Y Don't Match")
    if s2.shape != s3.shape:
        print(s1.shape, s2.shape, s3.shape)
        raise ValueError("X & Y Don't Match")
    if sum(~(Y['diabetes_%'].values == s1['diabetes_%'].values)) != 0:
        raise ValueError("X & Y Don't Match")

    # Test/Train Split
    X = X.drop(columns='state_county_fips')
    X_train = np.array(X[X.years_since_2006 < 1])
    X_test = np.array(X[X.years_since_2006 == 1])
    y_train = np.array(Y[Y.years_since_2006 < 1]['diabetes_%'])
    y_test = np.array(Y[Y.years_since_2006 == 1]['diabetes_%'])

    # Reshape X into sequences, print shapes
    X_train = X_train.reshape(X_train.shape[0], n + 1, 25)
    X_test = X_test.reshape(X_test.shape[0], n + 1, 25)
    print("X_train shape: {}  y_train shape: {}".format(X_train.shape, y_train.shape))
    print("X_test shape: {}  y_test shape: {}".format(X_test.shape, y_test.shape))

    return X_train, y_train, X_test, y_test