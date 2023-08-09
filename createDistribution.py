import os
import shutil
import json
import zipfile

def copy_files_with_filter(source_dir, destination_dir, exclude_dir, exclude_extensions):
    for root, dirs, files in os.walk(source_dir):
        if exclude_dir in dirs:
            dirs.remove(exclude_dir)
        
        for file in files:
            if not any(file.endswith(ext) for ext in exclude_extensions):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, os.path.relpath(source_path, source_dir))
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy2(source_path, destination_path)

def zip_directory(directory_path, mod_dist):
    with zipfile.ZipFile(mod_dist, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, relative_path)

# Read the JSON file
with open("info.json", "r") as json_file:
    json_content = json.load(json_file)
    name = json_content["name"]
    version = json_content["version"]

# Construct destination directory name
destination_dir = f"{name}_{version}"
mod_dist = f"{destination_dir}.zip"

# Specify the directory to exclude and the extensions to exclude
exclude_directory = '.vs'
exclude_extensions = ['.ps1', '.py', '.sln']

# Check if the main directory or zip file already exists
if os.path.exists(destination_dir) or os.path.exists(mod_dist):
    user_input = input("The main directory or zip file already exists. Do you want to proceed? (y/n): ").lower()
    if user_input != 'y':
        print("Operation cancelled.")
        exit()
    else:
        # Delete existing main directory and zip file
        if os.path.exists(destination_dir):
            shutil.rmtree(destination_dir)
        if os.path.exists(mod_dist):
            os.remove(mod_dist)

# Call the function to copy files
copy_files_with_filter(
    source_dir=os.path.dirname(os.path.abspath(__file__)),
    destination_dir=destination_dir,
    exclude_dir=exclude_directory,
    exclude_extensions=exclude_extensions
)

# Zip the created directory
zip_directory(destination_dir, mod_dist)

# Specify the path to the Factorio mods folder
factorio_mods_folder = os.path.expanduser("~/.factorio/mods")  # Linux and macOS
if os.name == 'nt':  # Windows
    factorio_mods_folder = os.path.expandvars("%APPDATA%/Factorio/mods")

factorio_mods_path = os.path.join(factorio_mods_folder, mod_dist)

# Move the new zip file to the Factorio mods folder
shutil.move(mod_dist, factorio_mods_path)

# Delete the created directory
shutil.rmtree(destination_dir)

print(f"Zip file moved to Factorio mods folder: {factorio_mods_path}")
print("Files copied, zipped, moved, and directory deleted successfully. Enjoy or die. Or enjoy dying, I don't know. I wanted this to sound much more playful.")
