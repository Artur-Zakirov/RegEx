import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
for row in contacts_list:
    print(row)
print()

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
pattern = r"(8|\+7)?[-\s]*?\(?(\d{3})\)?[-\s]*(\d+)[-\s]*(\d{2})[-\s]*(\d{2})\s?(\(?(доб[а-я]*?)(.)?(\s)?(\d+)\)?)?"
for row in contacts_list:
    for item in row:
        item_id = row.index(item)
        result = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8\10", item).strip()
        row[item_id] = result

for row in contacts_list:
    print(row)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


