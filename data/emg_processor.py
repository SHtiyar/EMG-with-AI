"""EMG Data Processing Pipeline

Objective: Process and validate EMG datasets with organized data management

Key Components:
- Directory Management
- Data Validation
- Path Collection
- Structured Output

Methodology:
* Recursive file traversal
* Class-based validation
* Systematic data organization
* Localized pickle storage"""

import os
import pickle
import pandas as pd
from typing import List, Dict, Tuple

class EMGFileProcessor:
    """Process EMG datasets with systematic validation and filtering
    
    Key Features:
    - Recursive directory traversal
    - Data integrity validation
    - 7-class filtering mechanism
    - Local pickle storage
    
    Example Usage:
    >>> processor = EMGFileProcessor("EMG_data_for_gestures-master")
    >>> valid_paths, class_counts = processor.process_files()
    >>> processor.save_paths(valid_paths)
    """
    
    def __init__(self, root_folder: str):
        """Initialize processor with directory management
        
        Args:
            root_folder (str): Root directory for EMG data
        
        Setup Steps:
        1. Validate input path
        2. Create processed directory
        3. Set up output paths
        """
        self.root_folder = root_folder
        self.processed_dir = os.path.join(root_folder, 'processed')
        
        # Create processed directory
        if not os.path.exists(self.processed_dir):
            os.makedirs(self.processed_dir)
    
    def process_files(self) -> Tuple[List[str], Dict[str, int]]:
        """Process and validate EMG data files
        
        Returns:
            Tuple[List[str], Dict[str, int]]: 
                - List of valid file paths (7 classes)
                - Dictionary of class counts for all files
        
        Processing Steps:
        1. Recursive directory traversal
        2. File content validation
        3. Class count verification
        4. Statistics collection
        """
        valid_paths = []
        class_counts = {}
        
        for subdir, _, files in os.walk(self.root_folder):
            if 'processed' in subdir:
                continue
                
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(subdir, file)
                    
                    try:
                        # Validate data structure
                        df = pd.read_table(file_path)
                        if 'class' in df.columns:
                            unique_classes = len(df['class'].unique())
                            class_counts[file_path] = unique_classes
                            
                            # Filter for 7 classes
                            if unique_classes == 7:
                                valid_paths.append(file_path)
                                
                    except Exception as e:
                        print(f"Validation Error ({file_path}): {e}")
        
        return sorted(valid_paths), class_counts
    
    def save_paths(self, valid_paths: List[str], filename: str = 'valid_emg_paths.pkl') -> str:
        """Save validated paths to local processed directory
        
        Args:
            valid_paths (List[str]): Valid file paths
            filename (str): Output filename
        
        Returns:
            str: Path to saved pickle file
        
        Storage Format:
        - Binary pickle file
        - List of absolute paths
        - Sorted alphabetically
        """
        output_path = os.path.join(self.processed_dir, filename)
        with open(output_path, 'wb') as f:
            pickle.dump(valid_paths, f)
        return output_path

def main():
    """Execute main processing workflow
    
    Workflow Steps:
    1. Input validation
    2. File processing
    3. Statistics display
    4. Path export
    """
    # Initialize processor
    root_folder = input("Enter the folder path: ")
    processor = EMGFileProcessor(root_folder)
    
    # Process files
    print("\nProcessing EMG data files...")
    valid_paths, class_counts = processor.process_files()
    
    # Display statistics
    print(f"\nProcessing Summary:")
    print(f"Total files analyzed: {len(class_counts)}")
    print(f"Files with 7 classes: {len(valid_paths)}")
    
    # Show samples
    print("\nSample of valid files:")
    for path in valid_paths[:5]:
        print(f"- {path}")
    if len(valid_paths) > 5:
        print("...")
    
    # Show invalid files
    print("\nFiles with incorrect class counts:")
    for path, count in class_counts.items():
        if count != 7:
            print(f"- {path}: {count} classes")
    
    # Save results
    output_path = processor.save_paths(valid_paths)
    print(f"\nValid paths saved to: {output_path}")

if __name__ == "__main__":
    main()
