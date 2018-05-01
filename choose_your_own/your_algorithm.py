#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

# Naive_Bayes classifier TU
from sklearn.naive_bayes import GaussianNB

t0=time()
print("Start GaussianNB")
clf=GaussianNB()
clf=clf.fit(features_train, labels_train)
print("GaussianNB() finish fit() time=", round(time()-t0))
pred=clf.predict(features_test)
print("GaussianNB() finish predict() time=", round(time()-t0))
acc=clf.score(features_test, labels_test)
print("GaussianNB() finish score() accuracy=",acc," time=", round(time()-t0))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

# SVM classifier TU
from sklearn import svm
t0=time()
print("start SVM")
clf=svm.SVC(kernel="rbf", C=100000.0)
clf.fit(features_train, labels_train)
print("SVM finish fit, time=", round(time()-t0))
clf.predict(features_test)
print("SVM finish predict, time=",round(time()-t0))
acc= clf.score(features_test, labels_test)
print("SVM finish score() accuracy=",acc," time=", round(time()-t0))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

# Decision tree
from sklearn import tree
t0=time()
print("start Decision tree")
clf=tree.DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)
print("Decision tree finish fit, time=", round(time()-t0))
clf.predict(features_test)
print("Decision tree finish predict, time=",round(time()-t0))
acc= clf.score(features_test, labels_test)
print("Decision tree finish score() accuracy=",acc," time=", round(time()-t0))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

# K nearest Neughbor
from sklearn.neighbors import KNeighborsClassifier
t0=time()
print("start K nearest Neighbors")
clf=KNeighborsClassifier()
clf.fit(features_train, labels_train)
print("K neighbors finish fit, time=", round(time()-t0))
clf.predict(features_test)
print("K neighbors finish predict, time=",round(time()-t0))
acc= clf.score(features_test, labels_test)
print("K Neighbors finish score() accuracy=",acc," time=", round(time()-t0))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

 #AbaBoost
from sklearn.ensemble import AdaBoostClassifier
t0=time()
print("start Adaboost")
clf=AdaBoostClassifier()
clf.fit(features_train, labels_train)
print("Ada boost finish fit, time=", round(time()-t0))
clf.predict(features_test)
print("Adaboost finish predict, time=",round(time()-t0))
acc= clf.score(features_test, labels_test)
print("AdaBoost finish score() accuracy=",acc," time=", round(time()-t0))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

#Ramdom forest
from sklearn.ensemble import RandomForestClassifier
t0=time()
print("start RamdomForest")
clf=RandomForestClassifier(n_estimators=50)
clf.fit(features_train, labels_train)
print("Randomforest finish fit, time=", round(time()-t0))
clf.predict(features_test)
print("Randomforest finish predict, time=",round(time()-t0))
acc= clf.score(features_test, labels_test)
print("Randomforest finish score() accuracy=",acc," time=", round(time()-t0))

try:
   prettyPicture(clf, features_test, labels_test)
except NameError:
   pass
