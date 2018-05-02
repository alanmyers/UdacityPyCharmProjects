from typing import Type

from sklearn.naive_bayes import GaussianNB


def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    ### your code goes here!
    from sklearn.naive_bayes import GaussianNB
    clf: Type[GaussianNB] = GaussianNB()
    clf.fit(X=features_train, y=labels_train)
    return clf
