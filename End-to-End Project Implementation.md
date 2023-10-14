# Steps involved in implementing an end-to-end project

## GitHub Setup
* Create a new repo in GitHub.
* Create a new venv using the command `python -m venv ./<Name of Virtual Environment>`
* Activate the venv using the command `.\<Name of Directory>\Scripts\activate`
* Create a README.md file
* Follow the steps as mentioned in GitHub
    * `git add README.md`
    * `git commit -m "<Commit Message>"`
    * `git branch -M main`
    * `git remote add origin <URL of GitHub repo>`
    * `git push -u origin main`
* If making any changes in GitHub directly, make sure to use the `git pull` command to make sure that the IDE is in sync with GitHub.
* Use `git add .` to add all the changed/modified files.

## setup.py & requirements.txt
In Python, **setup.py** is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. It basically allows us to create our machine learning project as a package.

* Also create a folder named `src`. Inside that, create a `__init__.py` file. Entire project development will be made inside the `src` folder
* Add `-e .` at the end of `requirements.txt` file. This will trigger the `setup.py` file.
* Now whenever we run the command `pip install -r requirements.txt`, the setup file will get triggered and the package will be built.

## Project Structure
* In the `src` folder, create a subfolder `components`. In that, create `__init__.py`, `data_ingestion.py`, `data_transformation.py`, and `model_trainer.py` files.
* Create another subfolder `pipeline` and create `__init__.py`, `train_pipeline.py`, and `predict_pipeline.py` files.
* Also create `logger.py`, `exception.py`, and `utils.py` files.

The reason why we use such a structure is to ensure readability and debugging. Also code blocks can be reused in different projects. It also facilitates collaboration.

### Exception File
In a machine learning project, the `exception.py`` file and custom exceptions are essential for efficient error handling and code maintainability. Custom exceptions provide clear, descriptive error messages that aid in debugging and make the code more readable, while separating them into a dedicated file enhances modularity. This practice streamlines error management and ensures that issues are handled gracefully, improving the overall reliability of the project.

### Logger File
In a machine learning project, a logger file is crucial for effective monitoring, troubleshooting, and maintaining project health. It records key information, such as training progress, validation metrics, errors, and warnings, allowing developers and data scientists to track model performance, identify issues, and make informed improvements. Additionally, logging provides a historical record of project activities, aiding in reproducibility, collaboration, and auditing, which are vital aspects of machine learning project management.

## Setup Jupyter Notebook
Create a folder named `notebook` that has a subfolder `data`. The dataset will be placed in this folder. In the parent folder, create `.ipynb` files for EDA and Model Training.

## Data Ingestion
In an end-to-end machine learning (ML) project, the data_ingestion.py script or module typically plays a crucial role in the data preprocessing and data acquisition stages. Its primary purpose is to load, clean, and prepare the raw data for use in the machine learning pipeline.

## Data Transformation
In a machine learning project, the "data transformation.py" file plays a pivotal role in shaping the quality and effectiveness of the model. It is essential for preparing and structuring the raw data into a format that is suitable for training and prediction. Data transformation encompasses tasks like cleaning, normalization, encoding categorical variables, handling missing values, feature engineering, and more.

## Model Trainer
The model is trained inside this file. This file has a class that returns the score of the best model. The object of this class is called in the data ingestion script.

Infact the data transformation class object is also run inside the ingestion script.

## Predict Pipeline
All the things done inside the flask app method will be done here. For example accepting form data, processing it, etc.

## Deployment to AWS Elastic Beanstalk
AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, and auto-scaling to application health monitoring. 

At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.

| Service                  | Pros                                                      | Cons                                                   |
|--------------------------|-----------------------------------------------------------|--------------------------------------------------------|
| **AWS Elastic Beanstalk** | - Easy to use and set up.  - Auto-scales your application. - Handles load balancing, monitoring, and auto-recovery. - Supports a variety of programming languages including Python. | - Limited control over the underlying infrastructure. - Limited customizability, especially for highly complex applications. - Pricing can be higher than other options for long-term use. |
| **Amazon EC2**           | - Full control over the virtual server instance. - Can be customized to fit the specific requirements of your Flask app and ML project. - Scalable, and can be used for various other applications. | - Requires manual configuration for load balancing, scaling, and monitoring. - Maintenance, patching, and updates are your responsibility. - You need to manage the entire infrastructure, which can be complex. |
| **AWS Lambda**           | - Serverless, so you don't need to worry about infrastructure. - Cost-effective as you only pay for the compute time used. - Scales automatically based on traffic. - Well-suited for lightweight Flask apps and smaller ML workloads. | - Limited to 15 minutes of execution time per request. - Limited to 3 GB of memory per execution. - Cold start latency can be an issue. - May require additional services for database and long-running tasks. |
