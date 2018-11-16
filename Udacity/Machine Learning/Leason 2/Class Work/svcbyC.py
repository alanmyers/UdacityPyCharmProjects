#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
import pickle

from time import time
from sklearn.externals import joblib

#sys.path.append("C:\\Users\\amyer\\PycharmProjects\\Udacity\\Machine Learning\\Leason 2\\ud120-projects\\tools")
#   Project:... > Project Interpreter. Now, in the main pane on the right,
#   click the settings symbol (gear symbol) next to the field for "Project Interpreter".
#   Choose More in the menu that pops up.
# print("SysPath = ", sys.path)
from email_preprocess import preprocess
import numpy as np
import matplotlib.pyplot as plt



print("### Import Complete")

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
print("### past PreProcess)")





#########################################################
### your code goes here ###
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import matplotlib.pyplot as plt

train_and_store = True

if (train_and_store):
    print("### Starting classifier C=1")

    clf = SVC(kernel="rbf", C=1, gamma='auto')
    t0 = time()
    clf.fit(features_train, labels_train)
    print ("### Training time:", round(time() - t0,3), "s")
    t0 = time()
    accuracy = clf.score(features_test, labels_test)
    print (" Accuracy = ", accuracy, " (Time ", round(time() - t0), ")")
    t0 = time()
    pred = clf.predict(features_test)
    print ("Predict Time ", round(time() - t0), ")")

    # Save for later plotting
    #
    pickle.dump(clf, open('svc_rbf_c0.sav', 'wb'))
    joblib.dump(clf, 'svc_rbf_c0.joblib')

    #########################################################
    print("### Starting classifier c=100")

    clf = SVC(kernel="rbf", C=100, gamma='auto')
    t0 = time()
    clf.fit(features_train, labels_train)
    print ("### Training time:", round(time() - t0,3), "s")
    t0 = time()
    accuracy = clf.score(features_test, labels_test)
    print (" Accuracy = ", accuracy, " (Time ", round(time() - t0), ")")
    t0 = time()
    pred = clf.predict(features_test)
    print ("Predict Time ", round(time() - t0), ")")
    # Save for later plotting
    #
    pickle.dump(clf, open('svc_rbf_c100.sav', 'wb'))
    joblib.dump(clf, 'svc_rbf_c100.joblib')
else:
    files = (["svc_rbf_c0.joblib", 'svc_rbf_c100.joblib'])
    for file in files:
        print("Processing " + file)
        clf = joblib.load(file)
        t0 = time()
        accuracy = clf.score(features_test, labels_test)
        print (" Accuracy = " + accuracy + " (Time " + round(time() - t0) + ")")
        t0 = time()
        pred = clf.predict(features_test)
        print ("Predict Time " + round(time() - t0) + ")")


