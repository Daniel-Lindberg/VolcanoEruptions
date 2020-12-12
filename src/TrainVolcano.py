# Author: Daniel Lindberg
"""
Description of kaggle project: kaggle.com/c/predict-volcanic-eruptions-ingv-oe/overview
"""

# Native python imports
import csv
import keras
import os

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

        self.test_files = absoluteFilePaths(test_dir)
        self.train_Files = absoluteFilePaths(train_dir)  

        train_csv_path = os.path.join(data_dir,"train.csv")

        # Going to be our tuple for segment_id and time to eruption
        self.train_tuple_list = []

        with open(train_csv_path, newline='') as csv_file:
            train_reader = csv.reader(csv_file, delimiter=',', quotechar="|")
            # train_reader has two columns: segment_id,time_to_eruption
            next(train_reader, None) # Skip the header
            for row in train_reader:
                self.train_tuple_list.append([int(row[0]), int(row[1])])
        

if __name__ == "__main__":
    vt = VolcanoTrainer()
    
                


