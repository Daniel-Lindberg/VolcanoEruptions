# Author: Daniel Lindberg
"""
Description of kaggle project: kaggle.com/c/predict-volcanic-eruptions-ingv-oe/overview
"""

# Native python imports
import ast
import csv
#import keras
import os

import tensorflow as tf

# Native python submodules
#from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


# Gets a list of the absolute file paths underneath a file_structure
def absoluteFilePaths(some_dir):
    all_files = []
    for dir_path,_,file_names in os.walk(some_dir):
        for single_file in file_names:
            all_files.append(os.path.abspath(os.path.join(dir_path, single_file)))
    return all_files

class VolcanoTrainer():

    def __init__(self):
        data_dir = "data"

        test_dir = data_dir+os.sep+"test"
        train_dir = data_dir+os.sep+"train"

        train_csv_path = os.path.join(data_dir,"train.csv")


        amount_of_sensors = 10

        # Going to be our tuple for segment_id and time to eruption
        self.train_tuple_list = []

        self.temp_count = 5
        count = 0
        with open(train_csv_path) as csv_file:
            train_reader = csv.reader(csv_file, delimiter=',', quotechar="|")
            # train_reader has two columns: segment_id,time_to_eruption
            next(train_reader, None) # Skip the header
            for row in train_reader:
                if count > self.temp_count:
                    continue
                # the dict with all sensor information associated with an entry
                sensor_dict = {}
                # list of all sensors
                sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6, sensor_7, sensor_8, sensor_9, sensor_10 = [],[],[],[],[],[],[],[],[],[]
                # open train csv, read all sensor data
                with open(train_dir+os.sep+row[0]+".csv") as train_file:
                    segment_reader = csv.reader(train_file, delimiter=',', quotechar="|")
                    # train_reader has ten columns: sensors[1-10]
                    next(segment_reader, None) # Skip the header    
                    for train_row in segment_reader:
                        for x in range(1, len(train_row)+1):
                            eval("sensor_{0}".format(x)).append(train_row[x-1])
                # put sensor information into dict
                for x in range(1, amount_of_sensors+1):
                    sensor_dict["sensor_{0}".format(x)] = eval("sensor_{0}".format(x))
                # put segment_id and time_to_eruption into dict
                sensor_dict["segment_id"] = int(row[0])
                sensor_dict["time_to_eruption"] = int(row[1])
                self.train_tuple_list.append(sensor_dict)
                count += 1

    def trainModel(self):
        batch_size =  self.temp_count
        #TODO: write entire function         
        
        

if __name__ == "__main__":
    vt = VolcanoTrainer()
    
                


