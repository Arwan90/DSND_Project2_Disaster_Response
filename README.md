### DSND_Project2_Disaster_Response_Pipeline

#### +----------> This Project is dedicated for the Data Scientist Nano Degree | Udacity <----------+

#### Table of contents
* General Information
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
