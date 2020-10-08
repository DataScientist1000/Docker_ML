# -*- coding: utf-8 -*-


"""
Pickling : A Python object can be saved as a binary file so that we can load 
it at a later point of time and leverage all its properties that are there now
our RF has trained with right paramenter  
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

import pickle

# loading the dataset

iris = load_iris()
X = iris.data
y = iris.target

#split the data
X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=42, 
                                               test_size = 0.5)

#Build the model
clf = RandomForestClassifier(n_estimators=10)

# Train the classifier
clf.fit(X_train,y_train)

# predictions 
predicted = clf.predict(X_test)

#Check accuracy 
print(accuracy_score(predicted, y_test))

#pickling the code
with open('rf.pkl','wb') as model_pkl:
    pickle.dump(clf, model_pkl)
     
      


