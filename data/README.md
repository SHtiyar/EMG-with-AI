# NOTE : all of my filtered files already uploaded in my drive, because my device is potato laptop

the files that i uses already filtered and use 50 files from 72 files.

if you download the original files, the original folder structure will be like
```
/EMG_data_for_gestures-master/
|
├── 01/
│   └── 1_raw_data_13-12_22.03.16.txt
│   └── 2_raw_data_13-13_22.03.16.txt
│
├── 02/
│   └── 1_raw_data_14-19_22.03.16.txt
│   └── 2_raw_data_14-21_22.03.16.txt
.
.
.
├── 36/
│   └── 1_raw_data_13-03_15.04.16.txt
│   └── 2_raw_data_13-04_15.04.16.txt
```
the firs step is to moves alt .txt files in one folder and filter the files with 7 classes and 8 classes with simple python code

```
import os
import pandas as pd

# Input folder path
folder = input("Enter the folder path: ")

# List all files in the folder
files = os.listdir(folder)
datasets = [f for f in files if os.path.isfile(os.path.join(folder, f))]

# Define the function
def finder(files):
    for file_name in files:
        try:
            # Construct the file path
            file_path = os.path.join(folder, file_name)
            
            # Read the table
            txt_f = pd.read_table(file_path)
            
            # Check if the DataFrame has a 'class' column and evaluate its unique class count
            if 'class' in txt_f.columns:
                unique_classes = len(txt_f['class'].unique())
                if unique_classes == 8:
                    print(f"{file_name} has 8 unique classes.")
                else:
                    print(f"{file_name} has {unique_classes} unique classes.")
            else:
                print(f"Column 'class' not found in {file_name}.")
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

# Call the function
finder(datasets)

```
