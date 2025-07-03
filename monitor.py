import psutil

def get_system_metrics():

    metrics = {
        # Загрузка ЦП в процентах
        'cpu_percent': psutil.cpu_percent(interval=1),
        # Использование оперативной памяти в процентах
        'ram_percent': psutil.virtual_memory().percent,
        # Использование файла подкачки (swap) в процентах
        'swap_percent': psutil.swap_memory().percent,
        # Количество активных процессов
        'num_processes': len(psutil.pids())
    }
    return metrics

if __name__ == '__main__':
    # Этот блок нужен для быстрой проверки работы модуля
    # При запуске файла напрямую он выведет текущие метрики
    import time
    while True:
        print(get_system_metrics())
        time.sleep(1)
