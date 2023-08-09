#FactorioModDevZipTest
---------------------------------------------------------------------------------------------------

Version: 1.0.4
Date: 09 Aug 2023
  Fixes:
    - rearranged logic
    - rereadmed

Version: 1.0.3
Date: 09 Aug 2023
  Fixes:
    - refactor variable names ( i like them less now.. :/ )
    - yeah well it works for certain now even more

Version: 1.0.2
Date: 09 Aug 2023
  Fixes:
    - yeah well it works for certain now

Version: 1.0.1
Date: 08 Aug 2023
  Features:
    - condition check if info.json exists
  Fixes:
    - cantpunishme, https://discord.com/channels/139677590393716737/496003658866098187/1138641837301694526
    - cross platform

Version: 1.0.0
Date: 08 Aug 2023
  Features:
1. **Function Definitions:**
   - `copy_files_with_filter`: Copies files from a source directory to a destination directory while excluding specified directories and file extensions.
   - `zip_dir`: Creates a zip archive of the contents of a directory.

2. **Check for "info.json":**
   - The script checks if the "info.json" file exists in the current directory.
   - If not, it prints an error message and exits.

3. **Read "info.json" Content:**
   - The script reads the content of the "info.json" file.
   - It extracts the mod's name and version.

4. **Factorio Mods Folder Path:**
   - Determines the path to the Factorio mods folder based on the operating system.
   - Constructs the destination directory name using the extracted mod name and version.
   - Creates the name for the mod distribution zip file.

5. **Check for Existing Mods:**
   - Checks if the main directory, zip file, or mod zip already exists in the Factorio mods folder.
   - Asks for user confirmation to proceed if any of these exist.
   - If the user cancels, the script prints a cancellation message and exits.

6. **Exclude Directories and Extensions:**
   - Specifies directories to exclude (`excl_dirs`) and file extensions to exclude (`excl_exts`).

7. **Create Destination Directory:**
   - Creates a new directory with the constructed destination directory name.
   
8. **Copy Files to Destination:**
   - Copies files from the script's directory to the destination directory.
   - Excludes specified directories and file extensions using `copy_files_with_filter` function.

9. **Zip Contents of Destination:**
   - Zips the contents of the created destination directory using `zip_dir` function.

10. **Construct Full Mod Path:**
    - Creates the complete path to the mod distribution file within the Factorio mods folder.

11. **Move Zip File to Mods Folder:**
    - Moves the newly created zip file to the Factorio mods folder.

12. **Cleanup:**
    - Deletes the created destination directory after moving the zip file.

13. **Print Success Messages:**
    - Prints the path where the zip file was moved.
    - Indicates successful completion of the operations.

14. **End of Script:**
    - Script execution concludes.

This script automates file copying, zip creation, and deployment for Factorio modders, improving efficiency and reducing manual tasks. It ensures a smoother development and deployment process by handling checks and cleanup steps.

Credits:
  - mr_arson, https://discord.com/channels/139677590393716737/496003658866098187/1138633527399809094
  - git add ., staging area
---------------------------------------------------------------------------------------------------
