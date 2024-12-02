from threading import Thread
from multiprocessing import Process, Queue


def search_keywords_in_file(file_path, keywords):
    results = {keyword: [] for keyword in keywords}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            for keyword in keywords:
                if keyword.lower() in content:
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return results


def threading_search(files, keywords, num_threads=4):
    def worker_func(file_subset, results_data):
        local_results = {keyword: [] for keyword in keywords}
        for file in file_subset:
            result_dict = search_keywords_in_file(file, keywords)
            for keyword in keywords:
                local_results[keyword].extend(result_dict[keyword])
        results_data.append(local_results)

    threads = []
    results = []
    num_threads = min(num_threads, len(files))
    chunk_size = len(files) // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = Thread(target=worker_func, args=(files[start:end], results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_results = {keyword: [] for keyword in keywords}
    for result in results:
        for keyword in keywords:
            final_results[keyword].extend(result[keyword])
    return final_results

def worker(file_subset, keywords_data, queue_w):
    results = {keyword: [] for keyword in keywords_data}
    for file in file_subset:
        result_data = search_keywords_in_file(file, keywords_data)
        for keyword in keywords_data:
            results[keyword].extend(result_data[keyword])
    queue_w.put(results)


def multiprocessing_search(files, keywords, num_processes=4):
    processes = []
    queue = Queue()
    num_processes = min(num_processes, len(files))
    chunk_size = len(files) // num_processes

    for i in range(num_processes):
        start = i * chunk_size
        end = None if i == num_processes - 1 else (i + 1) * chunk_size
        process = Process(target=worker, args=(files[start:end], keywords, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    final_results = {keyword: [] for keyword in keywords}
    while not queue.empty():
        result = queue.get()
        for keyword in keywords:
            final_results[keyword].extend(result[keyword])
    return final_results
