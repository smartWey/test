import shutil
import os
import sys

def delete_folder(folder_path):
    """
    Deletes a folder and all its contents.
    
    Args:
        folder_path (str): The path to the folder to delete.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory.")
        return

    try:
        shutil.rmtree(folder_path)
        print(f"Successfully deleted folder: {folder_path}")
    except Exception as e:
        print(f"Failed to delete folder '{folder_path}'. Reason: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python delete_folder.py <folder_path>")
    else:
        target_folder = sys.argv[1]
        delete_folder(target_folder)
