import sys
import pandas as pd
from sqlalchemy import *
import sqlite3


def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv('/home/workspace/data/disaster_messages.csv')
    categories = pd.read_csv('/home/workspace/data/disaster_categories.csv')
    #merging the two datasets
    data = pd.merge(messages, categories)
    return data


def clean_data(data):
    #Creating multiple categories columns out of the original category column
    categories = data['categories'].str.split(pat=';', n=0, expand=True)
    
    #creating headings for the created categories
    #assigning the first record to a variable
    row = categories.head(1)
    
    # removing any values from the headings excpet the category name itself
    category_colnames = []
    for i in row:
        category_colnames.append(str(row.loc[0,i])[slice(-2)])
     
    
    #Assigning the categories names to the categories columns
    categories.columns = category_colnames
    
    #cleaning the categories values by removing names and leaving the binary values.
    for i in categories:
        categories[i] = categories[i].str[-1:]
    
    #Converting the values types to integers.
    categories = categories.astype(str).astype(int)
    
    # drop category column from df
    data = data.drop(labels='categories', axis=1)
    
    # append the categories dataset to the merged dataset
    df = pd.concat([data, categories], axis=1, join='inner')
    
    #dropping the duplicates since they represent a small percentage of total dataset
    df = df.drop_duplicates()
    
    # Dropping the 'Original' column since it has a lots of null values
    # and it is written in Español (will not be used in analysis)
    df = df.drop(labels=['original'], axis=1)
    
    #deleting the '2' values from related columns since it will affect the ML model results
    df = df[df.related != 2]
    
    return df


def save_data(df, database_filename):
    #Saving the clean dataset into an sqlite database
    engine = create_engine('sqlite:///Disaster_Response.db')
    df.to_sql('Disaster_Response', engine, if_exists='replace', index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
            
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()