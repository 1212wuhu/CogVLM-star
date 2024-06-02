import os
from PIL import Image

def get_next_number(folder_path):
    max_number = 898
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.startswith("W1P_") and filename.endswith(".jpg"):
                try:
                    number = int(filename.split("_")[0])
                    if number > max_number:
                        max_number = number
                except ValueError:
                    pass
    return max_number + 1

def rename_files_in_folder(folder_path):
    next_number = get_next_number(folder_path)
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith("W1P.jpg"):
                old_filepath = os.path.join(root, filename)
                print(f"Current file: {old_filepath}")
                
                # Open the image using PIL
                try:
                    img = Image.open(old_filepath)
                    img.show()  # Show the image
                except Exception as e:
                    print(f"Error opening image: {e}")
                    continue
                
                # Ask user if they want to rename the file
                rename_file = input("Do you want to rename this file? (yes/no): ")
                if rename_file.lower() == "yes":
                    next_number_str = str(next_number).zfill(5)  # Zero padding
                    new_filename = f"{next_number_str}_{input('Enter new filename (including extension): ')}"
                    new_filepath = os.path.join(root, new_filename)
                    try:
                        os.rename(old_filepath, new_filepath)
                        print(f"Renamed file to: {new_filepath}")
                        next_number += 1
                    except Exception as e:
                        print(f"Error renaming file: {e}")
                else:
                    print("Skipping renaming.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    rename_files_in_folder(folder_path)
