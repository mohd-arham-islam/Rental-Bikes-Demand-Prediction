import os
import sys 
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import customException
from src.logger import logging
from src.utils import saveObject, evaluateModel

@dataclass
class ModelTrainerConfig:
    modelFilePath = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.trainerConfig = ModelTrainerConfig()
    
    def initiateModelTrainer(self, trainArr, testArr):
        try:
            logging.info("Splitting the Train & Test Arrays")

            X_train, X_test, y_train, y_test = (
                trainArr[:, 1:],
                testArr[:, 1:],
                trainArr[:, 0],
                testArr[:, 0]
            )

            models = {
                'Linear Regression': LinearRegression(),
                'Random Forest Regressor': RandomForestRegressor(),
                'XGBoost Regressor': XGBRegressor(),
                'AdaBoost Regressor': AdaBoostRegressor(),
                'Gradient Boost Regressor': GradientBoostingRegressor(),
                'Decision Tree Regressor': DecisionTreeRegressor()
            }

            modelReport = evaluateModel(X_train, X_test, y_train, y_test, models)

            logging.info("Model Report Generated")

            bestModelScore = max(modelReport.values())
            # Checking for tied results
            bestModelNames = [name for name, score in modelReport.items() if score == bestModelScore]

            bestModelName = bestModelNames[0]
            bestModel = models[bestModelName]

            if bestModelScore < 0.8:
                logging.info("Couldn't find any best model")
                raise customException("No best model found", sys)
            
            logging.info("Best model found")

            bestModel.fit(X_train, y_train)
            predictions = bestModel.predict(X_test)
            score = r2_score(y_test, predictions)

            saveObject(
                filePath=self.trainerConfig.modelFilePath,
                object=bestModel
            )

            logging.info(f'Best Model is {bestModel} with R2 score of {score}')
            return {
                'Model': bestModelName,
                'Score': score
            }
        
        except Exception as e:
            raise customException(e, sys)