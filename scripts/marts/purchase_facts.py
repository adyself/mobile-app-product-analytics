import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

events_file = os.path.join(PROCESSED_DIR, 'events_clean.csv')
products_file = os.path.join(PROCESSED_DIR, 'products_clean.csv')
purchase_facts_file = os.path.join(PROCESSED_DIR, 'purchase_facts.csv')

events = pd.read_csv(events_file)
products = pd.read_csv(products_file)

purchases = events[events['event_type'] == 'purchase']

purchases = purchases.merge(products, how='left', left_on='product_id', right_on='product_id')

purchase_summary = purchases.groupby('user_id').agg(
    total_revenue=('price', 'sum'),
    orders_count=('event_id', 'count'),
    avg_order_value=('price', 'mean')
).reset_index()

if os.path.exists(purchase_facts_file):
    os.remove(purchase_facts_file)

purchase_summary.to_csv(purchase_facts_file, index=False)
print(f"purchase_facts.csv создан в {PROCESSED_DIR}")