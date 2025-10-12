
import os

data_folder = 'data/' # path to the data folder

if os.path.exists(data_folder): # Check if it exists
    print ("the 'data'folder exists!")
else:
    print ("the 'data'folder does not exists!")