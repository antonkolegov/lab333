from converter import LengthConverter, TemperatureConverter, WeightConverter


def print_menu():
    """Выводит главное меню на экран."""
    print("\n" + "="*40)
    print("     КОНВЕРТЕР ФИЗИЧЕСКИХ ВЕЛИЧИН")
    print("="*40)
    print("1. Конвертировать длину")
    print("2. Конвертировать температуру")
    print("3. Конвертировать массу")
    print("4. Настройки")
    print("5. Выход")
    print("-"*40)


def get_user_choice() -> int:
    """
    Запрашивает у пользователя выбор пункта меню.

    :return: Выбранный номер пункта.
    """
    while True:
        try:
            choice = int(input("Выберите пункт меню (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print(" Некорректный выбор. Введите число от 1 до 5.")
        except ValueError:
            print(" Пожалуйста, введите целое число.")


def get_conversion_input(unit_type: str) -> tuple:
    """
    Запрашивает у пользователя данные для конвертации.

    :param unit_type: Тип величины ('length', 'temperature', 'weight').
    :return: Кортеж (значение, исходная единица, целевая единица).
    """
    while True:
        try:
            value = float(input("Введите значение: "))
            break
        except ValueError:
            print(" Некорректное значение. Введите число.")

    from_unit = input("Введите исходную единицу: ").strip()
    to_unit = input("Введите целевую единицу: ").strip()

    return value, from_unit, to_unit


def handle_length_conversion():
    """Обрабатывает конвертацию длины."""
    print("\n--- Конвертация длины ---")
    value, from_unit, to_unit = get_conversion_input('length')
    try:
        result = LengthConverter.convert(value, from_unit, to_unit)
        print(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")
    except ValueError as e:
        print(f" Ошибка: {e}")


def handle_temperature_conversion():
    """Обрабатывает конвертацию температуры."""
    print("\n--- Конвертация температуры ---")
    value, from_unit, to_unit = get_conversion_input('temperature')
    try:
        result = TemperatureConverter.convert(value, from_unit, to_unit)
        print(f" {value}°{from_unit} = {result:.6f}°{to_unit}")
    except ValueError as e:
        print(f" Ошибка: {e}")


def handle_weight_conversion():
    """Обрабатывает конвертацию массы."""
    print("\n--- Конвертация массы ---")
    value, from_unit, to_unit = get_conversion_input('weight')
    try:
        result = WeightConverter.convert(value, from_unit, to_unit)
        print(f" {value} {from_unit} = {result:.6f} {to_unit}")
    except ValueError as e:
        print(f" Ошибка: {e}")


def handle_settings():
    """Обрабатывает настройки."""
    print("\n--- Настройки ---")
    print("На данный момент доступны следующие настройки:")
    print("1. Изменить размер окна консоли (не реализовано)")
    print("2. Вернуться в меню")
    input("Нажмите Enter для возврата в меню...")
    print(" Настройки размера окна пока не реализованы в консольной версии.")


def run_ui():
    """Запускает цикл пользовательского интерфейса."""
    print("🚀 Запуск конвертера...")

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_length_conversion()
        elif choice == 2:
            handle_temperature_conversion()
        elif choice == 3:
            handle_weight_conversion()
        elif choice == 4:
            handle_settings()
        elif choice == 5:
            print("\n👋 Спасибо за использование конвертера! До свидания!")
            break

        # Пауза перед возвратом в меню
        input("\nНажмите Enter, чтобы продолжить...")