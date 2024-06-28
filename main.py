from abc import ABC, abstractmethod


# Абстрактный класс для коллег (компонентов, которые взаимодействуют через медиатор)
class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def notify(self, message):
        pass


# Конкретная реализация операнда (числа)
class Operand(Colleague):
    def __init__(self, mediator, value):
        super().__init__(mediator)
        self.value = value

    def set_value(self, value):
        self.value = value
        self.mediator.operands_changed()

    def notify(self, message):
        pass  # Операнды не реагируют на сообщения от медиатора


# Конкретная реализация оператора (сложение, вычитание, умножение, деление)
class Operator(Colleague):
    def __init__(self, mediator, operator_type):
        super().__init__(mediator)
        self.type = operator_type

    def set_type(self, operator_type):
        self.type = operator_type
        self.mediator.operator_changed()

    def notify(self, message):
        if message == "operands_ready":
            self.execute_operation()

    def execute_operation(self):
        if self.type == "+":
            result = self.mediator.operand1.value + self.mediator.operand2.value
        elif self.type == "-":
            result = self.mediator.operand1.value - self.mediator.operand2.value
        elif self.type == "*":
            result = self.mediator.operand1.value * self.mediator.operand2.value
        elif self.type == "/":
            if self.mediator.operand2.value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = self.mediator.operand1.value / self.mediator.operand2.value
        else:
            raise ValueError("Unknown operator type")

        print(f"Результат: {result}")


# Медиатор, координирующий взаимодействие между операндами и операторами
class CalculatorMediator:
    def __init__(self):
        self.operand1 = None
        self.operand2 = None
        self.operator = None

    def set_operand(self, operand, position):
        if position == 1:
            self.operand1 = operand
        elif position == 2:
            self.operand2 = operand
        else:
            raise ValueError("Position must be 1 or 2")

    def set_operator(self, operator):
        self.operator = operator

    def operands_changed(self):
        if self.operand1 and self.operand2 and self.operator:
            self.operator.notify("operands_ready")

    def operator_changed(self):
        if self.operand1 and self.operand2 and self.operator:
            self.operator.notify("operands_ready")


# Интерфейс для пользовательского взаимодействия
if __name__ == "__main__":
    mediator = CalculatorMediator()

    while True:
        command = input("""
Выберите команду:
1. Калькулятор
2. Выход
""")
        if command == '1':
            try:
                operand1 = float(input("Введите первое число: "))
                operator = input("""Введите операцию:
+
-
*
/
""")
                operand2 = float(input("Введите второе число: "))

                # Установка операндов
                mediator.set_operand(Operand(mediator, operand1), 1)
                mediator.set_operand(Operand(mediator, operand2), 2)

                # Установка оператора
                mediator.set_operator(Operator(mediator, operator))

                # Выполнение операции и вывод результата
                mediator.operator.execute_operation()

            except ValueError as ve:
                print(f"Ошибка ввода: {ve}")
            except ZeroDivisionError as zde:
                print(f"Ошибка: {zde}")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")

        elif command == '2':
            break
        else:
            print("Неверная команда, попробуйте снова.")


