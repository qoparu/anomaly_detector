import time
import multiprocessing

def high_cpu_load_task():
    """Задача, которая бесконечно нагружает одно ядро ЦП."""
    while True:
        _ = 12345 * 54321  # Простое бессмысленное вычисление

def run_cpu_anomaly(duration_seconds):
    """
    Запускает аномальную нагрузку на ЦП на заданное время.
    Создает по одному процессу на каждое ядро ЦП.
    """
    print(f"[ANOMALY] Запускаю аномальную нагрузку на ЦП на {duration_seconds} секунд...")
    
    num_cores = multiprocessing.cpu_count()
    processes = []
    
    for i in range(num_cores):
        process = multiprocessing.Process(target=high_cpu_load_task)
        process.start()
        processes.append(process)
        
    time.sleep(duration_seconds)
    
    for process in processes:
        process.terminate()
        process.join()
        
    print("[ANOMALY] Аномальная нагрузка завершена.")

if __name__ == '__main__':
    # Быстрая проверка: запускает аномалию на 15 секунд
    run_cpu_anomaly(15)
