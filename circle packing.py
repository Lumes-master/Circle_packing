# Задание - найти максимальный коэффициент увеличения радиуса вписанных
# окружностей  одинакового размера, чтобы при этом они не перескались
# и не выходили за пределы большой окружности.

# rbig - радиус большой окружности
# coord координата точки - кортеж 2х значений (x - центр по оси х, y - центр по оси y)
# coord_sets  - массив точек
# rsmal - радиус маленькой окружности
#
from math import sqrt


def get_distance(coord1: tuple, coord2: tuple):
    """функция считает расстояние между двумя точками на плоскости"""
    distance = sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)
    # print(distance)
    return distance


def get_rbig_min_distance_edge(rbig: float, coord_sets: tuple):
    """функция находит наименьшее растояние от края окружности до центра малой окрудности."""
    list_of_distances = []
    for i in coord_sets:
        """перебираем все точки и считаем расстояние от центра с помощью функции get distance"""
        distance = get_distance((0, 0), i)
        list_of_distances.append(distance)
    return rbig - max(list_of_distances)


def get_shortest_distance_between_small(rbig: float, coord_sets: tuple):
    """функция поочередно считает все расстояния между заданними точками.
    Сложность рассчета возрастает  в геометрической прогрессии
    в зависимости от числа точек. За исходную минимальную величину
    берем  диаметр большой окружности. Если расстояние между двумя
    точками меньше, оно становится новим минимумом. И каждий раз при
    нахождении нового минимума  величина 'start_min_dist' обновляется.
    """
    start_min_dist = rbig * 2
    for i in range(len(coord_sets)):
        for j in range(i + 1, len(coord_sets)):
            current_distance = get_distance(coord_sets[i], coord_sets[j])

            if current_distance < start_min_dist:
                start_min_dist = current_distance
                print(start_min_dist)
    return start_min_dist


def max_lambda(rbig: float, rsmal: float, coord_sets: tuple):
    """Функция принимает радиус большой окружности, малой,
    массив координат центров. Считает минимальное расстояние
    до края большой окружности. Считает минимальное расстояние
    между 2 точками и делит на 2.
    Меньшее из полученних значений - макс радиус малой окружности.
    Делим его на радиус, получаем лямбду.
    """
    rbig_min_distance = get_rbig_min_distance_edge(rbig, coord_sets)
    shortest_distance_small = get_shortest_distance_between_small(rbig, coord_sets)
    distance = min(rbig_min_distance, (shortest_distance_small / 2))
    answer_lambda = distance / rsmal
    if answer_lambda < 1:
        raise ValueError('Your small circle coordinates contain un error')
    print('answer: ', answer_lambda)
    return answer_lambda


if __name__ == '__main__':
    max_lambda(100, 2.5, ((-1, -1), (7, 8.1), (25, 24), (17, 13)))
    # answer: 1.094875162046673
