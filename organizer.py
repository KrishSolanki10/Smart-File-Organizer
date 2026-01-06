import os
import shutil

BASE_DIR = "test_folder"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

def organize_files():
    for file in os.listdir(BASE_DIR):
        file_path = os.path.join(BASE_DIR, file)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    target_dir = os.path.join(BASE_DIR, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, target_dir)
                    moved = True
                    break

            if not moved:
                other_dir = os.path.join(BASE_DIR, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, other_dir)

    print("Files organized successfully.")

if __name__ == "__main__":
    organize_files()
