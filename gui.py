import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from converter import LengthConverter, TemperatureConverter, WeightConverter


class UnitConverterApp:
    """Основное окно приложения конвертера."""

    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер физических величин")
        self.root.geometry("600x400")  # Начальный размер окна
        self.root.minsize(500, 300)    # Минимальный размер

        # Переменные для хранения значений
        self.from_unit_var = tk.StringVar()
        self.to_unit_var = tk.StringVar()
        self.value_var = tk.StringVar(value="0.0")
        self.result_var = tk.StringVar(value="")

        # Словарь для выбора типа конвертации
        self.converter_types = {
            "Длина": LengthConverter,
            "Температура": TemperatureConverter,
            "Масса": WeightConverter
        }

        self.current_converter = LengthConverter  # По умолчанию

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        """Создаёт меню приложения."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Выход", command=self.root.quit)

        # Меню "Настройки"
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Настройки", menu=settings_menu)
        settings_menu.add_command(label="Установить размер окна", command=self.set_window_size)

    def create_widgets(self):
        """Создаёт виджеты GUI."""
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Выбор типа конвертации
        ttk.Label(frame, text="Тип конвертации:").grid(row=0, column=0, sticky=tk.W, pady=5)
        type_combo = ttk.Combobox(frame, values=list(self.converter_types.keys()), state="readonly")
        type_combo.current(0)
        type_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        type_combo.bind("<<ComboboxSelected>>", self.on_type_change)

        # Поле ввода значения
        ttk.Label(frame, text="Значение:").grid(row=1, column=0, sticky=tk.W, pady=5)
        value_entry = ttk.Entry(frame, textvariable=self.value_var)
        value_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # Выбор исходной единицы
        ttk.Label(frame, text="Из единицы:").grid(row=2, column=0, sticky=tk.W, pady=5)
        from_unit_combo = ttk.Combobox(frame, textvariable=self.from_unit_var, state="readonly")
        from_unit_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # Выбор целевой единицы
        ttk.Label(frame, text="В единицу:").grid(row=3, column=0, sticky=tk.W, pady=5)
        to_unit_combo = ttk.Combobox(frame, textvariable=self.to_unit_var, state="readonly")
        to_unit_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

        # Кнопка конвертации
        convert_button = ttk.Button(frame, text="Конвертировать", command=self.convert)
        convert_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Результат
        ttk.Label(frame, text="Результат:").grid(row=5, column=0, sticky=tk.W, pady=5)
        result_label = ttk.Label(frame, textvariable=self.result_var, foreground="blue", font=("Arial", 10, "bold"))
        result_label.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5)

        # Настройка веса сетки для растягивания
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Заполняем единицы для начального типа
        self.update_units()

    def on_type_change(self, event):
        """Обновляет список единиц при смене типа конвертации."""
        selected_type = event.widget.get()
        self.current_converter = self.converter_types[selected_type]
        self.update_units()

    def update_units(self):
        """Обновляет списки единиц в зависимости от выбранного типа."""
        if self.current_converter == LengthConverter:
            units = list(LengthConverter.UNITS.keys())
        elif self.current_converter == TemperatureConverter:
            units = ['C', 'F', 'K']
        elif self.current_converter == WeightConverter:
            units = list(WeightConverter.UNITS.keys())

        # Обновляем комбобоксы
        from_combo = self.root.nametowidget(".!frame.!combobox2")
        to_combo = self.root.nametowidget(".!frame.!combobox3")
        from_combo['values'] = units
        to_combo['values'] = units
        if units:
            from_combo.set(units[0])
            to_combo.set(units[0])

    def convert(self):
        """Выполняет конвертацию и выводит результат."""
        try:
            value = float(self.value_var.get())
            from_unit = self.from_unit_var.get().strip()
            to_unit = self.to_unit_var.get().strip()

            if not from_unit or not to_unit:
                raise ValueError("Выберите единицы измерения.")

            # Выполняем конвертацию
            if self.current_converter == TemperatureConverter:
                result = self.current_converter.convert(value, from_unit, to_unit)
            else:
                result = self.current_converter.convert(value, from_unit, to_unit)

            self.result_var.set(f"{result:.6f} {to_unit}")

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Неизвестная ошибка", f"Произошла ошибка: {e}")

    def set_window_size(self):
        """Открывает диалог для установки размера окна."""
        size_window = tk.Toplevel(self.root)
        size_window.title("Настройка размера окна")
        size_window.geometry("300x150")
        size_window.transient(self.root)  # Окно поверх основного
        size_window.grab_set()             # Блокируем основное окно

        ttk.Label(size_window, text="Ширина:").grid(row=0, column=0, padx=10, pady=5)
        width_var = tk.StringVar(value=str(self.root.winfo_width()))
        width_entry = ttk.Entry(size_window, textvariable=width_var)
        width_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(size_window, text="Высота:").grid(row=1, column=0, padx=10, pady=5)
        height_var = tk.StringVar(value=str(self.root.winfo_height()))
        height_entry = ttk.Entry(size_window, textvariable=height_var)
        height_entry.grid(row=1, column=1, padx=10, pady=5)

        def apply_size():
            try:
                w = int(width_var.get())
                h = int(height_var.get())
                if w < 400 or h < 300:
                    raise ValueError("Размер слишком мал.")
                self.root.geometry(f"{w}x{h}")
                size_window.destroy()
            except ValueError as e:
                messagebox.showerror("Ошибка", str(e))

        ttk.Button(size_window, text="Применить", command=apply_size).grid(row=2, column=0, columnspan=2, pady=10)


def run_gui():
    """Запускает GUI-приложение."""
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()