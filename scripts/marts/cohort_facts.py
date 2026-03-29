import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

users_file = os.path.join(PROCESSED_DIR, 'users_clean.csv')
events_file = os.path.join(PROCESSED_DIR, 'events_clean.csv')
cohort_facts_file = os.path.join(PROCESSED_DIR, 'cohort_facts.csv')

users = pd.read_csv(users_file)
events = pd.read_csv(events_file)

users['registration_date'] = pd.to_datetime(users['registration_date'])
events['event_time'] = pd.to_datetime(events['event_time'])

users['cohort_month'] = users['registration_date'].dt.to_period('M')

events = events.merge(users[['user_id', 'cohort_month']], on='user_id', how='left')
events['event_month'] = events['event_time'].dt.to_period('M')

cohort_counts = events.groupby(['cohort_month', 'event_month']).agg(
    users_count=('user_id', 'nunique')
).reset_index()

if os.path.exists(cohort_facts_file):
    os.remove(cohort_facts_file)

cohort_counts.to_csv(cohort_facts_file, index=False)
print(f"cohort_facts.csv создан в {PROCESSED_DIR}")