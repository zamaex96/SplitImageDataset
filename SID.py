import os
import shutil
import random

# Example usage:
input_folder = r'C:\'  # Replace with your input folder path
output_folder = r'C:\'  # Replace with your output folder path


def split_data(input_folder, output_folder, train_split=0.7):
    # Create training and validation folders
    train_folder = os.path.join(output_folder, 'train')
    val_folder = os.path.join(output_folder, 'test')
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    # Iterate through each subfolder in the input folder
    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)

        if os.path.isdir(subfolder_path):
            # Create corresponding subfolders in train and val folders
            train_subfolder = os.path.join(train_folder, subfolder)
            val_subfolder = os.path.join(val_folder, subfolder)
            os.makedirs(train_subfolder, exist_ok=True)
            os.makedirs(val_subfolder, exist_ok=True)

            # Get list of PNG files in the subfolder
            png_files = [f for f in os.listdir(subfolder_path) if f.endswith('.png')]

            # Shuffle the files randomly
            random.shuffle(png_files)

            # Split the files by 70% for training and 30% for validation
            split_idx = int(len(png_files) * train_split)
            train_files = png_files[:split_idx]
            val_files = png_files[split_idx:]

            # Copy files to respective directories
            for file in train_files:
                src = os.path.join(subfolder_path, file)
                dest = os.path.join(train_subfolder, file)
                shutil.copy(src, dest)

            for file in val_files:
                src = os.path.join(subfolder_path, file)
                dest = os.path.join(val_subfolder, file)
                shutil.copy(src, dest)

            print(
                f"Processed folder '{subfolder}': {len(train_files)} training files, {len(val_files)} validation files.")




split_data(input_folder, output_folder)
