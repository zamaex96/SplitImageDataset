# Data Splitting Script Explanation

This Python script is designed to split a dataset of images into training and validation sets. It's particularly useful for preparing data for machine learning tasks, especially in computer vision projects. Here's a detailed breakdown of how the script works:

## Imports

```python
import os
import shutil
import random
```

- `os`: Used for file and directory operations.
- `shutil`: Used for high-level file operations like copying.
- `random`: Used to shuffle the list of files for randomized splitting.

## Main Function: `split_data`

```python
def split_data(input_folder, output_folder, train_split=0.7):
```

This function is the core of the script. It takes three parameters:
- `input_folder`: The path to the folder containing the original dataset.
- `output_folder`: The path where the split dataset will be saved.
- `train_split`: The proportion of data to use for training (default is 0.7, or 70%).

## Creating Output Directories

```python
train_folder = os.path.join(output_folder, 'train')
val_folder = os.path.join(output_folder, 'test')
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
```

This part creates 'train' and 'test' folders within the output directory. The `exist_ok=True` parameter ensures the script doesn't raise an error if the folders already exist.

## Iterating Through Subfolders

```python
for subfolder in os.listdir(input_folder):
    subfolder_path = os.path.join(input_folder, subfolder)
    if os.path.isdir(subfolder_path):
        # ... (rest of the code)
```

This loop goes through each subfolder in the input directory. It's designed to handle a dataset where images are organized into subfolders, typically representing different classes.

## Creating Corresponding Subfolders

```python
train_subfolder = os.path.join(train_folder, subfolder)
val_subfolder = os.path.join(val_folder, subfolder)
os.makedirs(train_subfolder, exist_ok=True)
os.makedirs(val_subfolder, exist_ok=True)
```

For each subfolder in the input directory, corresponding subfolders are created in both the train and test (validation) directories.

## Selecting and Shuffling Files

```python
png_files = [f for f in os.listdir(subfolder_path) if f.endswith('.png')]
random.shuffle(png_files)
```

This part creates a list of all PNG files in the current subfolder and then shuffles the list randomly.

## Splitting the Files

```python
split_idx = int(len(png_files) * train_split)
train_files = png_files[:split_idx]
val_files = png_files[split_idx:]
```

The list of files is split into training and validation sets based on the `train_split` ratio.

## Copying Files

```python
for file in train_files:
    src = os.path.join(subfolder_path, file)
    dest = os.path.join(train_subfolder, file)
    shutil.copy(src, dest)

for file in val_files:
    src = os.path.join(subfolder_path, file)
    dest = os.path.join(val_subfolder, file)
    shutil.copy(src, dest)
```

These loops copy the files from the original location to their respective train or validation folders.

## Reporting

```python
print(f"Processed folder '{subfolder}': {len(train_files)} training files, {len(val_files)} validation files.")
```

This line prints a summary of how many files were placed in the training and validation sets for each subfolder.

## Script Execution

```python
input_folder = r'C:\' # Replace with your input folder path
output_folder = r'C:\' # Replace with your output folder path
split_data(input_folder, output_folder)
```

These lines set up the input and output folder paths and call the `split_data` function to execute the splitting process.

## Summary

This script automates the process of splitting a dataset into training and validation sets, maintaining the original folder structure. It's particularly useful for image classification tasks where data is organized into subfolders by class. The script ensures a random split of data, which is important for creating representative training and validation sets.

<div align="center">
  <a href="https://maazsalman.org/">
    <img width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" alt="gh" />
  </a>
  <p> Explore More! 🚀</p>
</div>
