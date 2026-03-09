from app.io.input import input_console, read_file, read_file_pandas
from app.io.output import output_to_console, write_file


def main():
    # Шляхи до файлів
    input_file_path = "data/input.txt"
    input_pandas_path = "data/input.csv"
    output_file_path = "data/output.txt"

    # 1. Зчитування даних
    console_text = input_console()
    file_text = read_file(input_file_path)
    pandas_data = read_file_pandas(input_pandas_path)

    # 2. Вивід у консоль
    output_to_console("--- Результат з консолі ---")
    output_to_console(console_text)

    output_to_console("--- Результат з файлу (вбудовані функції) ---")
    output_to_console(file_text)

    output_to_console("--- Результат з файлу (pandas) ---")
    output_to_console(pandas_data)

    # 3. Запис у файл (через вбудовані можливості)
    content_to_write = f"Текст з консолі:\n{console_text}\n\nТекст з файлу:\n{file_text}\n\nДані з pandas:\n{pandas_data}"
    write_file(output_file_path, content_to_write)


# Цей блок гарантує, що функція main() дійсно запуститься
if __name__ == "__main__":
    main()