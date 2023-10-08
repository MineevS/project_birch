import random

def generate_random_pairs(num_pairs, filename):
    x1 = ["{:.2f}".format(random.uniform(0, 1)) for _ in range(num_pairs)]
    x2 = ["{:.2f}".format(random.uniform(0, 1)) for _ in range(num_pairs)]

    with open(filename, 'w') as file:
        file.write("x1 = [\n")
        file.write("    " + ",\n    ".join(x1) + "\n")
        file.write("]\n\n")

        file.write("x2 = [\n")
        file.write("    " + ",\n    ".join(x2) + "\n")
        file.write("]\n")

# Пример использования функции для создания 10 пар случайных чисел и сохранения их в файл example.py
generate_random_pairs(10, 'example.py')
