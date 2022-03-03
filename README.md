### DSND_Project2_Disaster_Response_Pipeline

#### +----------> This Project is dedicated to the Data Scientist Nano Degree | Udacity <----------+

#### Table of contents
* [General Information](#general)
* [Files available](#files)
* [Dataset used](#data)
* [Tools used](#tools)
* [Useful information](#info)
* [Program Execution Process](#exe)
* [Acknowledgment](#ack)


#### General Information
<a name="general"/> 

In this project, two datasets were cleaned, combined, and processed. The resulted dataset was used to train a machine learning pipeline.
The Machine Learning Pipeline went through a tuning process using GridSearchCV.
The final result is a web app that takes messages as input, analyzes them using the tuned ML Pipeline, and categorizes the message according to 36 available categories.
This web app is helpful for organizations that work in a disaster/response field. It will facilitate categorizing the received messages and direct the message to the category-related organization.


#### Files available
<a name="files"/>

* A message Dataset (messages.csv | From Figure 8 company) : 26248 Records x 4 Columns
* A categories Dataset (categories.csv | From Figure 8 company) : 26248 Records x 2 Columns
* A Python file for data processing (process_data.py)
* A resulting database that contains the cleaned table (Disaster_Response.db) with a Disaster_Response table.
* A python file that has the Machine Learning Pipeline (train_classifier.py).
* A pickle file that has the tuned ML Pipeline (classifier.pkl).
* A python file for rendering the web app pages (run.py).
* Two HTML files for formatting the web app pages (go.html | master.html).
* ReadMe file

app

| - template

| |- master.html # main page of web app

| |- go.html # classification result page of web app

|- run.py # Flask file that runs app

data

|- disaster_categories.csv # data to process

|- disaster_messages.csv # data to process

|- process_data.py

|- Disaster_Response.db # database to save clean data to

models

|- train_classifier.py

|- classifier.pkl # saved model

README.md


#### Dataset used
<a name="data"/>
messages & categories | The datasets were provided by Figure 8 company.

#### Libraries and Tools used
<a name="tools"/>
1. <b>Jupyter Nootebook</b>

* Python Version: 3.6.5
* Pandas Version: 0.23.0
* NLP Library: NLTK
* ML Libraries: NumPy, SciPy, Pandas, Sciki-Learn
* SQLlite Database Library: SQLalchemy
* Data Visualization: Flask, Plotly

2. <b>Udacity IDE</b>


#### Useful information: 
<a name="info"/>
+ <b>Web App Link</b> :  https://view6914b2f4-3001.udacity-student-workspaces.com/


#### Program Execution Process :
<a name="exe"/>
To create the database, train, and save the model, follow these instructions: 

1. To run ETL pipeline for data cleaning and saving: 

  `python process_data.py disaster_messages.csv disaster_categories.csv Disaster_Response.db`
 
2. To run the ML pipeline for data loading for the Database, training the model (classifier), and exporting the classifier as a pickle file: 

  `python train_classifier.py ../data/Disaster_Response.db classifier.pkl`

3. in order to run the web app, you must run the (run.py) file. 
    
    Then visit this link : (https://view6914b2f4-3001.udacity-student-workspaces.com/).


#### Acknowledgment
<a name="ack"/>
A special thanks to Udacity and Misk Academy for giving me the opportunity to learn, explore and use some data science-related skills.
Also, the appreciation goes to Figure 8 company for offering the dataset.
Thanks to our mentor Mr. Haroon.
