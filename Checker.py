import os
import time

import requests

while True:
    all_names = []
    saved_names = []
    url = "https://api.telegram.org/bot5366780727:AAG9XggRzYFRURxpgGEES5GbF5GePi0FWi0/sendMessage?chat_id=1324130964&text="

    with open('Checker_data.data', 'r', encoding='utf-8') as file:
        saved_names.append([a for a in file.read().split('\n') if a != ''])

    for dirpath, dirnames, filenames in os.walk(r"C:\Users\User\Desktop\уник"):
        catalogue = {}
        files = []
        for dirname in dirnames:
            all_names.append('Catalogue: ' + os.path.join(dirpath, dirname))

        for filename in filenames:
            all_names.append("File: " + os.path.join(dirpath, filename))

    if saved_names[0] != all_names:
        editted_list = []
        for i in all_names:
            if i not in saved_names[0]:
                category = i.split(":")[0]
                path = i.split("\\")[4:]
                correct_path = ''
                for i in path:
                    correct_path += i
                    correct_path += '\\'
                editted_list.append(correct_path)
        text = f"⭕В директории произошли изменения. ⭕\n🔰 Изменённые пути: 🔰\n\n"

        for i in saved_names[0]:
            if i not in all_names:
                category = i.split(":")[0]
                path = i.split("\\")[4:]
                correct_path = ''
                for i in path:
                    correct_path += i
                    correct_path += '\\'
                editted_list.append(correct_path)

        for eddited in editted_list:
            text += f"{eddited}\n"

        first_response = url + text
        requests.get(first_response)

        second_response = url + "✏️Записываю в базу новые файлы... ✏"
        requests.get(second_response)
        with open('Checker_data.data', 'w', encoding='utf-8') as file:
            for dirpath, dirnames, filenames in os.walk(r"C:\Users\User\Desktop\уник"):
                for dirname in dirnames:
                    file.write('Catalogue: ' + os.path.join(dirpath, dirname) + '\n')

                for filename in filenames:
                    file.write("File: " + os.path.join(dirpath, filename) + '\n')

        third_response = url + "✅️Успешно! ✅"
        requests.get(third_response)
        time.sleep(3600)