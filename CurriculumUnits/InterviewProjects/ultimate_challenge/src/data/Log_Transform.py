def log_trans_columns(df,list_,PowerTransformer,np):
    # Function to apply log transform to numerical data
    for feature in list_:
        a=np.array(df[feature]).reshape(-1, 1)
        pow_trans = PowerTransformer()
        q=pow_trans.fit_transform(a)
        df[feature]=q
    return df