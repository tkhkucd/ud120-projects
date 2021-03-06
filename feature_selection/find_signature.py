#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
#tkhkuchd 05/23/18 r->rb for Pytho3 adaptation
word_data = pickle.load( open(words_file, "rb"))
authors = pickle.load( open(authors_file, "rb") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train,labels_test = cross_validation.train_test_split(word_data,authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')

#print("Before vectorizer.fit_transform(features_train): ", features_train[0], "\n")

features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

#print("After vectorizer.fit_transform(features_train): ", features_train[0])



### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]




### your code goes here
from sklearn import tree
clf = tree.DecisionTreeClassifier()
print("features_train[0]", features_train[0],\
    "labels_train[0]", labels_train[0])
clf.fit(features_train, labels_train)
print("score:", clf.score(features_test, labels_test))
print("number of training data:",len(features_train))
print("feature_importances_:",clf.feature_importances_, "\n"\
    "len of feature_importances_:", len(clf.feature_importances_), "\n"\
    "max of feature_importances_:", max(clf.feature_importances_), "\n"\
    "index of max of feature importance:", numpy.argmax(clf.feature_importances_), "\n")

#Lesson12 Quiz 28, tkhkucd 05/24/2018
feature_names = vectorizer.get_feature_names()
print("len of feature_names: ", len(feature_names), "feature_names[most important] :", \
    feature_names[numpy.argmax(clf.feature_importances_)],"\n")

#Lesson12, Quiz30,tkhkucd 05/24/2018
cnt=0
index=0
for imp in clf.feature_importances_:
    if imp>0.2:
        cnt+=1
        print("index: ", index,"cnt :", cnt, " feature_name :", feature_names[index],"\n")
    index+=1
