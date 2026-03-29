import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS_DIR = os.path.join(BASE_DIR, 'etl')
MARTS_DIR = os.path.join(BASE_DIR, 'marts')
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')  

print("1. Генерация данных...")
generate_script = os.path.join(DATA_DIR, 'generate_data.py')
subprocess.run(['python', generate_script], check=True)

print("2. Запуск ETL...")
etl_scripts = ['etl_users.py', 'etl_products.py', 'etl_events.py']
for script in etl_scripts:
    script_path = os.path.join(SCRIPTS_DIR, script)
    print(f"Запуск {script}...")
    subprocess.run(['python', script_path], check=True)

print("3. Построение витрин ...")
mart_scripts = ['user_facts.py', 'event_facts.py', 'purchase_facts.py', 'cohort_facts.py']
for script in mart_scripts:
    script_path = os.path.join(MARTS_DIR, script)
    print(f"Запуск {script}...")
    subprocess.run(['python', script_path], check=True)

print("✅ Полный пайплайн завершён, все файлы созданы в data/processed/")