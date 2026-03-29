import subprocess
import os

ETL_DIR = os.path.dirname(os.path.abspath(__file__))
ETL_SCRIPTS = ['etl_users.py', 'etl_products.py', 'etl_events.py']

for script in ETL_SCRIPTS:
    script_path = os.path.join(ETL_DIR, script)
    print(f"Запуск {script}...")
    subprocess.run(['python', script_path], check=True)

print("ETL-пайплайн завершен, все файлы сохранены в data/processed/")