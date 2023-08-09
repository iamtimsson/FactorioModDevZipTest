import os
import shutil
import json
import zipfile

def copy_files_with_filter(source_dir, destination_dir, exclude_dirs, exclude_extensions):
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]  # Exclude specified directories
        for file in files:
            if not any(file.endswith(ext) for ext in exclude_extensions):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, os.path.relpath(source_path, source_dir))
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy2(source_path, destination_path)

def zip_directory(directory_path, mod_dist, destination_dir_name):
    with zipfile.ZipFile(mod_dist, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory_path)
                archive_path = os.path.join(destination_dir_name, relative_path)  # Include destination_dir_name in the path
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

# Construct destination directory name
destination_dir = f"{name}_{version}"
mod_dist = f"{destination_dir}.zip"

# Specify the directories to exclude and the extensions to exclude
exclude_directories = ['.vs', destination_dir]
exclude_extensions = ['.ps1', '.py', '.sln']

# Create a new directory with the name of destination_dir and copy the files into it
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

    # Check if the main directory or zip file already exists in Factorio mods folder
factorio_mods_folder = os.path.expanduser("~/.factorio/mods")  # Linux and macOS
if os.name == 'nt':  # Windows
    factorio_mods_folder = os.path.expandvars("%APPDATA%/Factorio/mods")

factorio_mods_path = os.path.join(factorio_mods_folder, mod_dist)

# Check if the main directory or zip file already exists
if os.path.exists(factorio_mods_path) or os.path.exists(destination_dir) or os.path.exists(mod_dist):
    user_input = input("The main directory, zip file, or mod zip already exists. Do you want to proceed? (y/n): ").lower()
    if user_input != 'y':
        print("Operation cancelled.")
        exit()

copy_files_with_filter(
    source_dir=os.path.dirname(os.path.abspath(__file__)),
    destination_dir=destination_dir,
    exclude_dirs=exclude_directories,
    exclude_extensions=exclude_extensions
)

# Zip the contents of the created directory
zip_directory(destination_dir, mod_dist, destination_dir)

# Move the new zip file to the Factorio mods folder
factorio_mods_folder = os.path.expanduser("~/.factorio/mods")  # Linux and macOS
if os.name == 'nt':  # Windows
    factorio_mods_folder = os.path.expandvars("%APPDATA%/Factorio/mods")

factorio_mods_path = os.path.join(factorio_mods_folder, mod_dist)

shutil.move(mod_dist, factorio_mods_path)

# Delete the created directory
shutil.rmtree(destination_dir)

print(f"Zip file moved to Factorio mods folder: {factorio_mods_path}")
print("Files copied, zipped, moved, and directory deleted successfully.")
