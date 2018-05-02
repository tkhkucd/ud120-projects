#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("length of enron_data:", len(enron_data))
#print("length of enron_data.keys():", enron_data.keys())
print("length of enron_data.keys() of len:", len(enron_data.keys()))
poi_count=0
qualified_sarary_count=0
qualified_emailaddress_count=0
total_payments_NaN_count=0

for person in list(enron_data.keys()):
    if enron_data[person]["poi"]:
        poi_count+=1
    if enron_data[person]["salary"]!="NaN":
        qualified_sarary_count+=1
    if enron_data[person]["email_address"]!='NaN':
        qualified_emailaddress_count+=1
    if enron_data[person]["total_payments"]=="NaN":
        total_payments_NaN_count+=1;


print("numner of poi_count:", poi_count)
print("numner of qualified_sarary_count:", \
    qualified_sarary_count)
print("numner of qualified_emaila_count:", \
    qualified_emailaddress_count)
print("number of total_payments_NaN_count: ",\
    total_payments_NaN_count, " : ", total_payments_NaN_count/len(enron_data))

print("total stock of James Prentice : " \
    ,enron_data["PRENTICE JAMES"]["total_stock_value"])
print("from Wesley Colwell to poi: " \
    ,enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("stock option exercised of Jeffrey K Skilling : " \
    ,enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print("Jeffrey K Skilling - total payment : ",\
    enron_data["SKILLING JEFFREY K"]["total_payments"])
print("Kenneth Lay -total payment : ",\
    enron_data["LAY KENNETH L"]["total_payments"])
print("Andrew S Fastow - total payment : ",\
    enron_data["FASTOW ANDREW S"]["total_payments"])


#MORAN MICHAEL P
#print("content of James Prentice : ",enron_data["MORAN MICHAEL P"])

#import csv
#pcount=0
#with open ("../final_project/poi_names.txt", 'rt') as fin:
#
#    poireader = csv.reader(fin, delimiter=' ')
#        print(row)
#        pcount+=1
#    print ("pcount:",pcount)


#print("enron_data[SKILLING JEFFREY K].keys():",\
# enron_data["SKILLING JEFFREY K"].keys())
#print("enron_data[SKILLING JEFFREY K].keys() length:", len(enron_data["SKILLING JEFFREY K"].keys()))
