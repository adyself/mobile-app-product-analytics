import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

products_file = os.path.join(RAW_DIR, 'products.csv')
products_clean_file = os.path.join(PROCESSED_DIR, 'products_clean.csv')

products = pd.read_csv(products_file)

products = products.drop_duplicates(subset=['product_id'])

products['price'] = pd.to_numeric(products['price'], errors='coerce')
products = products[products['price'] >= 0]

products['category'] = products['category'].str.strip().str.title()
products['brand'] = products['brand'].str.strip().str.title()

products.to_csv(products_clean_file, index=False)
print(f"products_clean.csv создан в {PROCESSED_DIR}")