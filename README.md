# goit-cs-hw-04

Homework 4. Tier 2. Computer Systems and Their Fundamentals at GoIT Neoversity

# Keyword Search Program

This program searches for specified keywords in multiple text files using two parallel processing approaches: **multithreading** and **multiprocessing**. It allows you to compare the performance of these two techniques and provides a detailed breakdown of where each keyword is found.

## Features

- **Multithreading**: Searches for keywords across files using multiple threads.
- **Multiprocessing**: Distributes the search tasks across multiple processes.
- **Performance Measurement**: Tracks execution time for both approaches.
- **Customizable**: Supports dynamic configuration of keywords and the number of threads/processes.

---

## Prerequisites

1. **Python Installation**: Ensure Python 3.6+ is installed on your system.
2. **Create the `text_files` directory**: The program requires a directory named `text_files` containing `.txt` files for testing.

---

## Setup and Usage

### Step 1: Generate Test Files

Use the provided `generate_files.sh` script to generate test files. This script creates `.txt` files in the `text_files` directory with random content, including keywords for testing.

1. Make the script executable:
   ```bash
   chmod +x generate_files.sh
   ```

2.	Run the script:
   ```bash
   ./generate_files.sh
   ```

### Step 2: Run the Program

1.	Open the main.py file and configure:
- Keywords: Update the KEYWORDS list with your desired keywords.
- Text Files Directory: Ensure FILES_DIR points to the correct directory (./text_files by default).

2.	Run the program:
   ```bash
   python main.py
   ```

3.	Observe the output:
- The program will display the execution time and results for both multithreading and multiprocessing approaches.
- Example output:
    ```
    Threading search:
    Execution time threading_search: 1.23 seconds
    {'keyword1': ['file_1.txt', 'file_2.txt'], 'keyword2': ['file_3.txt'], 'keyword3': []}

    Multiprocessing search:
    Execution time multiprocessing_search: 0.98 seconds
    {'keyword1': ['file_1.txt', 'file_2.txt'], 'keyword2': ['file_3.txt'], 'keyword3': []}
    ```
  
### Code Overview

- generate_files.sh: A Bash script that creates random .txt files containing sample data.
- main.py: The main program file that:
	-	Uses multithreading (threading_search) and multiprocessing (multiprocessing_search) to search for keywords.
	-	Measures and displays the execution time for each approach.
	-	Outputs the results as a dictionary where:
	     -	Keys are keywords.
	     -	Values are lists of files containing the corresponding keyword.

### Customization
1.	Modify Keywords: Edit the KEYWORDS list in main.py to add or remove search terms.
2. Adjust Threads/Processes: set num_threads or num_processes arguments inside the main.py to control the level of parallelism.

### Notes
- Ensure the text_files directory exists and contains .txt files before running the program.
- You can run the generate_files.sh script multiple times to prepare different datasets for testing.
