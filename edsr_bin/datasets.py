import glob
import numpy as np
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms

# Normalization parameters for pre-trained PyTorch models
"""
mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])
"""
mean = np.array([0.5, 0.5, 0.5])
std = np.array([0.5, 0.5, 0.5])


class ImageDataset(Dataset):
    def __init__(self, root, hr_shape):
        self.transform = transforms.Compose(
            [
                transforms.Normalize(mean, std),
            ]
        )

        self.lr_files = sorted(glob.glob(root + "bin_32/*"))
        self.hr_files = sorted(glob.glob(root + "bin_128/*"))

    def __getitem__(self, index):

        lr_bin = np.load(self.lr_files[index % len(self.lr_files)])
        hr_bin = np.load(self.hr_files[index % len(self.hr_files)])
        
        lr_bin = torch.from_numpy((lr_bin/np.max(np.abs(lr_bin))).astype(np.float32)).clone()
        hr_bin = torch.from_numpy((hr_bin/np.max(np.abs(hr_bin))).astype(np.float32)).clone()
        img_lr = self.transform(lr_bin)
        img_hr = self.transform(hr_bin)
        

        return {"lr": img_lr, "hr": img_hr}

    def __len__(self):
        return len(self.lr_files)