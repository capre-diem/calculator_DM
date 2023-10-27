# Модуль: MOD_NN_N
# Автор: Кузнецов_Илья_2381

from .Natural import Natural
# from div import div
# from subtract_product_from_natural import subtract_product_from_natural


def mod(num1: Natural, num2: Natural) -> Natural:
    if int(num2) == 0:
        raise ZeroDivisionError
    return num1.subtract_product_from_natural((num1.div(num2)), int(num2))
