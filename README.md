# Rental Bikes Demand Prediction

This is an end to end Machine Learning project. This project aims to predict the demand for rental bikes using a comprehensive dataset that includes hourly bike rental counts and corresponding weather conditions. The goal is to employ regression analysis techniques to accurately forecast the required number of bikes for each hour, thus enhancing the user experience and mobility convenience provided by rental bike providers. I have used modular coding in this project and have tried incorporating industry-level best practices such as file versioning, logging, and a well-defined folder structure.

![image](https://github.com/mohd-arham-islam/Bike-Share/assets/111959286/69a3ccb3-f46f-4d64-af80-b67173db4264)


## Exploratory Data Analysis (EDA)
During the exploratory phase of the project, several insightful visualizations were created to better understand the dataset:

* **Monthly Variation:** Bike rentals exhibited a clear seasonal pattern, with the lowest counts in winter (December to February) and the highest in June.
* **Day-wise Analysis:** Consistent rentals were observed from Monday to Friday, with a slight dip on weekends, suggesting a connection between weekday/weekend demand and bike availability.
* **Hourly Fluctuations:** Two prominent rental peaks at 8 am and 6 pm aligned with office commuting hours, emphasizing the correlation between rentals and work schedules. The lowest counts were at 4 am, and the highest at 6 pm.
* **Seasonal Distribution:** Summer had the highest rental percentage (37%), followed by autumn (29%), spring (26%), and winter (7.9%), indicating higher demand during pleasant weather.
* **Temperature Influence:** Bike rentals increased with rising temperatures, peaking around 25°C, emphasizing that mild temperatures are favorable for rentals while extreme cold or heat reduces demand.

For more details, refer to the EDA notebook at: `notebook/eda.ipynb`

## Feature Engineering
In the feature engineering phase, less important columns such as 'Dew point temperature(°C)', 'Solar Radiation (MJ/m2)', and 'Visibility (10m)' were dropped. Additionally, rainfall and snowfall were combined into a single column named "precipitation," streamlining the dataset and enhancing model efficiency.

## Model Building
For the model building process, I tried an ensemble of Regression models sich as RandomForestRegressor, AdaBoostRegressor, XGBoostRegressor, etc. The XGBoostRegressor gave the best performance with an R2 score of **0.92**.

## Flask Application for Model Deployment
To provide easy access to the trained model's predictions, a Flask application was developed. The web interface allows users to input relevant parameters and receive accurate bike count predictions in real-time. This integration of regression analysis, model deployment, and user interaction empowers rental bike providers to make informed decisions and optimize resource management effectively.

## Model Deployment using Azure 
I have deployed the application on Azure Cloud using GitHub actions, which is a crucial aspect of a Continuous Deployment (CD) pipeline. Any changes made in the repository get automatically reflected in the web app.


By leveraging these insights, feature engineering techniques, and advanced regression models, this project offers a comprehensive solution for predicting bike rental demand, enhancing the overall user experience, and enabling more efficient resource allocation for rental bike providers.

