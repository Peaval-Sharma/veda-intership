import os
import shutil

# Folder ka path input lena
folder_path = input("Enter folder path: ")

# File categories
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Python": [".py"],
    "Excel": [".xls", ".xlsx"],
    "Others": []
}

# Folder ke andar files check karna
for file_name in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file_name)

    # Sirf files ko process karna
    if os.path.isfile(file_path):

        # File extension lena
        extension = os.path.splitext(file_name)[1].lower()

        category = "Others"

        # Extension ke according category find karna
        for folder, extensions in folders.items():
            if extension in extensions:
                category = folder
                break

        # Destination folder banana
        destination_folder = os.path.join(folder_path, category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # File move karna
        destination = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination)

        print(file_name, "->", category)

print("\nFile organization completed!")