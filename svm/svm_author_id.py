#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]


#########################################################
### your code goes here ###
from sklearn import svm
#clf=svm.SVC(kernel="linear")
clf=svm.SVC(kernel="rbf", C=10000.0)

print("start fit: rbf, C=10000.0")
t0=time()
clf.fit(features_train, labels_train)
print ("training time : ", round(time()-t0), "s")

t1=time()
pred = clf.predict(features_test)
print("prediciton time : ", round(time()-t1), "s")

print ("prediction 10:", pred[10], " 26:", pred[26], " 50:", pred[50])

accuracy = clf.score(features_test, labels_test)
print ("Accuracy : ", accuracy)

num_of_chris_mail=0
for name in pred:
    if name==1:
        num_of_chris_mail+=1

print ("number of Chris's mail :", num_of_chris_mail)
#########################################################
