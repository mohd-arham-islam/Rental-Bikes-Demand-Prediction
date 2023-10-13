import sys
import numpy as np

from src.exception import customException
from src.utils import loadObject

class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, arr):
        try:
            modelPath = 'artifacts/model.pkl'
            model = loadObject(filePath=modelPath)

            # We can also load the preprocessor object and then process the array/dataframe before doing the predictions.
            predictions = model.predict(arr)

            return int(predictions[0])
        except Exception as e:
            raise customException(e, sys)


class CustomData:
    def __init__(
            self,
            hour: int,
            temperature: float,
            humidity: int,
            windSpeed: float,
            month: int,
            dayOfMonth: int,
            dayOfWeek: int,
            precipitation: int
    ):
        self.hour = hour
        self.temperature = temperature
        self.humidity = humidity
        self.windSpeed = windSpeed
        self.month = month
        self.dayOfMonth = dayOfMonth
        self.dayOfWeek = dayOfWeek
        self.precipitation = precipitation
    
    def getDataArr(self):
        try:
            return np.array([self.hour, self.temperature, self.humidity, self.windSpeed, self.month, self.dayOfMonth, self.dayOfWeek, self.precipitation]).reshape(1,8)
        except Exception as e:
            raise customException(e, sys)