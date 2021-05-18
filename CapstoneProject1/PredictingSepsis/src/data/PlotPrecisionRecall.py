def Plot_PR(Model, X_train, y_train, X_test, y_test, title, auc, precision_recall_curve, np, plt, figsz):
    np.seterr(divide='ignore', invalid='ignore')

    plt.subplots(figsize=figsz)

    # Plot no skill line
    plt.plot([0, 1], [0, 0], linestyle='--', label='No Skill', c='orange')

    # Train Data
    yhat = Model.predict_proba(X_train)
    yhat = yhat[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_train, yhat)
    fscore = (2 * precision * recall) / (precision + recall)
    ix = np.argmax(fscore)
    plt.scatter(recall, precision, marker='.', color='red', label='Train', s=10)
    plt.scatter(recall[ix], precision[ix], marker='o', color='darkred', label='Best Train', s=100)
    auc_train = round(auc(recall, precision), 3)
    prob=thresholds[ix]

    # Print Statement
    print('Best Train Threshold=%f, F-Score=%.3f' % (thresholds[ix], fscore[ix]))

    # Test Data
    yhat = Model.predict_proba(X_test)
    yhat = yhat[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_test, yhat)
    fscore = (2 * precision * recall) / (precision + recall)
    ix = np.argmax(fscore)
    plt.scatter(recall, precision, marker='.', color='blue', label='Test', s=10)
    plt.scatter(recall[ix], precision[ix], marker='^', color='darkblue', label='Best Test', s=100)
    auc_test = round(auc(recall, precision), 3)

    # Print Statements
    print('Best Test Threshold=%f, F-Score=%.3f' % (thresholds[ix], fscore[ix]))
    print('Train AUC: {} Test AUC: {}'.format(auc_train, auc_test))

    # General Plotting
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision Recall Curve')
    plt.legend()
    plt.title(title)
    plt.show()

    return prob