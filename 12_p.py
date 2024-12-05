import os
import shutil
import subprocess
import platform

download_dir = 'path/to/your/download/directory'


file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt'],
    'videos': ['.mp4', '.mov', '.avi'],
    'music': ['.mp3', '.wav'],
    'archives': ['.zip', '.tar', '.gz', '.rar']
}


for dir_name in file_types.keys():
    os.makedirs(os.path.join(download_dir, dir_name), exist_ok=True)


for item in os.listdir(download_dir):
    item_path = os.path.join(download_dir, item)
    if os.path.isfile(item_path):
        file_extension = os.path.splitext(item)[1].lower()
        moved = False
        for dir_name, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(item_path, os.path.join(download_dir, dir_name, item))
                moved = True
                break
        if not moved:
            
            os.makedirs(os.path.join(download_dir, 'others'), exist_ok=True)
            shutil.move(item_path, os.path.join(download_dir, 'others', item))
            
    print("Files have been organized successfully!")        
def clear_temp_files():
    temp_dir = os.getenv('TEMP')
    if temp_dir:
        for file in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

def defragment_disk():
    if platform.system() == 'Windows':
        subprocess.run(['defrag', 'C:', '/X'])
    else:
        print("Defragmentation is not supported on this OS.")

def check_updates():
    if platform.system() == 'Windows':
        subprocess.run(['powershell', '-Command', 'Get-WindowsUpdate'])
    elif platform.system() == 'Linux':
        subprocess.run(['sudo', 'apt', 'update'])
    else:
        print("Update check is not supported on this OS.")

def main():
    clear_temp_files()
    defragment_disk()
    check_updates()
    print("System maintenance tasks completed.")

if __name__ == '__main__':
    main()
            

    
