#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]

# removing key=TOTAL
del data_dict['TOTAL']
del data_dict['SKILLING JEFFREY K']
del data_dict['LAY KENNETH L']
del data_dict['FREVERT MARK A']
del data_dict['PICKERING MARK R']

data = featureFormat(data_dict, features)


### your code below
print ("DATA DICT")
#print (data_dict)
max_salary=0

for key_name in data_dict.keys():
    print(key_name)
    if (data_dict[key_name]['salary']!="NaN") and (data_dict[key_name]['salary'] > max_salary) :
        name_of_max_salary = key_name
        max_salary = data_dict[key_name]['salary']

print("Name of max salary", name_of_max_salary, "max salary", max_salary)


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    print("salary", salary, "bonus",bonus)


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
