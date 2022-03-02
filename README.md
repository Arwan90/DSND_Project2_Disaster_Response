### DSND_Project2_Disaster_Response_Pipeline

#### +----------> This Project is dedicated for the Data Scientist Nano Degree | Udacity <----------+

#### Table of contents
* [General Information](#general)
* [Files available](#files)
* Dataset used
* Tools used
* Acknowledgment 
* Resources



<a name="general"/> #### General Information

In this project, two datasets were cleaned, combined, and processed. The resulted dataset was used to train a machine learning pipeline.
The Machine Learning Pipeline went through a tuning process using GridSearchCV.
The final result is a web app that takes messages as input, analyzes them using the tuned ML Pipeline, and categorizes the message according to 36 available categories.

<a name="files"/>
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


#### Program Execution Process :
To create the database, train and save the model, follow these instructions: 
    1. To run ETL pipeline for data cleaning and saving: 
     ( python process_data.py disaster_messages.csv disaster_categories.csv Disaster_Response.db )
    2. To run the ML pipeline for data loading for Database, training the model (classifier), and exporting the classifier as a pickle file: 
    ( python train_classifier.py ../data/Disaster_Response.db classifier.pkl )
    3. in order to run the web app, you must run the (run.py) file. 
    
    Then visit this link : (https://view6914b2f4-3001.udacity-student-workspaces.com/).


#### Acknowledgment 
A special thanks to Udacity and Misk Academy for giving me the opportunity to learn, explore and use some data science-related skills.
Also, the appreciation goes to Fifure 8 company for offering the dataset.
Thanks to our mentor Mr. Haroon.
