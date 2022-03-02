import sys

import nltk
nltk.download(['punkt','stopwords'])
nltk.download('wordnet')

# import libraries
import pandas as pd
import numpy as np
import sqlite3
import re

from sqlalchemy import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion

from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

from sklearn.ensemble import AdaBoostClassifier

from sklearn.model_selection import GridSearchCV

from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import make_scorer


def load_data(database_filepath):
    
    path = 'sqlite:///' + database_filepath 
    df = pd.read_sql('Disaster_Response', path)
    
    target = df[['related', 'request', 'offer', 'aid_related', 'medical_help', 'medical_products',
    'search_and_rescue', 'security', 'military', 'child_alone', 'water', 'food', 'shelter',
    'clothing', 'money', 'missing_people', 'refugees', 'death', 'other_aid', 'infrastructure_related',
    'transport', 'buildings', 'electricity', 'tools', 'hospitals', 'shops', 'aid_centers', 'other_infrastructure',
    'weather_related', 'floods', 'storm', 'fire', 'earthquake', 'cold', 'other_weather', 'direct_report']]
    
    X = df['message']
    Y = target
    
    return X, Y


def tokenize(text):
    text = re.sub(r"[^a-zA-Z]"," ",text.lower())
    words = word_tokenize(text)
    lemm = [WordNetLemmatizer().lemmatize(w) for w in words if w not in stopwords.words('english') ]
    return lemm


def build_model():
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ]))
            
        ])),

        ('classifier', MultiOutputClassifier(AdaBoostClassifier()))
    ])
    return pipeline


def evaluate_model(model, X_test, Y_test, Y):
    predicted = model.predict(X_test)
    print(classification_report(Y_test.iloc[:,1:].values, np.array([x[1:] for x in predicted]), 
                                target_names=Y.columns))
        
def tuning_model(model, X_train, Y_train, Y_test):
    
    parameters = {'classifier__estimator__learning_rate': [0.01, 0.02, 0.05],
              'classifier__estimator__n_estimators': [10, 20, 40]}
    grid_obj = GridSearchCV(estimator=model, param_grid=parameters, scoring='f1_micro', n_jobs=-1)
    grid_obj.fit(X_train, Y_train)
    Y_test_pred = grid_obj.predict(X_test)
    display_results(Y_test, Y_test_pred)
    
    return grid_obj

def save_model(tuned_model, model_filepath):
  
    filename = 'classifier.pkl'
    pickle.dump(tuned_model, open(filename, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y = load_data(database_filepath)
        
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, Y)
        
        print('Tuning model...')
        tuned_model = tuning_model(model, X_train, Y_train, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(tuned_model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()