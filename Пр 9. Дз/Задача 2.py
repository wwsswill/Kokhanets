def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()

    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        return True
    else:
        return False


if is_right_triangle(3, 4, 5):
    print("Треугольник является прямоугольным.")
else:
    print("Треугольник не является прямоугольным.")
