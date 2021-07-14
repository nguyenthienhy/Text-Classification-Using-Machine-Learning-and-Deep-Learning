from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import *
from sklearn.metrics import *
from src.utils.plot_metric import *
from sklearn.feature_selection import *
from sklearn.pipeline import *
from sklearn.model_selection import GridSearchCV
import constant

class Random_Forest:
    def __init__(self): 
        self.model = Pipeline([
            ('feature_selection', SelectFromModel(RandomForestClassifier(n_estimators=150))),
            ('classification', LinearSVC(C=1.0))
        ])
        self.param_grid = { 
                            'n_estimators': [100, 150],
                            'max_features': ['auto', 'sqrt', 'log2'],
                            'max_depth' : [10, 100, None],
                            'criterion' :['gini', 'entropy'],
                            'min_samples_leaf' : [1, 10, 15],
                            'min_samples_split' : [2, 10, 15],
                            'bootstrap': [False, True]
                        }
        self.grid = GridSearchCV(estimator=self.model, param_grid=self.param_grid, cv=5, n_jobs=2)

    def get_best_hyperparams(self, X_train, y_train):
        self.grid.fit(X_train, y_train)
        return self.grid.best_params_
    
    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return classification_report(y_test, y_pred, target_names=constant.target_names)

    def get_confusion_matrix(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        plot_confusion_matrix(confusion_matrix(y_test, y_pred), constant.target_names)
