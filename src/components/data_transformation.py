import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
import datetime as dt
from src.exception import customException
from src.logger import logging

# The following class would be required if we're saving the preprocessor object as a pickle file.
# @dataclass
# class DataTransformationConfig:
#     preprocessorObjFilePath = os.path.join('artifacts', 'preprocessor.pkl')
class Processor:
    def __init__(self) -> None:
        pass
    
    def encode(self, x):
        day = {
            'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thursday': 4,
            'Friday': 5,
            'Saturday': 6,
            'Sunday': 7
        }

        return day[x]

    def preprocessing(self, df):
        df['date'] = df['Date'].apply(lambda x: dt.datetime.strptime(x,"%d/%m/%Y"))

        df['Month'] = df['date'].dt.month
        df['Day'] = df['date'].dt.day
        df['Day of the week'] = df['date'].dt.day_name()
        df = df.drop(['Date', 'Dew point temperature(°C)', 'Solar Radiation (MJ/m2)', 'Seasons', 'Holiday', 'Functioning Day', 'date', 'Visibility (10m)'], axis=1)

        df['Precipitation (mm)'] = df['Rainfall(mm)'] + 10 * df['Snowfall (cm)']
        df = df.drop(['Rainfall(mm)', 'Snowfall (cm)'], axis=1)
        df['Day of the week'] = df['Day of the week'].apply(lambda x: self.encode(x))

        return df

class DataTransformation:
    # def __init__(self):
    #     self.transformationConfig = DataTransformationConfig()
    
    # Since there isn't much transformation to do in terms of scaling, imputing, etc, I will skip the function -> getTransformerObject which basically returns the preprocessing object.

    def initiateTransformation(self, trainPath, testPath):
        try:
            trainData = pd.read_csv(trainPath)    
            testData = pd.read_csv(testPath)   

            logging.info("Imported the Train and Test Datasets") 

            logging.info("Initiated Data Transformation")

            processor = Processor()
            trainData = processor.preprocessing(trainData)
            testData = processor.preprocessing(testData)

            logging.info("Processing Complete")

            trainArr = np.array(trainData)
            testArr = np.array(testData)

            return (
                trainArr,
                testArr
            )
        
        except Exception as e:
            raise customException(e, sys)
