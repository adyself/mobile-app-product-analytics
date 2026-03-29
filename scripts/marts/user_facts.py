import os
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

users_file = os.path.join(PROCESSED_DIR, 'users_clean.csv')
user_facts_file = os.path.join(PROCESSED_DIR, 'user_facts.csv')

users = pd.read_csv(users_file)

users['days_since_registration'] = (pd.to_datetime('2026-03-01') - pd.to_datetime(users['registration_date'])).dt.days

users['user_segment'] = users['device_type'] + "_" + users['country']

if os.path.exists(user_facts_file):
    os.remove(user_facts_file)

users.to_csv(user_facts_file, index=False)
print(f"user_facts.csv создан в {PROCESSED_DIR}")