import os
import shutil
import json
import zipfile

def copy_files_with_filter(source_dir, dest_dir, excl_dirs, excl_exts):
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if d not in excl_dirs]  # Exclude specified directories
        for file in files:
            if not any(file.endswith(ext) for ext in excl_exts):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, os.path.relpath(source_path, source_dir))
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(source_path, dest_path)

def zip_dir(dir_path, mod_dist, dest_dir):
    with zipfile.ZipFile(mod_dist, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, dir_path)
                archive_path = os.path.join(dest_dir, relative_path)  # Include dest_dir in the path
                zipf.write(file_path, archive_path)  # Preserve original hierarchy


# Check if the current directory has a valid info.json file
if not os.path.exists("info.json"):
    print("The 'info.json' file is not present in the current directory.")
    exit()

# Read the JSON file
with open("info.json", "r") as json_file:
    json_content = json.load(json_file)
    name = json_content["name"]
    version = json_content["version"]

# Check if the main directory or zip file already exists in Factorio mods folder
factorio_mods_folder = os.path.expanduser("~/.factorio/mods")  # Linux and macOS
if os.name == 'nt':  # Windows
    factorio_mods_folder = os.path.expandvars("%APPDATA%/Factorio/mods")

# Construct destination directory name
dest_dir = f"{name}_{version}"
mod_dist = f"{dest_dir}.zip"
factorio_mods_path = os.path.join(factorio_mods_folder, mod_dist)

# Check if the main directory or zip file already exists
if os.path.exists(factorio_mods_path) or os.path.exists(dest_dir) or os.path.exists(mod_dist):
    user_input = input("The main directory, zip file, or mod zip already exists. Do you want to proceed? (y/n): ").lower()
    if user_input != 'y':
        print("Operation cancelled.")
        exit()

# Specify the directories to exclude and the extensions to exclude
excl_dirs = ['.vs', dest_dir]
excl_exts = ['.ps1', '.py', '.sln']

# Create a new directory with the name of dest_dir and copy the files into it
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

copy_files_with_filter(
    source_dir=os.path.dirname(os.path.abspath(__file__)),
    dest_dir=dest_dir,
    excl_dirs=excl_dirs,
    excl_exts=excl_exts
)

# Zip the contents of the created directory
zip_dir(dest_dir, mod_dist, dest_dir)

# Create the complete path to the mod distribution file within the Factorio mods folder
factorio_mods_path = os.path.join(factorio_mods_folder, mod_dist)

# Move the new zip file to the Factorio mods folder
shutil.move(mod_dist, factorio_mods_path)

# Delete the created directory
shutil.rmtree(dest_dir)

print(f"Zip file moved to Factorio mods folder: {factorio_mods_path}")
print("Files copied, zipped, moved, and directory deleted successfully.")
