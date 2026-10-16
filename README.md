# Python Automated File Organizer

## Overview

The Python Automated File Organizer is a command-line utility designed to automate file management by detecting newly added files in a specified directory and organizing them into categorized folders based on their file extensions.

Developed using Python's built-in modules, the program reduces the need for manual file sorting by continuously monitoring a directory, identifying new files, determining their categories, and moving them to the appropriate destinations. It also creates destination folders dynamically when they do not exist and incorporates retry logic to handle temporary file-access errors.

This project demonstrates the practical application of Python fundamentals to solve a common file-management problem through automation.

## Features

- **Automatic file detection:** Monitors a specified directory and identifies newly added files.
- **Extension-based categorization:** Determines the appropriate category for each file using its extension.
- **Dynamic directory creation:** Creates destination folders automatically when required.
- **Automated file movement:** Moves detected files into their corresponding category folders.
- **Error handling:** Uses retry logic to handle certain temporary file-access issues, such as files being locked by another application.
- **Continuous monitoring:** Repeats the detection and organization process while the program is running.

## File Categories

The program organizes supported files into four categories:

| Category | Supported extensions |
|---|---|
| Videos | `.mp4`, `.mkv`, `.avi` |
| Music | `.mp3`, `.m4a` |
| Pictures | `.jpg`, `.png` |
| Files | `.txt`, `.pdf`, `.docx` |

Files with extensions outside these configured categories are not assigned to any of the four destination folders.

## How It Works

### 1. Directory Monitoring

The program records the filenames initially present in the target directory. During each monitoring cycle, it retrieves the current directory contents and compares them with the previous record to identify newly added files.

Python sets and set-difference operations make it possible to identify new entries without repeatedly processing the entire directory as if every file were new.

### 2. File Identification

For every detected file, the program extracts its extension and checks it against a collection of predefined file categories. This determines the destination folder for each supported file type.

### 3. Dynamic Folder Creation

Before moving a file, the program checks whether the appropriate destination directory exists. If it does not, the program creates the directory automatically. This eliminates the need to prepare every category folder manually.

### 4. File Movement

The `shutil` module is used to move supported files into their corresponding directories. This automates the repetitive process of sorting files manually.

### 5. Error Handling and Retry Logic

During development, attempts to move files that were still in use by another application produced file-access errors. To address this, the program incorporates retry logic that waits briefly before attempting the operation again, with a limited number of attempts.

### 6. State Management

After processing a monitoring cycle, the program updates its record of the directory contents. This is important for ensuring that files already detected are not repeatedly treated as new during subsequent cycles.

## Technologies Used

- **Python:** Core programming language.
- **`os`:** Directory inspection, path handling, and directory creation.
- **`shutil`:** File movement.
- **`time`:** Delays between monitoring cycles and retry attempts.
- **Git and GitHub:** Version control and project documentation.

## Concepts Demonstrated

This project provided practical experience with several foundational programming concepts:

- Variables, loops, and conditional statements.
- Dictionaries and sets.
- Set difference and change detection.
- File extensions and path manipulation.
- Directory creation and file-system operations.
- Exception handling with `try` and `except`.
- Retry logic and execution delays.
- Program state management.
- Debugging and incremental problem-solving.

## Requirements

- Python 3.
- A Windows environment or another environment compatible with the required file-system operations.
- Permission to access and modify the target directory.

The program uses Python's standard library and does not require third-party packages.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the example URL and directory name with your actual GitHub repository details.

### 2. Configure the Target Directory

Open the Python script and set the directory path to the folder you want the program to monitor.

For example, on Windows:

```python
path = r"C:\Users\YourName\Downloads\MUSIC"
```

Replace the example path with your desired directory.

### 3. Run the Program

```bash
python organizer.py
```

Replace `organizer.py` with the actual name of your Python script.

Once running, the program monitors the configured directory and organizes supported files as they are detected.

## Important Notes

- Back up important files before testing the program on a directory containing valuable data.
- Test with sample files first to confirm that each category works as expected.
- The program is designed around the configured file extensions and categories; unsupported extensions are not automatically organized.
- Keep the script outside the directory being monitored if you do not want the program to detect its own files.
- The program must remain running to continue monitoring the directory.

## Future Improvements

Possible extensions to the project include:

- Supporting additional file types and customizable categories.
- Adding logging to record successful moves and failed attempts.
- Introducing configuration options so users can select the target directory without editing the source code.
- Improving handling of duplicate filenames and incomplete file transfers.
- Adding a graceful shutdown mechanism.
- Creating a graphical user interface.
- Adding automated tests for file classification, folder creation, and error handling.

## Project Motivation

This project began with the goal of replacing repetitive manual file organization with a simple automated process. During development, I explored how appropriate data structures, directory inspection, and control-flow logic could reduce unnecessary work and improve program behavior.

Debugging issues such as repeated processing and file-access errors reinforced the importance of tracking program state, understanding file-system behavior, and designing reliable retry mechanisms.

The project represents a practical step in strengthening my Python fundamentals through building, testing, debugging, and improving a working utility.

## Author

Developed as a personal Python programming project focused on file-system automation, problem-solving, and strengthening foundational software development skills.
