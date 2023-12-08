import os
import shutil

def organize_files(source_folder, destination_folder):
    # if destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Checking  if it's a file extension
        if os.path.isfile(source_path):
            file_extension = filename.split('.')[-1].lower()

            # destination path
            destination_path = os.path.join(destination_folder, file_extension)

            # creating new path/folder if not
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Moving the file to the corresponding folder
            shutil.move(source_path, os.path.join(destination_path, filename))

if __name__ == "__main__":
    source_directory = "C:/Users/shris/OneDrive/Desktop/py/"
    destination_directory = "C:/Users/shris/OneDrive/Desktop/py/new/"

    organize_files(source_directory, destination_directory)