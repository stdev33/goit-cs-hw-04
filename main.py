import os
import time
from search_keywords.search_keywords import threading_search, multiprocessing_search


KEYWORDS = ["keyword1", "keyword2", "keyword3"]
FILES_DIR = "./text_files"
FILES = [os.path.join(FILES_DIR, file) for file in os.listdir(FILES_DIR) if file.endswith(".txt")]

def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    results = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time {func.__name__}: {end_time - start_time:.2f} seconds")
    return results

def main():
    if not FILES:
        print(f"No text files found in directory: {FILES_DIR}")
        print("Please add .txt files to the directory or generate test files using:")
        print("  ./generate_files.sh 10")
        return

    print("Threading search:")
    threading_results = measure_execution_time(threading_search, FILES, KEYWORDS, num_threads=2)
    print(threading_results)

    print("\nMultiprocessing search:")
    multiprocessing_results = measure_execution_time(multiprocessing_search, FILES, KEYWORDS, num_processes=2)
    print(multiprocessing_results)

if __name__ == "__main__":
    main()