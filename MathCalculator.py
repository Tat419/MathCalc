import math

def solve_quadratic():
    """Вычисление корней квадратного уравнения."""
    print("\n=== Квадратное уравнение ===")
    try:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
    except ValueError:
        print("Ошибка: нужно вводить числа!")
        return

    D = b**2 - 4*a*c
    if D < 0:
        print("Решений нет (дискриминант отрицательный)")
    elif D == 0:
        x = -b / (2*a)
        print(f"Единственное решение: x = {x:.4f}")
    else:
        sqrtD = math.sqrt(D)
        x1 = (-b + sqrtD) / (2*a)
        x2 = (-b - sqrtD) / (2*a)
        print(f"Два решения: x1 = {x1:.4f}, x2 = {x2:.4f}")


# ----------  Прогрессии (общий пункт) ----------

def arithmetic_progression():
    """Арифметическая прогрессия."""
    print("\n--- Арифметическая прогрессия ---")
    print("1 — найти a_n (n-й член)")
    print("2 — найти S_n (сумму первых n членов)")
    try:
        choice = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка: нужно ввести 1 или 2")
        return

    try:
        if choice == 1:
            n = int(input("Введите номер n: "))
            a1 = float(input("Введите первый член a1: "))
            d = float(input("Введите разность d: "))
            an = a1 + (n - 1) * d
            print(f"a_{n} = {an:.4f}")
        elif choice == 2:
            a1 = float(input("Введите первый член a1: "))
            d = float(input("Введите разность d: "))
            n = int(input("Введите количество членов n: "))
            Sn = (2*a1 + d*(n-1)) / 2 * n
            print(f"S_{n} = {Sn:.4f}")
        else:
            print("Извините, вы ввели не то число")
    except ValueError:
        print("Ошибка: все значения должны быть числами")


def geometric_progression():
    """Геометрическая прогрессия."""
    print("\n--- Геометрическая прогрессия ---")
    print("1 — найти b_n (n-й член)")
    print("2 — найти S_n (сумму первых n членов)")
    try:
        choice = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка: нужно ввести 1 или 2")
        return

    try:
        if choice == 1:
            n = int(input("Введите номер n: "))
            b1 = float(input("Введите первый член b1: "))
            q = float(input("Введите знаменатель q: "))
            bn = b1 * q**(n-1)
            print(f"b_{n} = {bn:.4f}")
        elif choice == 2:
            b1 = float(input("Введите первый член b1: "))
            q = float(input("Введите знаменатель q: "))
            n = int(input("Введите количество членов n: "))
            if q == 1:
                Sn = b1 * n
            else:
                Sn = b1 * (q**n - 1) / (q - 1)
            print(f"S_{n} = {Sn:.4f}")
        else:
            print("Извините, вы ввели не то число")
    except ValueError:
        print("Ошибка: все значения должны быть числами")


def progressions_hub():
    """Меню прогрессий."""
    while True:
        print("\n" + "-"*30)
        print("       ПРОГРЕССИИ")
        print("-"*30)
        print("1 — Арифметическая прогрессия")
        print("2 — Геометрическая прогрессия")
        print("0 — Назад в главное меню")
        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Ошибка: введите номер")
            continue
        if choice == 0:
            break
        elif choice == 1:
            arithmetic_progression()
        elif choice == 2:
            geometric_progression()
        else:
            print("Неверный номер. Попробуйте ещё раз.")


# ----------  Тригонометрия ----------

def trig():
    """Вычисление синуса, косинуса, тангенса, котангенса."""
    print("\n=== Тригонометрия ===")
    print("1 — синус")
    print("2 — косинус")
    print("3 — тангенс")
    print("4 — котангенс")
    try:
        choice = int(input("Что вычисляем? "))
        if choice not in (1, 2, 3, 4):
            print("Неверный номер")
            return
        angle = float(input("Угол в градусах: "))
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    rad = math.radians(angle)

    if choice == 1:
        result = math.sin(rad)
        print(f"sin({angle}°) = {result:.4f}")
    elif choice == 2:
        result = math.cos(rad)
        print(f"cos({angle}°) = {result:.4f}")
    elif choice == 3:
        if abs(math.cos(rad)) < 1e-12:
            print(f"tg({angle}°) не определён (косинус = 0)")
        else:
            result = math.tan(rad)
            print(f"tg({angle}°) = {result:.4f}")
    elif choice == 4:
        if abs(math.sin(rad)) < 1e-12:
            print(f"ctg({angle}°) не определён (синус = 0)")
        else:
            result = 1.0 / math.tan(rad)
            print(f"ctg({angle}°) = {result:.4f}")


# ----------  ДВУМЕРНЫЕ ПЛОЩАДИ ----------

def triangle_area():
    """Площадь треугольника разными способами."""
    print("\n--- Площадь треугольника ---")
    print("1 — по основанию и высоте")
    print("2 — по трём сторонам (Герон)")
    print("3 — прямоугольный (два катета)")
    print("4 — по двум сторонам и углу между ними")
    try:
        method = int(input("Выберите метод: "))
    except ValueError:
        print("Ошибка: нужно ввести 1–4")
        return

    try:
        if method == 1:
            a = float(input("Основание: "))
            h = float(input("Высота: "))
            S = 0.5 * a * h
        elif method == 2:
            a = float(input("Сторона a: "))
            b = float(input("Сторона b: "))
            c = float(input("Сторона c: "))
            if a + b <= c or a + c <= b or b + c <= a:
                print("Треугольник с такими сторонами не существует!")
                return
            p = (a + b + c) / 2
            S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        elif method == 3:
            a = float(input("Первый катет: "))
            b = float(input("Второй катет: "))
            S = 0.5 * a * b
        elif method == 4:
            a = float(input("Первая сторона: "))
            b = float(input("Вторая сторона: "))
            angle = float(input("Угол между ними в градусах: "))
            S = 0.5 * a * b * math.sin(math.radians(angle))
        else:
            print("Неверный номер метода")
            return
        print(f"Площадь треугольника = {S:.4f}")
    except ValueError:
        print("Ошибка: все значения должны быть числами")


def rectangle_area():
    """Площадь прямоугольника."""
    print("\n--- Площадь прямоугольника ---")
    try:
        a = float(input("Длина: "))
        b = float(input("Ширина: "))
        if a <= 0 or b <= 0:
            print("Длина и ширина должны быть положительными")
            return
        S = a * b
        print(f"Площадь прямоугольника = {S:.4f}")
    except ValueError:
        print("Ошибка: нужно ввести числа")


def square_area():
    """Площадь квадрата."""
    print("\n--- Площадь квадрата ---")
    try:
        a = float(input("Сторона квадрата: "))
        if a <= 0:
            print("Сторона должна быть положительной")
            return
        S = a * a
        print(f"Площадь квадрата = {S:.4f}")
    except ValueError:
        print("Ошибка: нужно ввести число")


def rhombus_area():
    """Площадь ромба."""
    print("\n--- Площадь ромба ---")
    print("1 — через диагонали")
    print("2 — через сторону и высоту")
    try:
        method = int(input("Выберите метод: "))
    except ValueError:
        print("Ошибка: нужно ввести 1 или 2")
        return

    try:
        if method == 1:
            d1 = float(input("Первая диагональ: "))
            d2 = float(input("Вторая диагональ: "))
            S = 0.5 * d1 * d2
        elif method == 2:
            a = float(input("Сторона: "))
            h = float(input("Высота: "))
            S = a * h
        else:
            print("Неверный номер метода")
            return
        print(f"Площадь ромба = {S:.4f}")
    except ValueError:
        print("Ошибка: все значения должны быть числами")


def parallelogram_area():
    """Площадь параллелограмма."""
    print("\n--- Площадь параллелограмма ---")
    try:
        a = float(input("Основание: "))
        h = float(input("Высота: "))
        if a <= 0 or h <= 0:
            print("Основание и высота должны быть положительными")
            return
        S = a * h
        print(f"Площадь параллелограмма = {S:.4f}")
    except ValueError:
        print("Ошибка: нужно ввести числа")


def trapezoid_area():
    """Площадь трапеции."""
    print("\n--- Площадь трапеции ---")
    try:
        a = float(input("Первое основание: "))
        b = float(input("Второе основание: "))
        h = float(input("Высота: "))
        if a <= 0 or b <= 0 or h <= 0:
            print("Все значения должны быть положительными")
            return
        S = (a + b) * h / 2
        print(f"Площадь трапеции = {S:.4f}")
    except ValueError:
        print("Ошибка: нужно ввести числа")


def circle_area():
    """Площадь круга."""
    print("\n--- Площадь круга ---")
    try:
        r = float(input("Радиус: "))
        if r <= 0:
            print("Радиус должен быть положительным")
            return
        S = math.pi * r * r
        print(f"Площадь круга = {S:.4f}")
    except ValueError:
        print("Ошибка: нужно ввести число")


def flat_areas():
    """Меню двумерных площадей."""
    while True:
        print("\n" + "-"*40)
        print("       ДВУМЕРНЫЕ ПЛОЩАДИ (2D)")
        print("-"*40)
        print("1  — Треугольник")
        print("2  — Прямоугольник")
        print("3  — Квадрат")
        print("4  — Ромб")
        print("5  — Параллелограмм")
        print("6  — Трапеция")
        print("7  — Круг")
        print("0  — Назад")

        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Ошибка: введите номер")
            continue

        if choice == 0:
            break
        elif choice == 1:
            triangle_area()
        elif choice == 2:
            rectangle_area()
        elif choice == 3:
            square_area()
        elif choice == 4:
            rhombus_area()
        elif choice == 5:
            parallelogram_area()
        elif choice == 6:
            trapezoid_area()
        elif choice == 7:
            circle_area()
        else:
            print("Неверный номер. Попробуйте ещё раз.")


# ----------  ТРЁХМЕРНЫЕ ТЕЛА ----------

def parallelepiped_calc():
    """Прямоугольный параллелепипед."""
    print("\n--- Прямоугольный параллелепипед ---")
    print("1 — Площадь полной поверхности")
    print("2 — Площадь боковой поверхности")
    print("3 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2,3):
            print("Неверный номер")
            return
        a = float(input("Длина: "))
        b = float(input("Ширина: "))
        c = float(input("Высота: "))
        if a <= 0 or b <= 0 or c <= 0:
            print("Все размеры должны быть положительными")
            return
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = 2*(a*b + a*c + b*c)
        print(f"Полная поверхность = {S:.4f}")
    elif act == 2:
        S = 2*c*(a + b)
        print(f"Боковая поверхность = {S:.4f}")
    elif act == 3:
        V = a * b * c
        print(f"Объём = {V:.4f}")


def cube_calc():
    """Куб."""
    print("\n--- Куб ---")
    print("1 — Площадь полной поверхности")
    print("2 — Площадь боковой поверхности")
    print("3 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2,3):
            print("Неверный номер")
            return
        a = float(input("Ребро куба: "))
        if a <= 0:
            print("Ребро должно быть положительным")
            return
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = 6 * a * a
        print(f"Полная поверхность = {S:.4f}")
    elif act == 2:
        S = 4 * a * a
        print(f"Боковая поверхность = {S:.4f}")
    elif act == 3:
        V = a**3
        print(f"Объём = {V:.4f}")


def cylinder_calc():
    """Цилиндр."""
    print("\n--- Цилиндр ---")
    print("1 — Площадь полной поверхности")
    print("2 — Площадь боковой поверхности")
    print("3 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2,3):
            print("Неверный номер")
            return
        r = float(input("Радиус основания: "))
        h = float(input("Высота: "))
        if r <= 0 or h <= 0:
            print("Радиус и высота должны быть положительными")
            return
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = 2 * math.pi * r * (r + h)
        print(f"Полная поверхность = {S:.4f}")
    elif act == 2:
        S = 2 * math.pi * r * h
        print(f"Боковая поверхность = {S:.4f}")
    elif act == 3:
        V = math.pi * r * r * h
        print(f"Объём = {V:.4f}")


def cone_calc():
    """Конус."""
    print("\n--- Конус ---")
    print("1 — Площадь полной поверхности")
    print("2 — Площадь боковой поверхности")
    print("3 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2,3):
            print("Неверный номер")
            return
        r = float(input("Радиус основания: "))
        h = float(input("Высота: "))
        if r <= 0 or h <= 0:
            print("Радиус и высота должны быть положительными")
            return
        l = math.sqrt(r*r + h*h)  # образующая
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = math.pi * r * (r + l)
        print(f"Полная поверхность = {S:.4f}")
    elif act == 2:
        S = math.pi * r * l
        print(f"Боковая поверхность = {S:.4f}")
    elif act == 3:
        V = (1/3) * math.pi * r * r * h
        print(f"Объём = {V:.4f}")


def sphere_calc():
    """Шар."""
    print("\n--- Шар ---")
    print("1 — Площадь поверхности")
    print("2 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2):
            print("Неверный номер")
            return
        r = float(input("Радиус: "))
        if r <= 0:
            print("Радиус должен быть положительным")
            return
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = 4 * math.pi * r * r
        print(f"Площадь поверхности = {S:.4f}")
    elif act == 2:
        V = (4/3) * math.pi * r**3
        print(f"Объём = {V:.4f}")


def prism_calc():
    """Прямая призма (основание – произвольный многоугольник)."""
    print("\n--- Прямая призма ---")
    print("1 — Площадь боковой поверхности")
    print("2 — Площадь полной поверхности")
    print("3 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2,3):
            print("Неверный номер")
            return
        S_base = float(input("Площадь основания: "))
        P_base = float(input("Периметр основания: "))
        h = float(input("Высота призмы: "))
        if S_base <= 0 or P_base <= 0 or h <= 0:
            print("Все значения должны быть положительными")
            return
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = P_base * h
        print(f"Боковая поверхность = {S:.4f}")
    elif act == 2:
        S = 2 * S_base + P_base * h
        print(f"Полная поверхность = {S:.4f}")
    elif act == 3:
        V = S_base * h
        print(f"Объём = {V:.4f}")


def pyramid_calc():
    """Правильная пирамида."""
    print("\n--- Правильная пирамида ---")
    print("1 — Площадь боковой поверхности")
    print("2 — Площадь полной поверхности")
    print("3 — Объём")
    try:
        act = int(input("Что вычисляем? "))
        if act not in (1,2,3):
            print("Неверный номер")
            return
        S_base = float(input("Площадь основания: "))
        P_base = float(input("Периметр основания: "))
        if act in (1,2):
            l = float(input("Апофема (высота боковой грани): "))
        h = float(input("Высота пирамиды: "))
        if S_base <= 0 or P_base <= 0 or h <= 0 or (act in (1,2) and l <= 0):
            print("Все значения должны быть положительными")
            return
    except ValueError:
        print("Ошибка: нужно вводить числа")
        return

    if act == 1:
        S = 0.5 * P_base * l
        print(f"Боковая поверхность = {S:.4f}")
    elif act == 2:
        S = S_base + 0.5 * P_base * l
        print(f"Полная поверхность = {S:.4f}")
    elif act == 3:
        V = (1/3) * S_base * h
        print(f"Объём = {V:.4f}")


def solid_bodies():
    """Меню трёхмерных тел."""
    while True:
        print("\n" + "-"*40)
        print("    ПОВЕРХНОСТИ И ОБЪЁМЫ ТЕЛ (3D)")
        print("-"*40)
        print("1  — Прямоугольный параллелепипед")
        print("2  — Куб")
        print("3  — Цилиндр")
        print("4  — Конус")
        print("5  — Шар")
        print("6  — Прямая призма")
        print("7  — Правильная пирамида")
        print("0  — Назад")

        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Ошибка: введите номер")
            continue

        if choice == 0:
            break
        elif choice == 1:
            parallelepiped_calc()
        elif choice == 2:
            cube_calc()
        elif choice == 3:
            cylinder_calc()
        elif choice == 4:
            cone_calc()
        elif choice == 5:
            sphere_calc()
        elif choice == 6:
            prism_calc()
        elif choice == 7:
            pyramid_calc()
        else:
            print("Неверный номер. Попробуйте ещё раз.")


# ----------  ОБЩЕЕ МЕНЮ ПЛОЩАДЕЙ ----------

def areas_hub():
    """Выбор между двумерными и трёхмерными площадями/объёмами."""
    while True:
        print("\n" + "="*40)
        print("         ПЛОЩАДИ И ОБЪЁМЫ")
        print("="*40)
        print("1 — Двумерные площади (треугольник, квадрат, круг...)")
        print("2 — Трёхмерные тела (поверхности и объёмы)")
        print("0 — Назад в главное меню")

        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Ошибка: введите 1, 2 или 0")
            continue

        if choice == 0:
            break
        elif choice == 1:
            flat_areas()
        elif choice == 2:
            solid_bodies()
        else:
            print("Неверный номер. Попробуйте ещё раз.")


# ----------  ГЛАВНОЕ МЕНЮ ----------

def main():
    while True:
        print("\n" + "="*40)
        print("      МАТЕМАТИЧЕСКИЙ КАЛЬКУЛЯТОР")
        print("="*40)
        print("1 — Квадратное уравнение")
        print("2 — Прогрессии (арифм. и геом.)")
        print("3 — Площади фигур и объёмы тел")
        print("4 — Тригонометрия (sin, cos, tg, ctg)")
        print("0 — Выход")

        try:
            option = int(input("Что будем считать? Введите номер: "))
        except ValueError:
            print("Ошибка: введите число от 0 до 4")
            continue

        if option == 0:
            print("До свидания!")
            break
        elif option == 1:
            solve_quadratic()
        elif option == 2:
            progressions_hub()
        elif option == 3:
            areas_hub()
        elif option == 4:
            trig()
        else:
            print("Неверный номер. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()