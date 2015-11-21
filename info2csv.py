#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: info2csv.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Sat Nov 21 22:44:37 2015
#########################################################################

import os
import sys
import csv
import pymongo

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'o2o_info')

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]

def output_info_to_csv(file_name):
    row_keys = ['Supplier Name', 'Phone Numbers', 'Address', 'Open Time']
    with open(file_name, 'wb') as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(row_keys)
        suppliers = get_all_suppliers()

        for supplier in suppliers:
            csv_writer.writerow([supplier['supplierName'], supplier['contactPhone'], supplier['address'], supplier['operateStartTime']+'-'+supplier['operateEndTime']])


def get_all_suppliers():
    return db['suppliers'].find()

if __name__ == '__main__':
    output_file_name = sys.argv[1]
    if output_file_name:
        output_info_to_csv(output_file_name)

