import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
ANALYTICS_DIR = os.path.join(PROCESSED_DIR, "analytics")

events_file = os.path.join(PROCESSED_DIR, "events_clean.csv")
ab_file = os.path.join(ANALYTICS_DIR, "ab_test_results.csv")

# загружаем события
events = pd.read_csv(events_file)

# считаем уникальных пользователей в каждой группе
results = events.groupby("experiment_group")["user_id"].nunique().reset_index()

# переименуем колонку
results.columns = ["experiment_group", "active_users"]

# сохраняем
results.to_csv(ab_file, index=False)

print("ab_test_results.csv создан")