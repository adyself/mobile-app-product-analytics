import os
import pandas as pd

# путь к корню проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# папки
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
ANALYTICS_DIR = os.path.join(PROCESSED_DIR, "analytics")

os.makedirs(ANALYTICS_DIR, exist_ok=True)

# файлы источников
event_facts_file = os.path.join(PROCESSED_DIR, "event_facts.csv")
purchase_facts_file = os.path.join(PROCESSED_DIR, "purchase_facts.csv")
cohort_facts_file = os.path.join(PROCESSED_DIR, "cohort_facts.csv")

# файлы результатов
dau_mau_file = os.path.join(ANALYTICS_DIR, "dau_mau.csv")
arpu_ltv_file = os.path.join(ANALYTICS_DIR, "arpu_ltv.csv")

# загрузка данных
events = pd.read_csv(event_facts_file)
purchases = pd.read_csv(purchase_facts_file)
cohorts = pd.read_csv(cohort_facts_file)

# преобразуем дату
events["event_date"] = pd.to_datetime(events["event_date"])

# создаем месяц
events["event_month"] = events["event_date"].dt.to_period("M").dt.to_timestamp()

# DAU

dau = (
    events
    .groupby("event_date")["user_id"]
    .nunique()
    .reset_index()
)

dau["metric"] = "DAU"
dau.columns = ["date", "value", "metric"]

# MAU

mau = (
    events
    .groupby("event_month")["user_id"]
    .nunique()
    .reset_index()
)

mau["metric"] = "MAU"
mau.columns = ["date", "value", "metric"]

# объединяем
dau_mau = pd.concat([dau, mau])

# сохраняем
dau_mau.to_csv(dau_mau_file, index=False)

# ARPU

total_revenue = purchases["total_revenue"].sum()
active_users = events["user_id"].nunique()

arpu = total_revenue / active_users

# LTV

paying_users = purchases["user_id"].nunique()

ltv = total_revenue / paying_users

arpu_ltv = pd.DataFrame({
    "metric": ["ARPU", "LTV"],
    "value": [arpu, ltv]
})

arpu_ltv.to_csv(arpu_ltv_file, index=False)

print("product_metrics: DAU, MAU, ARPU, LTV сохранены")