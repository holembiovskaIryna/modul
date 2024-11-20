import csv
import matplotlib.pyplot as plt

file_name = "books.csv"


#Завантаження даних
def read_file(file_name):
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            books = [row for row in reader]
            return books
    except FileNotFoundError:
        print("Файл не знайдено!")
        return []


#Збереження даних у файл
def save_file(file_name, books):
    with open(file_name, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["Назва книги", "Автор", "Рік видання", "Жанр", "Кількість примірників"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


#Додавання нової книги
def add_book(books):
    name = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    year = input("Введіть рік видання: ")
    genre = input("Введіть жанр книги: ")
    quantity = input("Введіть кількість примірників: ")
    books.append(
        {"Назва книги": name, "Автор": author, "Рік видання": year, "Жанр": genre, "Кількість примірників": quantity})
    print("Книгу додано успішно.")


# Редагування інформації про книгу
def edit_book(books):
    name = input("Введіть назву книги, яку потрібно змінити: ")
    for book in books:
        if book["Назва книги"] == name:
            book["Автор"] = input(f"Новий автор (зараз: {book['Автор']}): ") or book["Автор"]
            book["Рік видання"] = input(f"Новий рік видання (зараз: {book['Рік видання']}): ") or book["Рік видання"]
            book["Жанр"] = input(f"Новий жанр (зараз: {book['Жанр']}): ") or book["Жанр"]
            book["Кількість примірників"] = input(f"Нова кількість (зараз: {book['Кількість примірників']}): ") or book["Кількість примірників"]
            print("Інформацію оновлено.")
            return
    print("Книгу не знайдено.")

# Видалення книги за назвою
def delete_book(books):
    name = input("Введіть назву книги, яку потрібно видалити: ")
    for book in books:
        if book["Назва книги"] == name:
            books.remove(book)
            print("Книгу видалено.")
            return
    print("Книгу не знайдено.")

# Виведення списку книг у вигляді таблиці
def display_books(books):
    print(f"{'Назва книги':<20} {'Автор':<20} {'Рік видання':<10} {'Жанр':<15} {'Кількість':<10}")
    print("-" * 75)
    for book in books:
        print(f"{book['Назва книги']:<20} {book['Автор']:<20} {book['Рік видання']:<10} {book['Жанр']:<15} {book['Кількість примірників']:<10}")


# Виведення популярних жанрів
def popular_genres(books):
    genre_counts = {}
    for book in books:
        genre = book["Жанр"]
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

    print("Найпопулярніші жанри:")
    for genre, count in genre_counts.items():
        print(f"{genre}: {count} книг")

#Підрахунок загальної кількості книг
def count_total_books(books):
    total = sum(int(book["Кількість примірників"]) for book in books)
    print(f"Загальна кількість книг у бібліотеці: {total}")

# Пошук книг певного автора
def find_books_by_author(books):
    author = input("Введіть ім'я автора для пошуку: ")
    found_books = [book for book in books if book["Автор"].lower() == author.lower()]
    if found_books:
        display_books(found_books)
    else:
        print("Книги цього автора не знайдено.")


#Побудова кругової діаграми
def genre_pie_chart(books):
    genre_counts = {}
    for book in books:
        genre = book["Жанр"]
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

    plt.pie(genre_counts.values(), labels=genre_counts.keys(), autopct="%1.1f%%")
    plt.title("Розподіл книг за жанрами")
    plt.show()


#Побудова гістограми за роками
def year_histogram(books):
    year_counts = {}
    for book in books:
        year = book["Рік видання"]
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1

    plt.bar(year_counts.keys(), year_counts.values())
    plt.title("Кількість книг за роками видання")
    plt.xlabel("Рік видання")
    plt.ylabel("Кількість")
    plt.show()

