import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
ANALYTICS_DIR = os.path.join(PROCESSED_DIR, 'analytics')
os.makedirs(ANALYTICS_DIR, exist_ok=True)

user_facts_file = os.path.join(PROCESSED_DIR, 'user_facts.csv')
purchase_facts_file = os.path.join(PROCESSED_DIR, 'purchase_facts.csv')
event_facts_file = os.path.join(PROCESSED_DIR, 'event_facts.csv')

segments_file = os.path.join(ANALYTICS_DIR, 'user_segments.csv')

users = pd.read_csv(user_facts_file)
purchases = pd.read_csv(purchase_facts_file)
events = pd.read_csv(event_facts_file)

# Активность пользователя
active_users = events['user_id'].unique()
users['is_active'] = users['user_id'].apply(lambda x: 1 if x in active_users else 0)

# Количество покупок
orders_count = purchases.groupby('user_id')['orders_count'].sum().reset_index()
users = users.merge(orders_count, on='user_id', how='left')
users['orders_count'] = users['orders_count'].fillna(0)

# Сегментация по устройству и стране (из user_facts)
users['segment'] = users['device_type'] + "_" + users['country']

# Безопасная запись
if os.path.exists(segments_file):
    os.remove(segments_file)
users.to_csv(segments_file, index=False)
print("user_segments.csv сохранен")