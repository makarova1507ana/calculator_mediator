

# Класс Calculator, реализующий конкретное поведение
class Calculator():
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

    def calculate(self):
        if self.operand1 is None or self.operand2 is None or self.operator is None:
            raise ValueError("Operands and operator must be set")
        
        match self.operator.type:
            case "+":
                return self.operand1.value + self.operand2.value
            case "-":
                return self.operand1.value - self.operand2.value
            case "*":
                return self.operand1.value * self.operand2.value
            case "/":
                if self.operand2.value == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                return self.operand1.value / self.operand2.value
            case _:
                raise ValueError("Unknown operator type")


# Класс Operand, представляющий операнд (число)
class Operand:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Operand must be a number")
        self.value = value



# Класс Operator, представляющий операцию (сложение, вычитание, умножение, деление)
class Operator:
    VALID_OPERATORS = {"+", "-", "*", "/"}

    def __init__(self, type):
        if type not in self.VALID_OPERATORS:
            raise ValueError(f"Invalid operator type: {type}")
        self.type = type


# Пример использования:
mediator = Calculator()
while True:
    command = input("""
Выберите команду: 
1. калькулятор
2. выход
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
            mediator.set_operand(Operand(operand1), 1)
            mediator.set_operand(Operand(operand2), 2)

            # Установка операции
            mediator.set_operator(Operator(operator))

            # Выполнение операции и вывод результата
            result = mediator.calculate()
            print(f"Результат: {result}")

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
