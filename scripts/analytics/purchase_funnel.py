import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
ANALYTICS_DIR = os.path.join(PROCESSED_DIR, "analytics")

events_file = os.path.join(PROCESSED_DIR, "events_clean.csv")
funnel_file = os.path.join(ANALYTICS_DIR, "funnel.csv")

events = pd.read_csv(events_file)

funnel_steps = ["app_open", "view_product", "add_to_cart", "purchase"]

funnel = []

for step in funnel_steps:
    users_count = events[events["event_type"] == step]["user_id"].nunique()

    funnel.append({
        "step": step,
        "users_count": users_count
    })

funnel_df = pd.DataFrame(funnel)

funnel_df.to_csv(funnel_file, index=False)

print("funnel.csv создан")