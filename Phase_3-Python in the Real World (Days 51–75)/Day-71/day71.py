# Day 71 — Thread-Safe Design & Avoiding Shared State

import threading
import queue


def worker(task_queue: queue.Queue, results: list):
    """
    Worker thread:
    - Receives tasks via queue
    - Produces results without touching shared counters
    """
    while True:
        try:
            value = task_queue.get_nowait()
        except queue.Empty:
            break

        result = value * value
        results.append(result)
        task_queue.task_done()


def main():
    task_queue = queue.Queue()
    results = []

    # Populate tasks
    for i in range(10):
        task_queue.put(i)

    threads = []
    for _ in range(3):
        t = threading.Thread(target=worker, args=(task_queue, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Results:", sorted(results))


if __name__ == "__main__":
    main()

print("\nDay 71 completed successfully!")
