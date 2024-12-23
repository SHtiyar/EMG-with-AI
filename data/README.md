**NOTE : all of my filtered files already uploaded in my drive, because my device is potato laptop**

# EMG Data Processing Pipeline

## Project Overview

Automated processing system for EMG (Electromyography) datasets with class-based validation

## Objective

Develop a robust data processing pipeline for EMG gesture recognition datasets

## Key Components

- Recursive File Collection
- Data Validation
- Class-based Filtering
- Structured Output Management

## Features

- Automated directory traversal
- Systematic data validation
- 7-class filtering mechanism
- Organized pickle storage
- Documentation and logging

## Directory Structure

```
EMG_data_for_gestures-master/
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
├── processed/
|   └── valid_emg_paths.pkl
└── README.txt
```

## Usage

1. Run the processor:
```
python emg_processor.py
```
2. Enter the root directory path when prompted
3. The script will:

- Process all .txt files recursively
- Validate files for 7 unique classes
- Create a 'processed' directory
- Save valid file paths to pickle format

4. Load processed paths in your projects:
```
import pickle
import os

processed_dir = os.path.join("your_input_path", "processed")
pickle_path = os.path.join(processed_dir, "valid_emg_paths.pkl")

with open(pickle_path, 'rb') as f:
    valid_paths = pickle.load(f)
```

## Validation Criteria
- Files must be in .txt format
- Must contain 'class' column
- Must have exactly 7 unique classes
- Must be readable by pandas

## Output Structure
- Creates 'processed' subdirectory
- Saves pickle file with valid paths
- Maintains absolute path references
- Provides processing statistics

## Error Handling
- Validates input directory
- Handles file reading errors
- Reports invalid class counts
- Creates missing directories

## Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
