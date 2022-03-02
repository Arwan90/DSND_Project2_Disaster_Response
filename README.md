### DSND_Project2_Disaster_Response_Pipeline

#### +----------> This Project is dedicated for the Data Scientist Nano Degree | Udacity <----------+

#### Table of contents
* General Information
* Files available
* Dataset used
* Tools used
* Acknowledgment 
* Resources

#### General Information
In this project, two datasets were cleaned, combined, and processed. The resulted dataset was used to train a machine learning pipeline.
The Machine Learning Pipeline went through a tuning process using GridSearchCV.
The final result is a web app that takes messages as input, analyzes them using the tuned ML Pipeline, and categorizes the message according to 36 available categories.

#### Files available
* A message Dataset (messages.csv | From Figure 8 company) : 26248 Records x 4 Columns
* A categories Dataset (categories.csv | From Figure 8 company) : 26248 Records x 2 Columns
* A Python file for data processing (process_data.py)
* A resulted database that contains the cleaned table (Disaster_Response.db) with a Disaster_Response table.
* A python file that has the Machine Learning Pipeline (train_classifier.py).
* A pickle file that has the tuned ML Pipeline (classifier.pkl).
* A python file for rendring the web app pages (run.py).
* Two html files for formatting the web app pages (go.html | master.html).
* ReadMe file

#### Dataset used
messages & categories | The datasets were provided by Figure 8 company.

#### Libraries and Tools used
##### Jupyter Nootebook
* Python Version: 3.6.5
* Pandas Version: 0.23.0
* NLP Library: NLTK
* ML Libraries: NumPy, SciPy, Pandas, Sciki-Learn
* SQLlite Database Library: SQLalchemy
* Data Visualization: Flask, Plotly
##### Udacity IDE


#### Useful information: 
###### Web App Link :  https://view6914b2f4-3001.udacity-student-workspaces.com/
###### in order to run the web app, you must run the (run.py) file. 

[#### Program Execution Process :]
To create the database, train and save the model, follow these instructions: 
1. To run ETL pipeline to clean data and store the processed data in the database: 
 ( python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/disaster_response_db.db)
To run the ML pipeline that loads data from DB, trains classifier and saves the classifier as a pickle file python models/train_classifier.py data/disaster_response_db.db models/classifier.pkl
Run the following command in the app's directory to run your web app. python run.py

Go to http://0.0.0.0:3001/

#### Acknowledgment 
A special thanks to Udacity and Misk Academy for giving me the opportunity to learn, explore and use some data science-related skills.
Also, the appreciation goes to Fifure 8 company for offering the dataset.
Thanks to our mentor Mr. Haroon.
