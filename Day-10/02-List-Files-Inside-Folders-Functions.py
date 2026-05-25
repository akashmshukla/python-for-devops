import os

def list_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except PermissionError:
        return None, "Permission Denied"
    except FileNotFoundError:
        return None, "Folder Not Found"

def main():
    folders = input("Please enter the folder name separated by space: ").split()
    
    for folder in folders:
        files, error_message = list_files_in_folder(folder)
        if files:
            print(f"----- Files in folder {folder} -----")
            for file in files:
                print(file)
            print()
        else:
            print(f"----- Files in folder {folder} -----")
            print(f"Error : {error_message}")
            print()

if __name__ == "__main__":
    main()