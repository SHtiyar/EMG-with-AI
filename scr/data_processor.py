import pandas as pd
import numpy as np
import torch.tesor as tensor

class DataProcessor:
    """
    Comprehensive data processing for EMG gesture datasets
    
    Handles:
    - File reading
    - Class clustering
    - Data normalization
    """
    def __init__(self, data_path):
        self.data_path = data_path
    
    def read_files(self, file_list):
        """
        Read and process multiple EMG data files
        
        Args:
            file_list (list): List of file names to process
        
        Returns:
            list: Processed datasets with class and normalized data
        """
        processed_data = []
        for filename in file_list:
            data = pd.read_table(self.lokasi_data + filename)
            del data['time']
            data = data[data['class'] > 0]
            Data = data
            Data['class'] = data['class'] - 1
            Data.reset_index(inplace = True)
            dataframes = self.cluster_class_data(Data)
            df_list = self.separate_class_data(dataframes)

            processed_data.extend(df_list)
            pass
        return processed_data

    def cluster_class_data(self, dataframe):
        dataframes = []
        current_class = None
        start_index = 0

        for index, row in dataframe.iterrows():
            if current_class is None or current_class != row['class']:
                if current_class is not None:
                    dataframes.append(dataframe.iloc[start_index:index])
                current_class = row['class']
                start_index = index
            pass

        dataframes.append(dataframe.iloc[start_index:])
        return dataframes

    def separate_class_data(self, dataframes):
        df_list = []

        for df in dataframes:
            class_value = int(df['class'].mode().iloc[0])
            data = df.iloc[:, 1:9].values
            data_swapped = np.swapaxes(data, 0, 1)

            df_list.append({"class": class_value, "data": data_swapped})

        return df_list
    
    def normalize_data(self, data):
        """
        Normalize sequential EMG data
        
        Args:
            data (np.array): Raw EMG signal data
        
        Returns:
            np.array: Normalized data
        """
        # Add normalization logic
        
        pass
