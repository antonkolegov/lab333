class LengthConverter:
    """Конвертер для единиц длины."""
    # Коэффициенты перевода в метры
    UNITS = {
        'м': 1.0,
        'км': 1000.0,
        'см': 0.01,
        'мм': 0.001,
        'дюйм': 0.0254,
        'фут': 0.3048,
        'миля': 1609.34
    }

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        """Конвертирует значение из одной единицы в другую."""
        if from_unit not in LengthConverter.UNITS:
            raise ValueError(f"Единица '{from_unit}' не поддерживается для длины.")
        if to_unit not in LengthConverter.UNITS:
            raise ValueError(f"Единица '{to_unit}' не поддерживается для длины.")

        # Переводим в метры, затем в нужную единицу
        meters = value * LengthConverter.UNITS[from_unit]
        return meters / LengthConverter.UNITS[to_unit]


class TemperatureConverter:
    """Конвертер для единиц температуры."""
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Переводит градусы Цельсия в Фаренгейты."""
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Переводит градусы Фаренгейта в Цельсия."""
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Переводит градусы Цельсия в Кельвины."""
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Переводит Кельвины в градусы Цельсия."""
        return kelvin - 273.15

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        """Конвертирует температуру из одной единицы в другую."""
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()

        if from_unit == to_unit:
            return value

        # C -> F
        if from_unit == 'C' and to_unit == 'F':
            return TemperatureConverter.celsius_to_fahrenheit(value)
        # F -> C
        elif from_unit == 'F' and to_unit == 'C':
            return TemperatureConverter.fahrenheit_to_celsius(value)
        # C -> K
        elif from_unit == 'C' and to_unit == 'K':
            return TemperatureConverter.celsius_to_kelvin(value)
        # K -> C
        elif from_unit == 'K' and to_unit == 'C':
            return TemperatureConverter.kelvin_to_celsius(value)
        # F -> K (через C)
        elif from_unit == 'F' and to_unit == 'K':
            c = TemperatureConverter.fahrenheit_to_celsius(value)
            return TemperatureConverter.celsius_to_kelvin(c)
        # K -> F (через C)
        elif from_unit == 'K' and to_unit == 'F':
            c = TemperatureConverter.kelvin_to_celsius(value)
            return TemperatureConverter.celsius_to_fahrenheit(c)
        else:
            raise ValueError(f"Невозможно конвертировать из {from_unit} в {to_unit}.")


class WeightConverter:
    """Конвертер для единиц массы."""
    UNITS = {
        'кг': 1.0,
        'г': 0.001,
        'мг': 0.000001,
        'т': 1000.0,
        'унция': 0.0283495,
        'фунт': 0.453592
    }

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        """
        Конвертирует значение из одной единицы в другую."""
        if from_unit not in WeightConverter.UNITS:
            raise ValueError(f"Единица '{from_unit}' не поддерживается для массы.")
        if to_unit not in WeightConverter.UNITS:
            raise ValueError(f"Единица '{to_unit}' не поддерживается для массы.")

        # Переводим в килограммы, затем в нужную единицу
        kg = value * WeightConverter.UNITS[from_unit]
        return kg / WeightConverter.UNITS[to_unit]