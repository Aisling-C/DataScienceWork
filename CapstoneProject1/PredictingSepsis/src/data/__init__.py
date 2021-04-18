def plot_outliers():
    Low_Temp = raw[['Temp', 'id']].loc[raw.Temp <= 31].sort_values(by='Temp')
    Low_Temp_id = Low_Temp['id'].values
    Low_Temp_id

    for i in Low_Temp_id:
        y_ = raw[['Temp', 'id']].loc[raw.id == i]
        y = y_['Temp'].reset_index(drop=True)
        plt.plot(y, marker='.', linestyle='none', markersize=30, alpha=0.8, label='id: ' + str(i))
    plt.axhline(31, c='black', lw=3, alpha=0.7)
    plt.text(74, 31.2, '31C', size=18)
    plt.axhline(30, c='black', lw=3, alpha=0.7)
    plt.text(74, 29.2, '30C', size=18)
    plt.axhline(37, c='blue', lw=3, alpha=0.7)
    plt.text(70, 36.3, '37C - Normal', size=18)
    plt.xlabel('Time (Hour)', size=18)