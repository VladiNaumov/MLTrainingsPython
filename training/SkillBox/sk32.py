# Продвинутый уровень понимания линейной регрессии

"""
Давайте посмотрим, как обучить модель линейной регрессии, пользуясь только библиотечными функциями - имеенно их вы будете применять при решении реальных задач на работе
Сначала реализуем вспомогательную функцию для печати чисел питоновского типа float в красивом виде без большого количества знаков после запятой:
"""

from sklearn.datasets import load_boston
from numpy.linalg import inv
from sklearn.linear_model import LinearRegression

# функция для красивого вывода результата 
def ndprint(a, format_string ='{0:.2f}'):
    """Функция, которая распечатывает список в красивом виде"""
    return [format_string.format(v,i) for i,v in enumerate(a)]

"""
Загружаем исходные данные - датасет с ценами на дома в Бостоне (boston_dataset = load_boston()). 
Это стандартный датасет, который используется для демонстрации алгоритмов настолько часто, что включён прямо в исходный код библиотеки sklearn.
"""

boston_dataset = load_boston()
features = boston_dataset.data

# вывод формы (features.shape)
print('Матрица Объекты X Фичи (размерность): %s %s' % features.shape) 
# вывод равен 506/13

y = boston_dataset.target
print('\nЦелевая переменная y (размерность): %s' % y.shape)
# вывод формы (y.shape) 506

# Исходя из наблюдения мы работаем с датасетом 506 наблюдений, У каждого наблюдения 13 фичей 
# Таким образом наша модель "boston_dataset" это вектор w в котором 13 компонентов w1, w2.....w по одному коэффициенту на кажую свичу

# текстовое описание датасета  - распечатать, если интересно print('\n',boston_dataset.DESCR)


# вычисляем коэффициенты линейной регрессии (наша написанная функция согласно формулы по вычислению линейной регрессии)
w_analytic = inv(
    features.T.dot(features)
).dot(
    features.T
).dot(
    y
)
print("Коэффициенты, вычисленные нашей написанной функцией \n%s" % ndprint(w_analytic))


# обучаем модель "из коробки"

# создаём объект
reg = LinearRegression()
# из библеотеки sklearn за обучение отвечает метод fit() подставляем туда значение наших витчей и целевой переменной y на которой мы хотим обучится
reg.fit(features, y)

# распечатываем наши коэффициентыю Коэфициенты (находятся coef_)
print("Коэффициенты, вычисленные моделью sklearn \n%s" % ndprint(reg.coef_))

"""
Мы реадезовали обучение модели линейной регрессии с помощью классов sklearn.linear_model и linearRegression 
который вычисляет коэффициенты приблежонною На практике используют имеено вышесказанные классы.

Данную функцию аналитическую функцию на практике не используютб потому что она является дорогостоящая по ресурсам машины 
def ndprint(a, format_string ='{0:.2f}'):
    """Функция, которая распечатывает список в красивом виде"""
    return [format_string.format(v,i) for i,v in enumerate(a)]
"""




