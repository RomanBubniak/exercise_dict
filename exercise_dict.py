import psutil
import time
while True:
    ram = psutil.virtual_memory()._asdict()
    total_gb = ram["total"] / (1024 ** 3)
    used_gb = ram["used"] / (1024 ** 3)
    available_gb = ram["available"] / (1024 ** 3)
    percent_of_usage = ram["percent"]
    print(f"количевство оперативки {total_gb:.1f} использовано {used_gb:.1f} доступно {available_gb:.1f} процент использования {percent_of_usage}%")
    time.sleep(1)