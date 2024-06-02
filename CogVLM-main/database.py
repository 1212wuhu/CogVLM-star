import os
import shutil

def copy_files_with_prefix(source_folder, dest_folder, start_index=1):
    count = start_index
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.jpg') and file.startswith('0'):
                source_file_path = os.path.join(root, file)
                new_filename = f"{count:05}_{file}"
                dest_file_path = os.path.join(dest_folder, new_filename)
                shutil.copyfile(source_file_path, dest_file_path)
                print(f"Copied: {source_file_path} -> {dest_file_path}")
                count += 1

source_folder = "D:/毕业设计/数据源/武汉流行观测站/2019cam1/2019"
dest_folder = "D:/毕业设计/数据源/images"

copy_files_with_prefix(source_folder, dest_folder)
