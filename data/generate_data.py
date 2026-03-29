import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')

n_users = 5000

users = pd.DataFrame({
    "user_id": range(1, n_users + 1),
    "registration_date": pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 365, n_users), unit="d"),
    "country": np.random.choice(["Russia", "Kazakhstan", "Belarus"], n_users),
    "device_type": np.random.choice(["iOS", "Android"], n_users)
})

users_file = os.path.join(RAW_DIR, "users.csv")
users.to_csv(users_file, index=False)
print(f"users.csv создан в {RAW_DIR}")

n_products = 200

products = pd.DataFrame({
    "product_id": range(1, n_products + 1),
    "category": np.random.choice(["Shoes", "T-shirts", "Jeans", "Jackets"], n_products),
    "price": np.random.randint(1000, 10000, n_products),
    "brand": np.random.choice(["Nike", "Adidas", "Puma", "Zara"], n_products)
})

products_file = os.path.join(RAW_DIR, "products.csv")
products.to_csv(products_file, index=False)
print(f"products.csv создан в {RAW_DIR}")

n_events = 50000

event_types = ["app_open", "view_product", "add_to_cart", "purchase"]

events = pd.DataFrame({
    "event_id": range(1, n_events + 1),
    "user_id": np.random.randint(1, n_users + 1, n_events),
    "event_type": np.random.choice(event_types, n_events, p=[0.4, 0.3, 0.2, 0.1]),
    "product_id": np.random.randint(1, n_products + 1, n_events),
    "event_time": pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 365, n_events), unit="d"),
    "session_id": np.random.randint(1, 20000, n_events),
    "experiment_group" : np.random.choice(['A', 'B'], size=n_events, p=[0.5, 0.5])
})

events_file = os.path.join(RAW_DIR, "events.csv")
events.to_csv(events_file, index=False)
print(f"events.csv создан в {RAW_DIR}")