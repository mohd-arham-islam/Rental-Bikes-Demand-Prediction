import dill
import os
import sys 
from sklearn.metrics import r2_score
from src.exception import customException

def saveObject(filePath, object):
    try:
        dirPath = os.path.dirname(filePath)
        os.makedirs(dirPath, exist_ok=True)

        with open(filePath, "wb") as fileObj:
            dill.dump(object, fileObj)
        
    except Exception as e:
        raise customException(e, sys)

def evaluateModel(X_train, X_test, y_train, y_test, models):
    try:
        report = {}

        for modelName, model in models.items():
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            trainModelScore = r2_score(y_train, y_train_pred)
            testModelScore = r2_score(y_test, y_test_pred)

            report[modelName] = testModelScore
            
        return report
    
    except Exception as e:
        raise customException(e, sys)
            
def loadObject(filePath):
    try:
        with open(filePath, 'rb') as file:
            return dill.load(file)
    except Exception as e:
        raise customException(e, sys)