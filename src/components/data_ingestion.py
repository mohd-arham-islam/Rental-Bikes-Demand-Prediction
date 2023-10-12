import os
import sys

from src.components.data_transformation import DataTransformation
from src.exception import customException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.model_trainer import ModelTrainer

@dataclass()
class DataIngestionConfig:
    trainDataPath = os.path.join('artifacts', 'train.csv')
    testDataPath = os.path.join('artifacts', 'test.csv')
    rawDataPath = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()
    
    def initiateDataIngestion(self):
        logging.info("Started the Data Ingestion process")

        try:
            # This is a case of simple data reading. It can anything from reading from a database, or from an API, etc.
            df = pd.read_csv('notebook\data\SeoulBikeData.csv', encoding='unicode_escape')
            logging.info("Imported Dataset")

            # The following code will create an 'artifacts' folder
            os.makedirs(os.path.dirname(self.ingestionConfig.trainDataPath), exist_ok=True)

            df.to_csv(self.ingestionConfig.rawDataPath, index=False, header=True)

            logging.info("Train Test Split Initiated")
            trainSet, testSet = train_test_split(df, test_size=0.3, random_state=42)

            trainSet.to_csv(self.ingestionConfig.trainDataPath, index=False, header=True)
            testSet.to_csv(self.ingestionConfig.testDataPath, index=False, header=True)

            logging.info("Ingestion Complete")

            return (
                self.ingestionConfig.trainDataPath,
                self.ingestionConfig.testDataPath
            )
        
        except Exception as e:
            raise customException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    trainDataPath, testDataPath = obj.initiateDataIngestion()

    transformer = DataTransformation()
    trainArr, testArr = transformer.initiateTransformation(trainDataPath, testDataPath)

    trainer = ModelTrainer()
    trainer.initiateModelTrainer(trainArr, testArr)