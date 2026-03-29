import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

users_file = os.path.join(RAW_DIR, 'users.csv')
users_clean_file = os.path.join(PROCESSED_DIR, 'users_clean.csv')

users = pd.read_csv(users_file)

users = users.drop_duplicates(subset=['user_id'])

users['registration_date'] = pd.to_datetime(users['registration_date'], errors='coerce')

users['country'] = users['country'].str.strip().str.title()

users['device_type'] = users['device_type'].str.strip().str.capitalize()
users.loc[~users['device_type'].isin(['Ios', 'Android']), 'device_type'] = 'Unknown'

users.to_csv(users_clean_file, index=False)
print(f"users_clean.csv создан в {PROCESSED_DIR}")