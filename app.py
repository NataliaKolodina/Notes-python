import csv
import datetime


def create_note(title, body, notes):
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y')
    new_note = [len(notes) + 1, title, body, timestamp]
    notes.append(new_note)
    write_to_csv(notes)
    return "Заметка создана!"


def edit_note(note_id, title, body, notes):
    if 0 < note_id <= len(notes):
        timestamp = datetime.datetime.now().strftime('%d-%m-%Y')
        notes[note_id - 1] = [note_id, title, body, timestamp]
        write_to_csv(notes)
        return "Заметка изменена!"
    return "Такой заметки не существует!"


def delete_note(note_id, notes):
    if 0 < note_id <= len(notes):
        del notes[note_id - 1]
        for i in range(note_id - 1, len(notes)):
            notes[i][0] -= 1
        write_to_csv(notes)
        return "Заметка удалена!"
    return "Такой заметки не существует!"


def list_notes(notes, filter_date=None):
    if filter_date:
        filtered_notes = [note for note in notes if filter_date in note[3]]
        return filtered_notes
    return notes


def write_to_csv(notes):
    with open('notes.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(notes)


def read_from_csv():
    try:
        with open('notes.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            return list(reader)
    except FileNotFoundError:
        return []


def main():
    notes = read_from_csv()
    print("1. Создать заметку\n2. Изменить заметку\n3. Удалить заметку\n4. Печать заметок\n")

    option = input("Выберите действие: ")

    if option == "1":
        title = input("Введите заголовок: ")
        body = input("Введите заметку: ")
        print(create_note(title, body, notes))


    elif option == "2":
        note_id = int(input("Введите ID для изменения: "))
        title = input("введите новый заголовок: ")
        body = input("Введите новую заметку: ")
        print(edit_note(note_id, title, body, notes))

    elif option == "3":
        note_id = int(input("Введите ID для удаления: "))
        print(delete_note(note_id, notes))

    elif option == "4":
        filter_date = input("Введите ID заметки или нажмите Enter для отбора всех заметок: ")
        filtered_notes = list_notes(notes, filter_date)
        for note in filtered_notes:
            print(note)
    else:
        print('Неверный выбор')


if __name__ == "__main__":
    main()