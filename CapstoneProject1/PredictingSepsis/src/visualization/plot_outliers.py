def plot_low_outliers(df,column,limit,h_line,color):
    Outlier_Vals = df[[column, 'id']].loc[df[column] <= limit].sort_values(by=column)
    Outlier_Vals_id = Outlier_Vals['id'].values
    for i in Outlier_Vals_id:
        y_ = df[[column, 'id']].loc[df.id == i]
        y = y_[column].reset_index(drop=True)
        a=plt.plot(y, marker='.', linestyle='none', markersize=30, alpha=0.8, label='id: ' + str(i))
    for i in h_line:
        a=plt.axhline(i, c=color, lw=3, alpha=0.7)
    return a

def plot_high_outliers(df,column,limit,h_line,color):
    Outlier_Vals = df[[column, 'id']].loc[df[column] >= limit].sort_values(by=column)
    Outlier_Vals_id = Outlier_Vals['id'].values
    for i in Outlier_Vals_id:
        y_ = df[[column, 'id']].loc[df.id == i]
        y = y_[column].reset_index(drop=True)
        b=plt.plot(y, marker='.', linestyle='none', markersize=30, alpha=0.8, label='id: ' + str(i))
    for i in h_line:
        b=plt.axhline(i, c=color, lw=3, alpha=0.7)
    return b