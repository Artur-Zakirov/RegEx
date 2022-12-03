import re
import csv


def csv_read(csv_name):
    with open(csv_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def data_edit(contacts_list):
    pattern = r"(8|\+7)?[-\s]*?\(?(\d{3})\)?[-\s]*(\d+)[-\s]*(\d{2})[-\s]*(\d{2})\s?(\(?(доб[а-я]*?)(.)?(\s)?(\d+)\)?)?"
    for row in contacts_list:
        for item in row:
            item_id = row.index(item)
            result = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8\10", item).strip()
            row[item_id] = result

    for row in contacts_list:
        for i in range(3):
            if len(row[i].split()) == 3:
                row[i], row[i + 1], row[i + 2] = row[i].split()
            elif len(row[i].split()) == 2:
                row[i], row[i + 1] = row[i].split()

    contacts_dict = {}
    for row in contacts_list:
        if row[0] in contacts_dict:
            new_info = {row[i]: i for i in range(len(row))}
            contacts_dict[row[0]] = {**contacts_dict[row[0]], **new_info}
            copy_info = contacts_dict[row[0]].copy()
            for key, value in copy_info.items():
                if value in contacts_dict[row[0]].values() and not key:
                    del contacts_dict[row[0]][key]
            contacts_dict[row[0]] = dict(sorted(contacts_dict[row[0]].items(),
                                                key=lambda x: x[1]))
        else:
            contacts_dict[row[0]] = {row[i]: i for i in range(len(row))}
    new_contacts_list = [list(contact_value) for contact_value in contacts_dict.values()]
    return new_contacts_list


def csv_write(csv_name, list):
    with open(csv_name, "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(list)


if __name__ == '__main__':
    csv_file = "phonebook_raw.csv"
    new_csv_file = "phonebook.csv"
    contacts_list = csv_read(csv_file)
    new_contacts_list = data_edit(contacts_list)
    csv_write(new_csv_file, new_contacts_list)
