#FactorioModDevZipTest
---------------------------------------------------------------------------------------------------
Version: 1.0.1
Date: 08 Aug 2023
  Features:
    - condition check if info.json exists
  Fixes:
    - cantpunishme, https://discord.com/channels/139677590393716737/496003658866098187/1138641837301694526
    - cross platform
---------------------------------------------------------------------------------------------------
Version: 1.0.0
Date: 08 Aug 2023
  Features:
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

Credits:
  - mr_arson, https://discord.com/channels/139677590393716737/496003658866098187/1138633527399809094
  - git add ., staging area
---------------------------------------------------------------------------------------------------
