import pandas as pd
import os

# путь к корню проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# папки данных
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

# файлы
events_file = os.path.join(RAW_DIR, "events.csv")
events_clean_file = os.path.join(PROCESSED_DIR, "events_clean.csv")

# загрузка данных
events = pd.read_csv(events_file)

# преобразуем дату
events["event_time"] = pd.to_datetime(events["event_time"])

# убираем пробелы и приводим события к одному формату
events["event_type"] = events["event_type"].str.strip().str.lower()

# удаляем дубликаты
events = events.drop_duplicates()

# проверяем количество событий
print("Количество событий по типу:")
print(events["event_type"].value_counts())

# сохраняем очищенные данные
events.to_csv(events_clean_file, index=False)

print(f"Файл сохранён: {events_clean_file}")