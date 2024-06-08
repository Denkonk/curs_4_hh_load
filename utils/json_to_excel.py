import json
import pandas as pd
import os

def json_to_excel(json_file_path, excel_file_path):
    """
    Функция для загрузки данных из JSON файла и сохранения их в Excel файл.
    """
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    formatted_data = []
    for entry in data:
        formatted_entry = {
            'title': entry.get('title'),
            'city': entry.get('city'),
            'salary_from': entry.get('salary_from'),
            'salary_to': entry.get('salary_to'),
            'requirement': entry.get('requirement'),
            'responsibility': entry.get('responsibility'),
            'schedule': entry.get('schedule'),
            'url': entry.get('url'),
            'created_at': entry.get('created_at')
        }
        formatted_data.append(formatted_entry)

    df = pd.DataFrame(formatted_data)
    df.to_excel(excel_file_path, index=False)

# Пример использования:
current_dir = os.path.dirname(__file__)
json_file_path = os.path.join(current_dir, '..', 'data', 'vacancies.json')
excel_file_path = os.path.join(current_dir, '..', 'data', 'vacancies.xlsx')

json_to_excel(json_file_path, excel_file_path)

print(f"Данные успешно сохранены в {excel_file_path}")
