import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

events_file = os.path.join(PROCESSED_DIR, 'events_clean.csv')
event_facts_file = os.path.join(PROCESSED_DIR, 'event_facts.csv')

# Загрузка данных
events = pd.read_csv(events_file)

# Приводим дату события к дате без времени
events['event_date'] = pd.to_datetime(events['event_time']).dt.date

# Считаем количество событий на пользователя в день
event_counts = events.groupby(['user_id', 'event_date', 'event_type']).size().reset_index(name='event_count')

# Безопасная запись
if os.path.exists(event_facts_file):
    os.remove(event_facts_file)

event_counts.to_csv(event_facts_file, index=False)
print(f"event_facts.csv создан в {PROCESSED_DIR}")