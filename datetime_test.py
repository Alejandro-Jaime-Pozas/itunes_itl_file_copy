import os
import shutil
import datetime

def copy_file():
    file_to_copy = "iTunes Library.itl.itl"  # Replace with the actual file name
    # source_path = os.path.join(source_dir, file_to_copy)
    
    # Generate a new file name based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_file_name = f"{timestamp}_{file_to_copy}"
    
    # destination_path = os.path.join(destination_dir, new_file_name)
    
    # shutil.copy2(source_path, destination_path)
    print(f'File copied as a new file: {new_file_name}')

def delete_oldest_file():
    files = os.listdir(destination_dir)
    if len(files) > 5:
        oldest_file = min(files, key=lambda f: os.path.getctime(os.path.join(destination_dir, f)))
        oldest_file_path = os.path.join(destination_dir, oldest_file)
        os.remove(oldest_file_path)
        print(f'Oldest file deleted: {oldest_file}')

copy_file()