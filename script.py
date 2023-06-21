import shutil, time, psutil, os

source_dir = "C:\\Users\\Propietario\\OneDrive\\Music\\iTunes"
destination_dir = "C:\\Users\\Propietario\\OneDrive\\Music\\iTunes library backup"


def copy_file():
    file_to_copy = "iTunes Library.itl.itl" 
    source_path = os.path.join(source_dir, file_to_copy)
    destination_path = os.path.join(destination_dir, file_to_copy)
    shutil.copy2(source_path, destination_path)
    print(f'File copied: {file_to_copy}')

def delete_oldest_file():
    files = os.listdir(destination_dir)
    if len(files) > 5:
        oldest_file = min(files, key=lambda f: os.path.getctime(os.path.join(destination_dir, f)))
        oldest_file_path = os.path.join(destination_dir, oldest_file)
        os.remove(oldest_file_path)
        print(f'Oldest file deleted: {oldest_file}')


already_copied = False 

while True:
    itunes_running = False
    for process in psutil.process_iter(['name']):
        # print(process.info['name'])
        if process.info['name'] == 'iTunes.exe':  # check if process named iTunes.exe
            print('itunes is still running')
            itunes_running, already_copied = True, False 
            break

    if not itunes_running:
        print('itunes is no longer running')
        if not already_copied:
            copy_file()
            already_copied = True
        # THIS DIDN'T WORK:
        # timestamp = os.path.getmtime("C:\\Users\\Propietario\\OneDrive\\Music\\iTunes\\iTunes Library.itl.itl")
        # now = time.time()
        # time_difference = (now - timestamp) / 60
        # print(time_difference)
        # if time_difference > 10:
        #     copy_file()
        # break
    time.sleep(5)  # Wait for _ seconds before checking again