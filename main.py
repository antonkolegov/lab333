import sys
import os

from interface import run_ui

def main():
    """
    Главная функция приложения.
    """
    print("Добро пожаловать в Конвертер Физических Величин!")
    try:
        run_ui()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем. До свидания!")
        sys.exit(0)
    except Exception as e:
        print(f"\n ошибка: {e}")
        print("Программа будет закрыта.")
        sys.exit(1)


if __name__ == "__main__":
    main()