def parameter_search(model,X_train,y_train,parameters,RandomizedSearchCV,
                     RandomForestClassifier,GradientBoostingClassifier,LogisticRegression,scoring='f1',n_iter=20):

    if model=='LogisticRegression':
        # Search for optimal parameters
        clf=LogisticRegression(max_iter=10000)
        C=parameters['C']
        distributions = {'C': C}
        LR_GS = RandomizedSearchCV(clf, distributions,n_iter, n_jobs=-1, scoring='f1')
        search_LR = LR_GS.fit(X_train, y_train)
        best_dict = search_LR.best_params_

        # Create Model
        clf = LogisticRegression(max_iter=1000, C=best_dict['C'])
        clf.fit(X_train, y_train)

        return search_LR, best_dict, clf

    if model=='GradientBoost':
        # Search for optimal parameters
        GB = GradientBoostingClassifier(random_state=42)
        n_estimators = parameters['n_estimators']
        learning_rate= parameters['learning_rate']
        max_depth = parameters['max_depth']
        max_features = parameters['max_features']
        distributions = {'max_depth': max_depth,
                         'n_estimators': n_estimators,
                         'max_features': max_features,
                         'learning_rate': learning_rate}
        GB_RS = RandomizedSearchCV(GB, distributions, random_state=42, n_iter=n_iter, n_jobs=-1, scoring=scoring)
        search_GB = GB_RS.fit(X_train, y_train)
        best_dict = search_GB.best_params_

        # Create Model
        GB = GradientBoostingClassifier(n_estimators=best_dict['n_estimators'],
                                     learning_rate=best_dict['learning_rate'],
                                     max_depth=best_dict['max_depth'],
                                     max_features=best_dict['max_features'],
                                     random_state=42)
        GB.fit(X_train, y_train)

        return search_GB, best_dict, GB

    if model=='RandomForest':
        # Search for optimal parameters
        RFC = RandomForestClassifier(random_state=42)
        n_estimators=parameters['n_estimators']
        max_features=parameters['max_features']
        max_depth = parameters['max_depth']
        min_samples_split = parameters['min_samples_split']
        min_samples_leaf = parameters['min_samples_leaf']
        distributions = {'max_depth': max_depth,
                         'min_samples_split': min_samples_split,
                         'min_samples_leaf': min_samples_leaf,
                         'n_estimators': n_estimators,
                         'max_features': max_features}
        RFC_RS = RandomizedSearchCV(RFC, distributions, random_state=42, n_iter=n_iter, n_jobs=-1, scoring=scoring)
        search_RFC = RFC_RS.fit(X_train, y_train)
        best_dict = search_RFC.best_params_

        #Create Model
        RFC = RandomForestClassifier(n_estimators=best_dict['n_estimators'],
                                      min_samples_split=best_dict['min_samples_split'],
                                      min_samples_leaf=best_dict['min_samples_leaf'],
                                      max_features=best_dict['max_features'],
                                      max_depth=best_dict['max_depth'],
                                      random_state=42, n_jobs=-1)
        RFC.fit(X_train, y_train)

        return search_RFC, best_dict, RFC
