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

folder = input("folder path")

files = os.listdir(folder)
datasets = [f for f in files if os.path.isfile(folder+'/'+f)]


for f in files:
  
```
