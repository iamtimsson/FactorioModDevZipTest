# FactorioModDevZipTest
1. **Function Definitions:**
   - `copy_files_with_filter(source_dir, destination_dir, exclude_dir, exclude_extensions)`: Recursively copies files while excluding specific directories and file extensions.
   - `zip_directory(directory_path, mod_dist)`: Creates a zip file containing the contents of a specified directory.

2. **Reading JSON Information:**
   - Reads mod information (name and version) from "info.json".

3. **Creating Destination Directory and Zipping:**
   - Constructs a destination directory using the mod name and version.
   - Checks if the destination directory or zip file exists, prompting user input.
   - If confirmed, deletes existing directory and zip file.
   - Uses `copy_files_with_filter` to copy selected files to the destination.
   - Calls `zip_directory` to create a zip file from the destination.

4. **Moving Zip File to Factorio Mods Folder:**
   - Constructs the Factorio mods folder path using environment variables.
   - Moves the new zip file to the Factorio mods folder.

5. **Cleaning Up:**
   - Deletes the created destination directory after moving the zip.

6. **Final Output:**
   - Prints the path where the zip was moved and a success message.

This script automates file copying, zip creation, and deployment for Factorio modders, improving efficiency and reducing manual tasks. It ensures a smoother development and deployment process by handling checks and cleanup steps.
