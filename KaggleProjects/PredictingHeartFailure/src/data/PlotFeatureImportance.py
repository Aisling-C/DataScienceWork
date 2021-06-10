def Plot_Feat_Imp(model,labels,pd,np,plt,figsz):
    importance = model.feature_importances_
    importance = pd.DataFrame(importance, index=labels,
                              columns=["Importance"])

    x = range(importance.shape[0])
    y = importance.iloc[:, 0]
    plt.subplots(figsize=figsz)
    plt.bar(x, y, align="center")
    plt.xticks(ticks=range(0,len(labels)),labels=importance.index,rotation=90)
    plt.title('Feature Importance')
    plt.show()