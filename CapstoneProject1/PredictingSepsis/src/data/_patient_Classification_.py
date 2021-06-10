def PatientLevelClassification (model,probability,X_test,y_test_all,df,test_id,pd,classification_report,confusion_matrix):
    #This function produces a classification report and confusion matrix for patient level predictions of having sepsis, rather than hourly
    #It is specific to the sepsis project in its current form
    # Set probability threshold
    q = model.predict_proba(X_test)[:, 1]
    y_pred_test_new = [1 if i > probability else 0 for i in q]

    # Bring back patient id & sepsis onset information from original dataframe
    X_test2 = df[df.id.isin(test_id)][['id', 'SepsisOnset']].reset_index(drop=True)

    # Combine patient id and predictions into a dataframe
    c = pd.concat([y_test_all.reset_index(drop=True), pd.Series(y_pred_test_new, name='Prediction')], axis=1)
    d = pd.concat([X_test2, c], axis=1)

    # Create a prediction column; copy of the model's predictions, except it marks all prediction during sepsis/post sepsis as 0
    # Because we are only interested in model performance pre-sepsis or when a patient doesn't have sepsis.
    pre_sep = []
    for i in list(d.id.unique()):
        q = d[d.id == i]
        SepOn = q['Prediction']
        # Get Prediction for Non Sepsis Patients
        if q['SepsisOnset'].sum() == 0:
            [pre_sep.append(g) for g in list(q[q.id == i].Prediction.values)]
        else:
            # Get Predictions for Non Sepsis Patients, but only in the pre sepsis period - mark as zero predictions in the sepsis period or later
            sep_on = q['SepsisOnset'].idxmax()
            for items in SepOn.iteritems():
                if items[0] <= sep_on:
                    if items[1] == 1:
                        pre_sep.append(1)
                    else:
                        pre_sep.append(0)
                else:
                    pre_sep.append(0)
    d['Prediction'] = pre_sep

    # Create a Dataframe of patient-level, sepsis prediction
    model_name = type(model).__name__
    Pred_name=model_name+'_Prediction'
    Patient_Predictions = d.groupby('id')[['SepsisOnset', 'Prediction']].sum().reset_index()
    Patient_Predictions[Pred_name] = Patient_Predictions.Prediction.apply(lambda x: 1 if x > 0 else 0)
    Patient_Predictions.drop(columns='Prediction', inplace=True)

    # Print Classification Report - Patient Level Data
    cr=classification_report(Patient_Predictions.SepsisOnset.values,Patient_Predictions[Pred_name].values)

    # Print Confusion Matrix - Patient Level Data
    cm = confusion_matrix(Patient_Predictions.SepsisOnset.values, Patient_Predictions[Pred_name].values)

    return Patient_Predictions, cm, cr