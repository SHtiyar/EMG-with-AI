import torch.nn as nn

class VariableCNN(nn.Module):
    """
    Adaptive Convolutional Neural Network for EMG Gesture Classification
    
    Architecture:
    - 1D Convolution Layer
    - Batch Normalization
    - Adaptive Max Pooling
    - Fully Connected Layers
    """
    def __init__(self, num_classes=6):
        super(VariableCNN, self).__init__()
        self.conv01 = nn.Sequential(
            nn.Conv1d(8, 32, kernel_size = 3, padding = 2),
            nn.BatchNorm1d(32),
            nn.ReLU(),
        )

        self.fc = nn.Sequential(
            nn.Linear(32 * 32, 128),
            nn.ReLU(),
            nn.Dropout(0.25),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
        )
        self.Classifikasi = nn.Sequential(
            nn.Linear(16, 6),
        )

        self.flat = nn.Flatten()
        self.globmaxpool = nn.AdaptiveMaxPool1d(32)
        pass
    
    def forward(self, x):
        x = self.conv01(x)
        x = self.globmaxpool(x)
        x = self.flat(x)
        x = self.fc(x)
        x = self.Classifikasi(x)
        pass
