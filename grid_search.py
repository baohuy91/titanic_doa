from sklearn.model_selection import GridSearchCV


def grid_search(X_train, y_train, est, param_grid):
    # Setup GridSearch
    gs = GridSearchCV(estimator=est,
                      param_grid=param_grid,
                      scoring='roc_auc',
                      cv=10,
                      n_jobs=-1)
    gs = gs.fit(X_train, y_train)

    print(gs.best_score_)
    print(gs.best_params_)


def grid_search_svc(X_train, y_train, est):
    param_range = [0.1, 1.0, 10.0]
    param_grid = [{'clf__C': param_range,
                   'clf__kernel': ['linear']},
                  {'clf__C': param_range,
                   'clf__gamma': param_range,
                   'clf__kernel': ['rbf']}]

    grid_search(X_train, y_train, est, param_grid)


def grid_search_lr(X_train, y_train, est):
    param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    param_grid = [{'clf__C': param_range}]

    grid_search(X_train, y_train, est, param_grid)


def grid_search_knn(X_train, y_train, est):
    param_range = [1, 5, 10, 15, 20, 25, 30, 50]
    param_grid = [{'clf__n_neighbors': param_range}]

    grid_search(X_train, y_train, est, param_grid)


def grid_search_dt(X_train, y_train, est):
    param_range = [1, 2, 3, 4, 5, 6, 7, 8]
    param_grid = [{'max_depth': param_range}]

    grid_search(X_train, y_train, est, param_grid)


def grid_search_rf(X_train, y_train, est):
    param_range = [10, 50, 100, 150, 200]
    param_grid = [{'n_estimators': param_range}]

    grid_search(X_train, y_train, est, param_grid)