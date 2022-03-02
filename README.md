### DSND_Project2_Disaster_Response_Pipeline

#### +----------> This Project is dedicated for the Data Scientist Nano Degree | Udacity <----------+

#### Table of contents
* General Information
* The file Structure of the project
* Files available
* Dataset used
* Tools used
* Findings
* Acknowledgment 
* Resources

#### General Information
In this project, two datasets were cleaned, combined, and processed. The resulted dataset was used to train a machine learning pipeline.
The Machine Learning Pipeline went through a tuning process using GridSearchCV.
The final result is a web app that takes messages as input, analyzes them using the tuned ML Pipeline, and categorizes the message according to 36 available categories.

#### The file structure of the project

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md


#### Files available
* A messages Dataset (From Figure 8 company) : 26248 Records x 4 Columns
* A categories Dataset (From Figure 8 company) : 26248 Records x 2 Columns
* ReadMe file
* Jupyter notebook file (.ipynb)

#### Dataset used
Seattle Airbnb | The dataset was retrieved from Kaggle (https://www.kaggle.com/airbnb/seattle)

#### Tools used
##### Jupyter Notebook
* Python Version: 3.6.5
* Pandas Version: 0.23.0

##### Python Libraries Used
* pandas 
* matplotlib
* seaborn

#### Findings

After analyzing Seattle Airbnb Dataset and imposing three business questions, we can say that downtown got the highest renting price compared to other neighborhoods. We also can conclude that having more guests included in renting process will increase the total renting price. On the other hand, not verifying an Airbnb account with a phone number or a profile picture might be a factor in increasing renting prices by hosts.

#### Acknowledgment 
A big thanks to Udacity and Misk Academy for giving me the opportunity to learn, explore and use some data science-related skills.
Also, the appreciation goes to kaggle for offering the dataset.


#### Useful Resources
###### Project Link :  https://github.com/Arwan90/DSND_Project1_Seattle_AirBnB.git
###### Medium blog for the project : https://medium.com/@rawanalmakinah/analyzing-seattle-airbnb-dataset-using-python-libraries-5b8dd1801fe3
