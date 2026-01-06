import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

def get_folder_path():
    path = input("Enter folder path to organize: ").strip()
    if not os.path.exists(path):
        print("❌ Folder does not exist.")
        return None
    return path

def ask_preview_mode():
    choice = input("Run in preview mode? (y/n): ").lower()
    return choice == "y"

def organize_files(base_dir, preview=False):
    summary = {}
    total_files = 0

    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)

        # Skip folders & hidden files
        if not os.path.isfile(item_path) or item.startswith("."):
            continue

        total_files += 1
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if item.lower().endswith(tuple(extensions)):
                target_dir = os.path.join(base_dir, folder)
                os.makedirs(target_dir, exist_ok=True)

                if preview:
                    print(f"[PREVIEW] {item} → {folder}/")
                else:
                    shutil.move(item_path, target_dir)

                summary[folder] = summary.get(folder, 0) + 1
                moved = True
                break

        if not moved:
            other_dir = os.path.join(base_dir, "Others")
            os.makedirs(other_dir, exist_ok=True)

            if preview:
                print(f"[PREVIEW] {item} → Others/")
            else:
                shutil.move(item_path, other_dir)

            summary["Others"] = summary.get("Others", 0) + 1

    return total_files, summary

def show_summary(total, summary):
    print("\n📊 Summary Report")
    print(f"Total files scanned: {total}")
    for folder, count in summary.items():
        print(f"{folder}: {count} files")

def main():
    base_dir = get_folder_path()
    if not base_dir:
        return

    preview = ask_preview_mode()
    confirm = input("Proceed with organizing? (y/n): ").lower()

    if confirm != "y":
        print("Operation cancelled.")
        return

    total, summary = organize_files(base_dir, preview)
    show_summary(total, summary)

    print("\n✅ Done.")

if __name__ == "__main__":
    main()
